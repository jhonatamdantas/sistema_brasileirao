from rich import print
from rich.panel import Panel
from time import sleep
import random

def generate_games(teams):
    teams = teams[:]
    random.shuffle(teams)

    n = len(teams)
    rounds = []

    for _ in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            round_matches.append((teams[i], teams[n - 1 - i]))
        rounds.append(round_matches)
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]
    return rounds
