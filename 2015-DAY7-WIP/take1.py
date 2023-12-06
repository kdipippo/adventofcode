import re

def read_file_into_words(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

class Circuit:
    def __init__(self, instructions):
        self.signals = {}
        for instruction in instructions:
            self.read_instruction(instruction)

    def read_instruction(self, instruction: str):
        print(instruction)
        if "AND" in instruction:
            # "(1)x AND (2)y -> (3)z"
            parts = re.search("^(\w+) AND (\w+) -> (\w+)$", instruction)
            self.set_signal(
                parts.group(3),
                instr_bitwise_and(
                    self.get_signal(parts.group(1)),
                    self.get_signal(parts.group(2))
                )
            )
        elif "OR" in instruction:
            # "(1)x OR (2)y -> (3)z"
            parts = re.search("^(\w+) OR (\w+) -> (\w+)$", instruction)
            self.set_signal(
                parts.group(3),
                instr_bitwise_or(
                    self.get_signal(parts.group(1)),
                    self.get_signal(parts.group(2))
                )
            )

        elif "LSHIFT" in instruction:
            # "(1)p LSHIFT (2)2 -> q"
            parts = re.search("^(\w+) LSHIFT (\w+) -> (\w+)$", instruction)
            self.set_signal(
                parts.group(3),
                instr_lshift(
                    self.get_signal(parts.group(1)),
                    int(parts.group(2))
                )
            )

        elif "RSHIFT" in instruction:
            # "(1)p RSHIFT (2)2 -> q"
            parts = re.search("^(\w+) RSHIFT (\w+) -> (\w+)$", instruction)
            self.set_signal(
                parts.group(3),
                instr_rshift(
                    self.get_signal(parts.group(1)),
                    int(parts.group(2))
                )
            )

        elif "NOT" in instruction:
            # "NOT (1)x -> (2)y"
            parts = re.search("^NOT (\w+) -> (\w+)$", instruction)
            self.set_signal(
                parts.group(2),
                instr_not(
                    self.get_signal(parts.group(1))
                )
            )
        else:
            # "(1)123 -> (2)x"
            parts = re.search("^(\w+) -> (\w+)$", instruction)
            if parts.group(1).isalpha():
                self.set_signal(
                    parts.group(2),
                    self.get_signal(parts.group(1))
                )
            else:
                self.set_signal(
                    parts.group(2),
                    int(parts.group(1))
                )

    def set_signal(self, signal, value):
        self.signals[signal] = value
    
    def get_signal(self, signal):
        if signal in self.signals:
            return self.signals[signal]
        return 0

def adjust_for_negatives(value: int) -> int:
    if value < 0:
        value += 65536
    return value

def instr_bitwise_and(value_a: int, value_b: int) -> int:
    return adjust_for_negatives(value_a & value_b)

def instr_bitwise_or(value_a: int, value_b: int) -> int:
    return adjust_for_negatives(value_a | value_b)

def instr_lshift(value: int, left_shift: int) -> int:
    return adjust_for_negatives(value << left_shift)

def instr_rshift(value: int, left_shift: int) -> int:
    return adjust_for_negatives(value >> left_shift)

def instr_not(value: int) -> int:
    return adjust_for_negatives(~value)

def main():
    instructions = read_file_into_words("input.txt")
    circuit = Circuit(instructions)
    return circuit.signals
    return circuit.signals["a"]

if __name__ == "__main__":
    print(main())
