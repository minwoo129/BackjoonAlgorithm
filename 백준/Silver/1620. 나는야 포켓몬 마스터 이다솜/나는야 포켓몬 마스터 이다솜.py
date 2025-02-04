import sys

n, m = map(int, sys.stdin.readline().split())
pokemonMap = {}
pokeMons = []

for i in range(n):
    pokemon = sys.stdin.readline().rstrip()
    newIdx = i+1
    pokemonMap[pokemon] = newIdx
    pokemonMap[str(newIdx)] = pokemon

for i in range(m):
    pokeMons.append(sys.stdin.readline().rstrip())

for pokeMon in pokeMons:
    print(pokemonMap[pokeMon])
