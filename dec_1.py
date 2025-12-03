def dial(position: int, up: bool, num: int, count: int):
    print(f"start {position}")
    if up is True:
        position += num
    else:
        position -= num
    print(f"calc {position}")
    while position < 0 or position > 99:
        if position < 0:
            position = 100 - abs(position+1)
            count += 1

        if position > 99:
            position = position - 100
            count += 1

    return position, count


# initiation
where = 50
password = 0
dial_up = True
dial_num = 0
file = "test_input"

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

print(where)
print(password)
