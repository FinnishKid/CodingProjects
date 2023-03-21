import os
import time

clear = lambda: os.system('cls')
sleep = lambda: time.sleep(.001)
lights = [0] * 100
xNew = 0
lights[0] = 1

for x in range(1, 101):
  y = x
  while (y < 100):
    if (lights[y] == 0):
      lights[y] = 1
    else:
      lights[y] = 0
    print(lights)
    sleep()
    clear()
    y += x
    
print(lights)

count = 0
for x in lights:
  if (x == 1):
    count += 1
print("Total number of lightbulbs turned on: " + str(count))