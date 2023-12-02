def read_file_into_words(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def get_letternum_in_str(input_str: str) -> int:
    letternums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, letternum in enumerate(letternums):
        if letternum in input_str:
            return num
    return -1

def get_first_digit(input_str):
    substr = ""
    for char in range(len(input_str)):
        # If we encounter numeric character, return.
        if input_str[char] in "0123456789":
            return int(input_str[char])
        # Otherwise, look at current substring.
        substr = substr + input_str[char]
        possible_value = get_letternum_in_str(substr)
        if possible_value != -1:
            return possible_value

def get_last_digit(input_str):
    substr = ""
    for char in reversed(range(len(input_str))):
        # If we encounter numeric character, return.
        if input_str[char] in "0123456789":
            return int(input_str[char])
        # Otherwise, look at current substring.
        substr = input_str[char] + substr
        possible_value = get_letternum_in_str(substr)
        if possible_value != -1:
            return possible_value

def get_test_input():
    return ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

def get_full_input():
    return read_file_into_words("input.txt")


def main():
    inputs = get_full_input()
    sum = 0
    for line in inputs:
        sum += int(f"{get_first_digit(line)}{get_last_digit(line)}")
    return sum

if __name__ == "__main__":
    print(main())
