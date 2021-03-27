from tabulate import tabulate
from typing import *

class VarContainer:
    def __init__(self, onchange):
        super(VarContainer, self).__setattr__("onchange", onchange)

    def __setattr__(self, name, value):
        #print(f"Setting {name} to {value}")
        self.onchange(name, value)
        super(VarContainer, self).__setattr__(name, value)

class Tracker:
    def __init__(self):
        self.values = {}
        self.line = 0
    
    def onchange(self, name, value):
        #print(f"{name} -> {value}")
        data: dict = self.values.get(name, {})
        
        #while self.line in data.keys():
        self.line += 1
        
        data[self.line] = value

        self.values[name] = data
    def displayTraceTable(self, variables: List[str] = None) -> str:
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
        return tabulate(table, headers=headers, tablefmt="psql")