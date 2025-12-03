def dial(position:int ,up:bool, num:int, count:int):
  print(f"start {position}")
  if up is True:
    position +=num
  else:
    position -=num

  print(f"calc {position}")
  while position< 0 or position > 99:  
    if position < 0:
      position=99 - abs(position)
      count += 1
  
    if position > 99:
      position=position - 99
      count +=1

  return position,count

# TODO einlesen der listenelemte 
# parse ersten buchstaben -> R = True
# wandle nächsten teil in int um

with open("puzzle_input", "r", encoding="utf-8") as f:
    dials = [line.strip() for line in f]
print(len(dials))    

where,password=dial(0,False,4000,0)
print(where)
print(password)
