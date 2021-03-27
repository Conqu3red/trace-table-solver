from tracker import Tracker, VarContainer


tracker = Tracker()
t = VarContainer(tracker.onchange)

def _print(msg, *args, **kwargs):
    t.output = msg
    print(msg, *args, **kwargs)

t.turns = 0
t.x = 3

while t.turns < 22:
    t.x = t.x * 3
    t.turns = t.turns + 3

_print(t.turns)

_print(t.x)


print(tracker.displayTraceTable())