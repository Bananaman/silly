import time

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

spooky_parts = ["\\", " \\", "  |", "  /", " /", "/", "|"]
while True:
    for part in spooky_parts:
        time.sleep(0.2)
        print(part)
