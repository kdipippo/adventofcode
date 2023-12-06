def read_file_into_words(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def convert_to_2d_list(list1d):
    final_list = []
    inner_list = []
    for entry in list1d:
        if entry == "":
            final_list.append(inner_list)
            inner_list = []
        else:
            inner_list.append(entry)
    final_list.append(inner_list)
    return final_list

class SeedsTracker:
    def __init__(self, seeds_str):
        self.before_nums = parse_seeds(seeds_str)
        self.after_nums = []

    def process_map_row(self, map_row_str):
        # ["destination range start", "source range start", "range length"]
        map_row = [int(entry) for entry in map_row_str.split()]
        for num in self.before_nums[:]: # Loop over array copy while we delete items.
            # print(f"{map_row[1]} <= {num} < {(map_row[1] + map_row[2])}")
            if map_row[1] <= num < (map_row[1] + map_row[2]):
                # Calculate mapping.
                new_num = map_row[0] + (num - map_row[1])
                print(f"Convert {num} -> {new_num}")
                self.after_nums.append(new_num)
                self.before_nums.remove(num)

    def migrate_rows_after_processing(self):
        print(f"Passing {', '.join([str(entry) for entry in self.before_nums])}")
        for entry in self.after_nums:
            self.before_nums.append(entry)
        self.after_nums = []

def parse_seeds(seeds_str):
    return [int(entry) for entry in seeds_str.replace("seeds: ", "").split()]

def main():
    inputs = read_file_into_words("fullinput.txt")
    grouped_instructions = convert_to_2d_list(inputs)
    seeds_tracker = SeedsTracker(grouped_instructions[0][0])
    for instr_index in range(1, len(grouped_instructions)):
        print(f"\nProcessing '{grouped_instructions[instr_index][0]}'")
        for row_index in range(1, len(grouped_instructions[instr_index])):
            seeds_tracker.process_map_row(grouped_instructions[instr_index][row_index])
        seeds_tracker.migrate_rows_after_processing()
        print(seeds_tracker.before_nums)
    print(min(seeds_tracker.before_nums))


if __name__ == "__main__":
    main()
