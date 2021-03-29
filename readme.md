# Trace Table Solver
A simple program to create trace tables.

## Getting Started
Here is a template code snippet:
```python
from tracker import Tracker, VarContainer
tracker = Tracker() # initialise tracker
t = VarContainer(tracker.onchange) # create variable container with reference to tracker onchange

t.a = 0 # setting variables
t.b = 1
t.a = 2

print(tracker.displayTraceTable()) # display trace table
```

An alternative way to do this using the trace decorator:
```python
from tracker import trace

@trace(["a", "b"], displayOnComplete=True, trackerArguments={"compact": True})
def traced_function():
    a = 0
    b = 1
    a = 2

traced_function()
# Outputs:
# |   a | b   |
# |-----|-----|
# |   0 | 1   |
# |   2 |     |
```