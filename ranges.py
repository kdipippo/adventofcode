class Ranges:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.diff = end - start
    def __str__(self):
        return f"{self.start} -{self.diff}-> {self.end}"

# Just a helper so that it's easy to not have to determine who's lower.
def get_range_overlap(range1, range2):
    if range1.start <= range2.start:
        return get_range_overlap_inner(range1, range2)
    return get_range_overlap_inner(range2, range1)

def get_range_overlap_inner(lower, higher):
    # ranges do not overlap.
    # start----end  START----END
    if lower.end < higher.start:
        return False

    # ranges are the same.
    # startSTART========endEND
    if lower.start == higher.start and lower.end == higher.end:
        return lower

    # higher range is inside lower range.
    # start----START==END----end
    if lower.start <= higher.start and higher.end <= lower.end:
        return higher

    # lower and higher ranges overlap.
    # start----START==end----END
    return Ranges(higher.start, lower.end)

class MachineRow:
    def __init__(self, input_str):
        numbers = [int(entry) for entry in input_str.split()]
        self.input_range = Ranges(numbers[1], numbers[1]+numbers[2])
        self.output_range = Ranges(numbers[0], numbers[0]+numbers[2])
    def __str__(self):
        return f"{str(self.input_range)}   {str(self.output_range)}"

machine1 = []
machine1.append(MachineRow("88 18 7"))
machine1.append(MachineRow("18 25 70"))

machine2 = []
machine2.append(MachineRow("45 77 23"))
machine2.append(MachineRow("81 45 19"))
machine2.append(MachineRow("68 64 13"))

for machine_row in machine1:
    print(machine_row)
print()
for machine_row in machine2:
    print(machine_row)

# print(get_range_overlap(test1, test2))

