import time
from random import random as rand

print("Watch out here comes the snake...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("THE SNAKE IS HERE!!!")
time.sleep(1)

MAX_SNAKE_POS = 40

snake_pos = 0
snake_direction = "right"
consecutive_same = 0
while True:
    change_direction = False
    if snake_pos <= 0 and snake_direction == "left":
        change_direction = True
    elif snake_pos >= MAX_SNAKE_POS and snake_direction == "right":
        change_direction = True
    else:
        if consecutive_same >= 5: # Force new direction.
            change_direction = True
        elif consecutive_same >= 2: # Consider new direction.
            if rand() <= 0.35: # 35% chance to change direction.
                change_direction = True    
    
    if change_direction:
        snake_direction = "left" if snake_direction == "right" else "right"
        consecutive_same = 0
    
    consecutive_same += 1
    
    if change_direction:
        time.sleep(0.2)
        print((" " * snake_pos) + "|")
    
    snake_pos += -1 if snake_direction == "left" else 1
    
    time.sleep(0.2)
    spooky_part = "/" if snake_direction == "left" else "\\"
    print((" " * snake_pos) + spooky_part)
