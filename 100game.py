# --------------------------  بسم الله الرحمن الرحيم   ---------------------------------

# CS112_A1_T2_1_20230710.py 
# 100 game : Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# NAME : Amro Yassir Alhaj Mohammed
# ID : 20230710

counter = 0
print ("\ncounter is : 0")

while True :
#------------------------------------------------------------------------------------
    print("\n")

    player1 = int(input("player_1 enter your number : "))

    while player1 > 10 or player1 < 1:
        player1 = int(input("hey player_1 please sellect a valid number11 : "))
    while counter + player1 > 100:
        player1 = int(input("hey player_1 please sellect a valid number22 : "))
    counter = counter + player1
    print ("counter is : ",counter)
    if counter == 100 :
        print ("################   player_1 was win   ###################") 
        break   

#------------------------------------------------------------------------------------
    
    print("\n")
    
    player2 = int(input("player_2 enter your number : "))
    while player2 > 10 or player2 < 1:
        player2 = int(input("hey player_2 please sellect a valid number : "))
    while counter + player2 > 100:
        player2 = int(input("hey player_2 please sellect a valid number : "))
    counter = counter + player2
    print ("counter is : ",counter)
    if counter == 100 :
        print ("################   player_2 was win   ###################")
        break