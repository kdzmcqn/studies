# Catching a SIGINT

"""
Catching the SIGINT Signal may be useful
for scripts or application which are
multithreaded or when it’s necessary
to be caught during the whole script execution.
"""
# Import signal library
import signal

# Handler for the caught KeyboardInterrupt SIGINT
"""Now we need to add a function which is executed 
as soon as the SIGINT has been caught."""

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID:{}) has been caught. Cleaning up...".format(signal))
    exit(0)

"""As you can see, the function takes two positional arguments. 
The signal (integer) and the frame (object). 
The signal variable is an integer which represents the number of the caught signal. 
For SIGINT it’s the two (2). 
The frame variable represents the current Python stack frame 
which can be useful for debugging purposes."""

# Register a signal action
"""To execute a function before quitting the program you need to register an action."""

signal.signal(signal.SIGINT, keyboardInterruptHandler)

# Executing a long-running task
"""Now we’re executing a long-running task which will be interrupted by SIGINT."""

while True:
    pass
# Script will never end on its own