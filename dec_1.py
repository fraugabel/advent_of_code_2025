import pdb

def dial(position: int, up: bool, num: int, count: int):
    print(f"########## start {position}")
    print(f"{num} (up:{up})")
    start_zero=False
    if position == 0:
        start_zero = True

    if up is True:
        position += num
    else:
        position -= num
    print(f"calc {position}")
    #pt1:
    if position == 0:       
        count += 1
        print(f"count {count}")
        return position, count
    else:
        while position < 0 or position > 99:
            if position < 0:
                position = 100 - abs(position)
            if position > 99:
                position = position - 100
            if not start_zero:
                count += 1 #pt2
            else:
                start_zero = False
            print(f"in loop {position}")
            print(f"count {count}")
    return position, count


# initiation
where = 50
password = 0
dial_up = True
dial_num = 0
#file = "test_input_1"
#file = "test_input_2"
file = "puzzle_input"

with open(file, "r", encoding="utf-8") as f:
    dials = [line.strip() for line in f]
print(f"number of dials {len(dials)}")

for d in dials:
    if d[0] == "R":
        dial_up = True
    else:
        dial_up = False
    dial_num = int(d[1:])
    where, password = dial(where, dial_up, dial_num, password)

print(f"########## end  {where}")
print(f"pw: {password}")
