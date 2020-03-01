from hunt import Hunt
from board import Board
from qagent import Qagent
import csv


with open('results1.csv', 'w', newline='') as csvfile:
    fieldnames = ['games', 'learning_rate', 'discount', 'average_moves']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

game_repeat = 1000

learning_rate = 0
step = 0.02
while(learning_rate<1.1):
    discount = 0
    while(discount<1.1):
        counts = [] 
        for i in range(0, game_repeat):
            count = 0
            board1 = Board()
            player = Qagent(board1, learning_rate, discount)
            while(board1.remaining_targets()!=0):
                rt = board1.remaining_targets()
                player.move()
                count +=1
            print("---------")
            counts.append(count)
        with open('results.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'games': game_repeat, 
                'learning_rate': round(learning_rate, 2), 
                'discount': round(discount, 2), 
                'average_moves': str(round(sum(counts)/game_repeat, 2))})
        discount += step
    learning_rate += step
            
#print("PROSEK: " + str(sum(counts)/game_repeat))
