# Catching KeyboardInterrupt exception
"""The second method reacting to is catching the
KeyboardInterrupt exception. It can be useful in a
script which is single threaded and also in
long-running task situations
which can be skipped but not canceling the whole script."""

import time # use time library to simulate a running task

# long running task in try block

try:
    while True:
        print("Heavy Task!")
        time.sleep(2)
except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught")

print("Continuing script execution.")
