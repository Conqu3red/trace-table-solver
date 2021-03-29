from tracker import Tracker, Tracer
import sys

request = {"variables":["a","b","c"], "code": "a=1\nb=2\nb=3", "parameters": {"compact": True}}

def print_trace_table(request):
    def temp():
        exec(request["code"])
    tracker = Tracker(**request["parameters"])
    targets = request["variables"]
    
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

    temp()

    sys.settrace(None)

    print(tracker.displayTraceTable())

print_trace_table(request=request)


with Tracer(["a","b","c"], compact=True):
    def TotalOut(a, b):
        c = a + b
        while a < c:
            a = a + 1
            b = b - a
        return b 
    
    TotalOut(3, 4)