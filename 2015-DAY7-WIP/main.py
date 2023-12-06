import re
import sys

def read_file_into_words(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

class CircuitInstructions:
    def __init__(self, input_instructions):
        self.signals = {}
        self.instructions = []

        for instruction in input_instructions:
            parts = instruction.split(" -> ")
            self.signals[parts[1]] = parts[0]
        self.todo = list(self.signals.keys())
        self.print_signal("a")
        self.display_instructions()

    def print_signal(self, signal):
        # Don't print anything if the signal is an integer
        if not signal.isalpha():
            return
        if signal not in self.todo:
            return
        instruction = self.signals[signal]
        line = f"{instruction} -> {signal}"
        self.instructions.append(line)
        self.todo.remove(signal)

        if len(self.todo) == 0:
            return

        if "AND" in instruction:
            parts = re.search("^(\w+) AND (\w+)$", instruction)
            self.print_signal(parts.group(2))
            self.print_signal(parts.group(1))
        elif "OR" in instruction:
            parts = re.search("^(\w+) OR (\w+)$", instruction)
            self.print_signal(parts.group(2))
            self.print_signal(parts.group(1))
        elif "LSHIFT" in instruction:
            parts = re.search("^(\w+) LSHIFT (\w+)$", instruction)
            self.print_signal(parts.group(2))
            self.print_signal(parts.group(1))
        elif "RSHIFT" in instruction:
            parts = re.search("^(\w+) RSHIFT (\w+)$", instruction)
            self.print_signal(parts.group(2))
            self.print_signal(parts.group(1))
        elif "NOT" in instruction:
            parts = re.search("^NOT (\w+)$", instruction)
            self.print_signal(parts.group(1))
        else:
            self.print_signal(instruction)

    def display_instructions(self):
        print(self.todo)
        self.instructions.reverse()
        for line in self.instructions:
            print(line)

def main():
    instructions = read_file_into_words("input.txt")
    circuit_instructions = CircuitInstructions(instructions)

if __name__ == "__main__":
    print(main())
