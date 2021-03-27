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