# build a download timer program using the time module as:
# ask the user to enter the size of the file in MB
# and the speed of the internet in Mbps
# and calculate the time it will take to download the file
# and use countdown to simulate the download process
# at the end print "Download completed in {time} seconds"
#################################################################
import time
#################################################################
print("#########################")
print("Download Timer Program")
print("#########################")
#################################################################
file_size = float(input("Enter the file size in MB: "))
internet_speed = float(input("Enter the internet speed in Mbps: "))
print("-------------------------")
time_to_download = round((file_size * 8) / internet_speed, 3)
################################################################
countdown = round(time_to_download)
while countdown > 0:
    print(f"time remaining: {countdown} seconds")
    countdown -= 1
    time.sleep(1)
#################################################################
print(f"Download completed in {time_to_download} seconds")
#################################################################
print("#########################")
print("Download Timer Program Completed Successfully")
print("#########################")
#################################################################
