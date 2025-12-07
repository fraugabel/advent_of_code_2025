# go through the list from the beginnig take each number except the last and compare them to elem1 
# of a second list with 2 elems and keep the row number as stop  
# then go through the list from the end until stop and and compare each elemt with elem2
# synthese of second list and add up 

file = "puzzle_input_3"

def sort_joltage(bat_list):
    highest=['0','0']
    stop = 0
    maxi = len(bat_list)
    for i in range(0,maxi-1):
        if bat_list[i] > highest[0]:
            highest[0] = bat_list[i]
            stop = i
    print(bat_list)
    for i in range(stop+1,maxi):
            if bat_list[i] > highest[1]:
                highest[1] = bat_list[i]
    print(f"{highest} row {stop}")

    highest=list(map(int, highest))
    return highest

def return_numbers(num_list):
    '''
    takes digit count and digit list 
    multiplies each element with their positional dezimal
    
    :param dig_count: count of digits
    :param num_list: list of digits
    '''
    num=0
    dig_count = len(num_list)
    for i in range(0,dig_count):
        dezi=pow(10,i)
        prod=num_list[dig_count-i-1]*dezi
        num += prod
    return num

with open(file) as f:
    ranges =[line.strip() for line in f]

print(ranges)
total_output=0

# split ranges into lists with start and end as int
for single_range in ranges:
    single_range = list(single_range)
    highest = sort_joltage(single_range)
    joltage = return_numbers(highest) 
    total_output += joltage
    print(joltage)

print(total_output)
