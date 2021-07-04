
import time
print("Type your task?")
text = str(input())
print("when you will do it ?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)
