from hunt import Hunt
from board import Board



game_repeat = 100000
counts = []
for i in range(0, game_repeat):
    count = 0
    board1 = Board()
    hunt = Hunt(board1)
    while(board1.remaining_targets()!=0):
        rt = board1.remaining_targets()
        #print(rt)
        hunt.move()
        count +=1
    #print("count " +str(count))
    print("---------")
    counts.append(count)
print("PROSEK: " + str(sum(counts)/game_repeat))