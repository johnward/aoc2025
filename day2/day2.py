from pathlib import Path

def check_ids(start_id, end_id) -> int:
    id_total = 0

    for current_id in range(start_id, end_id):
        id_str = str(current_id)
        str_len = len(id_str)
        if str_len > 1 and (str_len % 2 == 0):
            pos = int(str_len/2)
            front = id_str[:pos]
            back = id_str[pos:] 

            if front == back:
                print(f"INVALID: {id_str}")
                id_total += int(id_str)
            
    return id_total

script_dir = Path(__file__).parent
input_path = script_dir / "input.txt"
print (f"Path = {input_path}")

with open(input_path, "r") as file:
    content = file.read()

lines = content.split(',')

total = 0
for line in lines:
    ids = line.split("-")
    print(f"{ids[0]}-{ids[1]}")
    total += check_ids(int(ids[0]), int(ids[1]))


print(f"Total: {total}")
