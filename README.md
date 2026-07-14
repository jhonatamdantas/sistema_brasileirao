# Simulador de Jogos do Brasileirão 2026 ⚽ 

<p>Este programa simula jogos do Campeonato Brasileiro de Futebol (Brasileirão) de 2026, gerando resultados aleatórios para cada partida e atualizando a tabela de classificação com base nos resultados obtidos.</p>

## Informações do Programa
<li><p>O código utiliza a biblioteca <code>rich</code> para exibir informações de forma estilizada no terminal, caso não tenha, instale-a com <code>pip install rich</code>.</p></li>
<li><p>O programa simula 10 rodadas (você pode ajustar esse número no loop while) do campeonato, atualizando a tabela de classificação a cada rodada, isso está comentado no código.</p></li>
<li><p>Os resultados dos jogos são gerados aleatoriamente, com placares entre 0 e 5.</p></li>
<li><p>A tabela de classificação é atualizada com base nos resultados dos jogos, considerando vitórias, empates e derrotas.</p></li>
<li><p>A quantidade de times sorteados podem ser ajustadas na variável <code>TEAMS_SORTED</code>.</p></li>


### Informação Extra
Os jogos não possuem ida e volta, ou seja, cada time joga apenas uma vez contra cada adversário.