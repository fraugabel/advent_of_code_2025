file = "puzzle_input_2"


    # pseudocode:
    # count digits and look for numbers that could be devided by 2, 
    # split into two parts
    # look for matching two parts maybe sum up both parts
    # add them up 

def digitize(num:int):
    dig_list = [int(z) for z in str(num)]
    dig_count=len(dig_list)
    rest=dig_count % 2
    #print(f"{dig_count} rest {rest}")
    if rest == 0:
        half=int(dig_count/2)
        same=0
        for i in range(0,half):            
            #print(f"{dig_list[i]} vs {dig_list[half+i]}")
            if {dig_list[i]} == {dig_list[half+i]}:
                same += 1
        if same == half:
            return dig_count,dig_list
    
    return dig_count, 0

def return_numbers(dig_count,num_list):
    num=0
    for i in range(0,dig_count):
        dezi=pow(10,i)
        prod=num_list[dig_count-i-1]*dezi
        num += prod
        print(f"factor {dezi} num {num}")
    return num


with open(file) as f:
    all_ids =" ".join(line.strip() for line in f)
# split input into a list of ranges as strings
ranges = [teil.strip() for teil in all_ids.split(",")]
print(ranges)

filtered_out=[]

# split ranges into lists with start and end as int
for single_range in ranges:
    single_range = [int(teil.strip()) for teil in single_range.split("-")]
    # fill up the ranges
    filled_range=list(range(single_range[0],single_range[1]+1))
    print(filled_range)
    for num in filled_range:
        dig_count, evol_twins=digitize(num)
        if evol_twins != 0:
            print(evol_twins)
            filtered_out.append(return_numbers(dig_count, evol_twins))

print(filtered_out)        

print(sum(filtered_out))

