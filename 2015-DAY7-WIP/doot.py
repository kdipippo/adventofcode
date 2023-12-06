import re

def read_file_into_words(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def rewrite(instruction: str):
    if ("AND" in instruction) or ("OR" in instruction) or ("SHIFT" in instruction):
        parts = re.search("^(\w+) (\w+) (\w+) -> (\w+)$", instruction)
        if parts.group(1).isalpha():
            print(f"{parts.group(1)} --> {parts.group(4)}")
        if parts.group(3).isalpha():
            print(f"{parts.group(3)} --> {parts.group(4)}")
    elif "NOT" in instruction:
        # "NOT (1)x -> (2)y"
        parts = re.search("^NOT (\w+) -> (\w+)$", instruction)
        if parts.group(1).isalpha():
            print(f"{parts.group(1)} --> {parts.group(2)}")
    else:
        # "(1)123 -> (2)x"
        parts = re.search("^(\w+) -> (\w+)$", instruction)
        if parts.group(1).isalpha():
            print(f"{parts.group(1)} --> {parts.group(2)}")

def main():
    instructions = read_file_into_words("input.txt")
    for instruction in instructions:
        rewrite(instruction)

if __name__ == "__main__":
    main()
