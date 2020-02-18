from hunt import Hunt
from board import Board

board1 = Board()
hunt = Hunt(board1)
count = 0
while(board1.remaining_targets()!=0):
    hunt.move()
    rt = board1.remaining_targets()
    count +=1
    print(rt)
print(count)