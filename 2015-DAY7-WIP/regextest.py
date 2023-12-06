import re

text = "x LSHIFT 2 -> f"
matches = re.search("^(\w+) LSHIFT (\w+) -> (\w+)$", text)
print(matches.group(0))
print(matches.group(1))
print(matches.group(2))
print(matches.group(3))