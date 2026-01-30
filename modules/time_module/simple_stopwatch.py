# build a stopwatch program using the time module
# ask the user to press 1 to start the stopwatch
# if the user presses 1, start the stopwatch and print the current time
# ask the user to press 0 to stop the stopwatch
# if the user presses 0, stop the stopwatch and print the current time
# and print the elapsed time
# if the user presses any other key, print "Invalid input"

import time

print("###########################")
print("The Simple Stopwatch Program")
print("###########################")
print("-------------------------------------")
start = input("Press 1 to start the stopwatch: ")
print("-------------------------------------")
if start == "1":
    start_time = time.time()
    print("Stopwatch started at: ", time.ctime())
    print("-------------------------------------")
    end = input("Press 0 to stop the stopwatch: ")
    print("-------------------------------------")
    if end == "0":
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 1)
        print("Stopwatch stopped at: ", time.ctime())
        print("-------------------------------------")
        print(f"Elapsed time: {elapsed_time} seconds")
        print("-------------------------------------")
    else:
        print("Invalid input")
        print("-------------")

else:
    print("Invalid input")
    print("-------------")

print("###########################")
print("Stopwatch Program completed")
print("###########################")
