def read_file_into_words(filename: str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

class CubeGame:
    def __init__(self, cube_game_str: str):
        self.game_id = -1
        self.sets = []

        # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        cube_game_parts = cube_game_str.split(": ")
        # ["Game 1","3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
        self.game_id = int(cube_game_parts[0].replace("Game ", ""))
        cube_game_sets_strs = cube_game_parts[1].split("; ")
        # ["3 blue, 4 red", "1 red, 2 green, 6 blue","2 green"]
        for cube_game_set_str in cube_game_sets_strs:
            self.sets.append(CubeGameSet(cube_game_set_str))

    def get_power(self) -> int:
        # Get the fewest number of cubes for game.
        max_red = 0
        max_green = 0
        max_blue = 0
        for set in self.sets:
            if set.red > max_red:
                max_red = set.red
            if set.green > max_green:
                max_green = set.green
            if set.blue > max_blue:
                max_blue = set.blue
        return max_red * max_green * max_blue

class CubeGameSet:
    def __init__(self, cube_game_set_str: str):
        self.red = 0
        self.green = 0
        self.blue = 0

        # "1 red, 2 green, 6 blue"
        cubes = cube_game_set_str.split(", ")
        # ["1 red","2 green","6 blue"]
        for cube in cubes:
            if "red" in cube:
                self.red = int(cube.replace(" red", ""))
            elif "green" in cube:
                self.green = int(cube.replace(" green", ""))
            elif "blue" in cube:
                self.blue = int(cube.replace(" blue", ""))

def main():
    power_sums = 0
    cube_games_strs = read_file_into_words("input.txt")
    for cube_game_str in cube_games_strs:
        cube_game = CubeGame(cube_game_str)
        power = cube_game.get_power()
        power_sums += power
    return power_sums

if __name__ == "__main__":
    print(main())
