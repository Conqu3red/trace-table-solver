import sys
from tracker import Tracker, trace


@trace(["a", "b", "c"], displayOnComplete=True, trackerArguments={"compact": True})
def some_function():
    # put code to be traced here
    def TotalOut(a, b):
        c = a + b

        while a < c:
            a = a + 1
            b = b - a

        return b
    
    TotalOut(3, 4)


some_function()