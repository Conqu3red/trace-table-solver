from tabulate import tabulate
from typing import *
from collections.abc import Callable
import sys

class VarContainer:
    def __init__(self, onchange: Callable):
        self._onchange = onchange

    def __setattr__(self, name, value):
        if name != "_onchange":
            self._onchange(name, value)
        super(VarContainer, self).__setattr__(name, value)

class Tracker:
    def __init__(self, compact=False):
        self.values = {}
        self.line = 0
        self.compact = compact
    
    def onchange(self, name, value):
        #print(f"{name} -> {value}")
        data: dict = self.values.get(name, {})
        
        #while self.line in data.keys():
        if data.get(self.line) != None or not self.compact:
            self.line += 1
        
        data[self.line] = value

        self.values[name] = data
    def displayTraceTable(self, variables: List[str] = None, tablefmt="github") -> str:
        headers = list(self.values.keys())
        if variables:
            headers = variables
        
        maxLine = max([max(l.keys()) for l in self.values.values()])
        
        table = []
        for i in range(maxLine+1):
            row = []
            for h in headers:
                row.append(self.values[h].get(i, ""))
            table.append(row)
        return tabulate(table, headers=headers, tablefmt=tablefmt)


def arg_decorator(fn):
    def wrapped_decorator(*args, **kwargs):
        def real_decorator(decoratee):
            return fn(decoratee, *args, **kwargs)

        return real_decorator
    return wrapped_decorator

@arg_decorator
def trace(function, targets, tracker: Tracker, displayOnComplete=False):
    if targets == None:
        targets = []
    def wrapper(*args, **kwargs):
        def tracer(frame, event, arg = None):
            code = frame.f_code
            line_no = frame.f_lineno
            #tracker.onchange("_line_number", line_no)
            for v in targets:
                if len(tracker.values.get(v, {}).keys()) > 0:
                    if tracker.values[v][max(tracker.values[v].keys())] == frame.f_locals.get(v):
                        continue
                if v in frame.f_locals.keys():
                    tracker.onchange(v, frame.f_locals.get(v))
            return tracer
        
        sys.settrace(tracer)
        
        response = function(*args, **kwargs)
        
        if displayOnComplete:
            print(tracker.displayTraceTable(targets))
        
        sys.settrace(None)
        
        return response
    return wrapper
