maze = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 2]]
from queue import Queue  

# maze defined as above within an array

debug = input("Debug mode?")
from colorama import Fore
if debug == "True":
  print(Fore.GREEN + 'debug on') # ignore, shitty debug code

def threader():
    while True:
        pathFinding(queue.get())
        queue.task_done()
if debug == "True":
  print("1")
import threading
print_lock = threading.Lock()
NUMBER_OF_THREADS = int(input("Enter the amount of threads allocated for the scan: "))
for _ in range(NUMBER_OF_THREADS):
    thread = threading.Thread(target=threader)
    thread.daemon = True 
    thread.start()
queue = Queue() # threading (not even sure this works tbh, take with grain of salt)
if debug == "True":
  print("2")
def pathFinding(x, y): 
    if maze[x][y] == 2:
        print(f"found at {x},{y}")
        return True
    elif maze[x][y] == 1:
        print(f"wall at {x},{y}")
        return False
    elif maze[x][y] == 3:
        print (f"visited at {x},{y}")
        return False
    print (f"visiting at {x},{y}")
    maze[x][y] = 3
    if ((x < len(maze)-1 and pathFinding(x+1, y))
        or (y > 0 and pathFinding(x, y-1))
        or (x > 0 and pathFinding(x-1, y))
        or (y < len(maze)-1 and pathFinding(x, y+1))): # pathfinding algorithm
        return True
    return False
if debug == "True":
  print("3")

pathFinding(0, 0)


print(maze) # prints out solved maze - follow the trail of 3s from 0, 0 to endpoint

if debug == "True":
  print("debug complete")
