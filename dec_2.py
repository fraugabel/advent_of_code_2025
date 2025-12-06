file = "test_input_2"

def digitize(num:int):
    '''
    seperates numberes into their digits
    checks whether digit count is even
    if so compares digits and returns digit count
    and found twins of null
    :param num: int number
    '''
    dig_list = [int(z) for z in str(num)]
    dig_count=len(dig_list)
    rest=dig_count % 2
    if rest == 0:
        half=int(dig_count/2)
        same=0
        for i in range(0,half):            
            if {dig_list[i]} == {dig_list[half+i]}:
                same += 1
        if same == half:
            return dig_count,dig_list
    
    return dig_count, 0

def return_numbers(dig_count,num_list):
    '''
    takes digit count and digit list 
    multiplies each element with their positional dezimal
    
    :param dig_count: count of digits
    :param num_list: list of digits
    '''
    num=0
    for i in range(0,dig_count):
        dezi=pow(10,i)
        prod=num_list[dig_count-i-1]*dezi
        num += prod
    return num

def stringlize(numlist):
    num_string_list=list(map(str, numlist))
    substring = num_string_list[0]
    count = sum(substring in s for s in num_string_list)
    print(f"sub {count}")
    return

with open(file) as f:
    all_ids =" ".join(line.strip() for line in f)
# split input into a list of ranges as strings
ranges = [teil.strip() for teil in all_ids.split(",")]
filtered_out=[]

# split ranges into lists with start and end as int
for single_range in ranges:
    single_range = [int(teil.strip()) for teil in single_range.split("-")]
    # fill up the ranges
    filled_range=list(range(single_range[0],single_range[1]+1))
    stringlize(filled_range)
    for num in filled_range:
        dig_count, evol_twins=digitize(num)
        if evol_twins != 0:
            print(evol_twins)
            filtered_out.append(return_numbers(dig_count, evol_twins))

print(filtered_out)        
print(sum(filtered_out))

