from pathlib import Path

script_dir = Path(__file__).parent
input_path = script_dir / "input.txt"
print (f"Path = {input_path}")

with open(input_path, "r") as file:
    content = file.read()

input("File read, Press a key to continue")
lines = content.split('\n')

position = 50
max_pos = 99
min_pos = 0
zero_count = 0
line_count = 0

for line in lines:
    print(line)
    direction = line[0]
    numpart = int(line[1:])
    print(f"Direction: {direction}, Number: {numpart}")

    if direction == "L":    
        position = (position - numpart + 100) % 100

    if direction == "R":
        position = (position + numpart) % 100

    if position == 0:
        zero_count += 1

    line_count += 1
    
    print(f"Line Count: {line_count}")
    print(f"Position: {position}")


print(f"Password is {zero_count}")


