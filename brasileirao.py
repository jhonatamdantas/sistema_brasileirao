# Bibliotecas utilizadas
from rich import print
from rich.panel import Panel
from time import sleep
import random
from generateGames import generate_games
import os

# Times do Brasileirão 2026
teams_brazil = (
    "Athletico-PR", "Atlético-MG", "Bahia", "Botafogo", 
    "Chapecoense", "Corinthians", "Coritiba", "Cruzeiro", 
    "Flamengo", "Fluminense", "Grêmio", "Internacional", 
    "Mirassol", "Palmeiras", "Red Bull Bragantino", 
    "Remo", "Santos", "São Paulo", "Vasco", "Vitória"
)

# Controle para o número de rodadas
GAMES = 1

# Sorteio dos times para a tabela de classificação
TEAMS_SORTED = random.sample(teams_brazil, 10)

# Tabela dos times em MATRIZ
TABLE_TEAMS = [
    ["Team", "MP", "W", "D", "L", "PTS"],
    [TEAMS_SORTED[0], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[1], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[2], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[3], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[4], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[5], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[6], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[7], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[8], 0, 0, 0, 0, 0],
    [TEAMS_SORTED[9], 0, 0, 0, 0, 0],
]

# Gera os jogos do campeonato (função importada do arquivo generateGames.py)
generated_rounds = generate_games(TEAMS_SORTED)

# Aqui pode ajustar o número de rodadas que deseja simular (atualmente definido para 10 rodadas)
while GAMES < 10:
    sleep(1)
    # Exibe a rodada atual e a tabela de classificação
    print(Panel(f"[bold yellow]Rodada {GAMES}[/bold yellow]", expand=True))
    print(Panel(f"[bold green]Tabela de Classificação[/bold green]", expand=False))

    # Exibe a tabela de classificação
    for row in TABLE_TEAMS:
        sleep(1)
        print(Panel(f"{row[0]:<15} {row[1]:>10} {row[2]:>3} {row[3]:>3} {row[4]:>3} {row[5]:>3}", expand=False))

    # Exibe os jogos da rodada e os resultados
    print(Panel("[bold blue]Jogos da Rodada:[/bold blue]", expand=False))
    for game in generated_rounds[GAMES - 1]:
        sleep(1)
        print(Panel(f"[bold blue]{game[0]} X {game[1]}[/bold blue]", expand=False))
    
    # Simula os resultados dos jogos e atualiza a tabela de classificação
    print(Panel("[bold blue]Resultado da Rodada:[/bold blue]", expand=False))
    for game in generated_rounds[GAMES - 1]:
        sleep(1)
        # Simula o resultado do jogo com placares aleatórios entre 0 e 5
        score1, score2 = random.randint(0, 5), random.randint(0, 5)
        print(Panel(f"[bold blue]{game[0]} {score1} X {score2} {game[1]}[/bold blue]", expand=False))

        # Atualiza a tabela de classificação com base no resultado do jogo
        classification = TABLE_TEAMS[1:]  # -> Exclui o cabeçalho da tabela
        if score1 > score2:
            # Atualiza a tabela para o time vencedor
            for team_row in classification:  # Exclui o cabeçalho da tabela
                if team_row[0] == game[0]:
                    team_row[1] += 1  # Incrementa MP (Matches Played)
                    team_row[-1] += 3  # Incrementa PTS (Points)
                    team_row[2] += 1  # Incrementa W (Wins)
                elif team_row[0] == game[1]:
                    team_row[1] += 1  # Incrementa MP (Matches Played)
                    team_row[4] += 1  # Incrementa L (Losses)
        elif score2 > score1:
            # Atualiza a tabela para o time vencedor
            for team_row in classification:  # Exclui o cabeçalho da tabela
                if team_row[0] == game[1]:
                    team_row[1] += 1  # Incrementa MP (Matches Played)
                    team_row[-1] += 3  # Incrementa PTS (Points)
                    team_row[2] += 1  # Incrementa W (Wins)
                elif team_row[0] == game[0]:
                    team_row[1] += 1  # Incrementa MP (Matches Played)
                    team_row[4] += 1  # Incrementa L (Losses)
        else:
            # Atualiza a tabela para empate
            for team_row in classification:  # Exclui o cabeçalho da tabela
                if team_row[0] == game[0] or team_row[0] == game[1]:
                    team_row[1] += 1  # Incrementa MP (Matches Played)
                    team_row[-1] += 1  # Incrementa PTS (Points)
                    team_row[3] += 1  # Incrementa D (Draws)

    # Atualiza a tabela de classificação e exibe o fim da rodada
    GAMES += 1
    # Exibe o fim da rodada e ordena a tabela de classificação por pontos
    print(Panel(f"[bold yellow]Fim da Rodada {GAMES - 1}[/bold yellow]", expand=False))
    # Lambda para ordenar a tabela de classificação por pontos (última coluna)
    TABLE_TEAMS[1:] = sorted(classification, key=lambda x: x[-1], reverse=True)  # Ordena a tabela por pontos
    sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para a próxima rodada