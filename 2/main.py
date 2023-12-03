from typing import Dict
from numpy import prod


class GameConfig:
    FILENAME = "input.txt"
    BAG = {"blue": 14, "red": 12, "green": 13}


class GameDataLoader:
    def __init__(self, filename: str):
        self.filename = filename

    def load_data(self) -> Dict[int, Dict[str, int]]:
        games = {}
        with open(self.filename) as file:
            input_data = file.readlines()

        for game_data in input_data:
            game_info = game_data.split(":")
            game_number = int(game_info[0].split()[1])
            color_counts = {"blue": 0, "red": 0, "green": 0}

            for turn in game_info[1].split(";"):
                for color_count in turn.split(","):
                    count, color = color_count.split()
                    count = int(count)
                    color_counts[color] = max(color_counts[color], count)

            games[game_number] = color_counts

        return games


class GameCalculator:
    def __init__(self, games: Dict[int, Dict[str, int]], bag: Dict[str, int]):
        self.games = games
        self.bag = bag

    def is_game_possible(self, cubes: Dict[str, int]) -> bool:
        return all(cubes[color] <= self.bag[color] for color in self.bag)

    def sum_possible_games(self) -> int:
        return sum(game_number for game_number, cubes in self.games.items() if self.is_game_possible(cubes))

    def power_cubes(self) -> int:
        return sum(prod(list(game_colors.values())) for game_colors in self.games.values())


if __name__ == '__main__':
    games_loader = GameDataLoader(GameConfig.FILENAME)
    games_data = games_loader.load_data()
    calculator = GameCalculator(games_data, GameConfig.BAG)

    result_part_1 = calculator.sum_possible_games()
    result_part_2 = calculator.power_cubes()
    print(result_part_1)
    print(result_part_2)
