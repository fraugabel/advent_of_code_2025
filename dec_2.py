file = "test_input_2"

with open(file) as f:
    all_ids =" ".join(line.strip() for line in f)
# split input into a list of ranges as strings
ranges = [teil.strip() for teil in all_ids.split(",")]
print(ranges)

# split ranges into lists with start and end as int
for single_range in ranges:
    single_range = [int(teil.strip()) for teil in single_range.split("-")]
    print(single_range)
    # fill up the ranges
    filled_range=list(range(single_range[0],single_range[1]+1))
    print(filled_range)
            
    # pseudocode:
    # count digits and look for numbers that could be devided by 2, 
    # split into two parts
    # look for matching two parts
    # add them up 