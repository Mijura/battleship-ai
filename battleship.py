from hunt import Hunt
from board import Board
from qagent import Qagent



game_repeat = 100
counts = []
for i in range(0, game_repeat):
    count = 0
    board1 = Board()
    player = Qagent(board1)
    while(board1.remaining_targets()!=0):
        rt = board1.remaining_targets()
        #print(rt)
        player.move()
        count +=1
    #print("count " +str(count))
    print("---------")
    counts.append(count)
print("PROSEK: " + str(sum(counts)/game_repeat))