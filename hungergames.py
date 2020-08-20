import random


players = input("Digite o numero de jogadores: ")

randomlist = random.sample(range(100), int(players))

print('os jogadores sao: \n' + str(randomlist))

for i in range(int(players)):
    if(len(randomlist) == 1):
        print(str(randomlist[0]) + ' is the winner')
        break;
    randomlist.sort()
    j = randomlist.pop()
    print(str(j) + ' foi eliminado')
