from tracker import Tracker, VarContainer


tracker = Tracker(compact=True)
t = VarContainer(tracker.onchange)

# begin problem
def TotalOut(a, b):
    t.a, t.b = a, b # must use variables in the varContainer
    t.c = t.a + t.b

    while t.a < t.c:
        t.a = t.a + 1
        t.b = t.b - t.a
    
    return t.b

TotalOut(3, 4)

# end problem
print(tracker.displayTraceTable())