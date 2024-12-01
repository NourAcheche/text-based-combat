import random# in order for the module random to work

x = input(" please type the first hero's name")#in this line the user have to give a real name not a space
while x == "":
    x = input(" please type the first hero's name")
y = input(" please type the second hero's name")# for the second name it has to be different than the first name and i added the condition of sâce in case their is repitition
while (x == y) or (y == ""):
    y = input(f"{x} is taken please choose another name ")


def coin_toss(x, y):#from this fuction we will determine who is the first player by random
    first_attacker = random.choice([x, y])#it will choose between two things either player1 or player2
    if first_attacker == x:#if the chosen  attacker is the first hero then the second hero is the second player
        second_attacker = y
    else:
        second_attacker = x#if the chosen attacker is the second hero then the first hero is the other player
    return first_attacker, second_attacker




def bars(health):#we make a for loop to repeat the stick as much as the health value
    for i in range(health):
        print("I", end="")



def attack(M,health,max,player_name):# a function which determines the value of the attack 
    success_rate=(100-M)
    if random.randint(1,100)<=success_rate:
        max=max-M
        health=health-(M//2)# the value of sticks is half of the health points so whataver hits the oponent will make it shoul be devide by half to decrease the number of sticks
        print("attack successful", {player_name}, "hits", M, "damages")
        return health,max
    else:
        print("opps ",player_name,"missed the attack")#if it 's not sucessful then it should print this value and keep the value of sticks and health points as it is
        return health,max

def result(max1, max2):#this function will determine who the winner
    if max1 <= 0:#if the health points of player one is equal to 0 then the other player is the winner
        print(sep="\n      ")
        print("####################################################################################", f"{player2}",
              " is the winner",
              "#############################################################################################")
    elif max2 <= 0:#if the health points of player two is equal to 0 then the player 1 is the winner
        print(sep="\n      ")
        print("####################################################################################", f"{player1}",
              " is the winner",
              "#############################################################################################")

player1, player2 = coin_toss(x, y)#this function will chose who starts first from player 1 and player 2
def comba():
  
  print(f"{player1} starts first")#and here we determine who start first using the coin_toss function
  print(f"{player1}", "  " * 29, f"{player2}")#the placement of the names
  max=100
  health=50
  Ip = "HP"
  print(Ip, end="")#we add the end="" to add the next line to this line
  print(f"{[max]}", end="")#print both players health points at a maximum value
  bars(health)
  print("         ", f"{Ip}{[max]}", end="")
  bars(health)
  print(sep="\n      ")
  max1=100
  max2=100
  health1=50
  health2=50
  while ((max1 > 0) or (max2 > 0)):#while both of the player still have health points
    print(sep="\n      ")
    print("————— ", player1, "attack —————")
    M = int(input("choose your attack magnitude between 1 and 50 "))
    while not (1 <= M <= 50):#unless they give a magnitude between 1 and 50 it will keep sending this message
        M = int(input("choose your attack magnitude between 1 and 50 "))
    health2,max2=attack(M, health2, max2 , player1)
    if max2 > 0:#if the second player is still alive print his health points
        print(f"{player1}", "  " * 20, f"{player2}")
        print(f"{Ip}{[max1]}", end="")
        bars(health1)
        print("         ", f"{Ip}{[max2]}", end="")
        bars(health2)
    elif max2 <= 0:#if he is dead then print his health points and determine the winner from the def result
        max2=0
        print(f"{player1}", "  " * 20, f"{player2}")
        print(f"{Ip}{[max1]}", end="")
        bars(health1)
        print("         ", f"{Ip}{[max2]}", end="")
        bars(health2)
        break#show both of the player health points at the end
    ### 2nd round
    print(sep="\n      ")
    print("————— ", player2, "attack —————")
    M = int(input("choose your attack magnitude between 1 and 50 "))#we repeat this condition for both players
    while not (1 <= M <= 50):
        M = int(input("choose your attack magnitude between 1 and 50 "))

    health1, max1 = attack(M, health1, max1 , player2)
    if max1 > 0:#if the first player is still alive print his health points and the other player and continue the attack
        print(f"{player1}", "  " * 20, f"{player2}")
        print(f"{Ip}{[max1]}", end="")
        bars(health1)
        print("         ", f"{Ip}{[max2]}", end="")
        bars(health2)
    if max1 <= 0:#then one of the first loses and it will print who's the winner by the result function
        max1=0
        print(f"{player1}", "  " * 20, f"{player2}")
        print(f"{Ip}{[max1]}", end="")
        bars(health1)
        print("         ", f"{Ip}{[max2]}", end="")
        bars(health2)
        break#show both of the player health points at the end of this round
  result(max1, max2)##show who is the winner the end of this round

comba()
def play():
    play=input("do you want another round (yes or no)")
    if play=="no":
            print("thanks for playing ! see you again!")
    elif play=="yes":#this function is to repeat the game again if the user says yes
        player1, player2 = coin_toss(x, y)
        comba()#it will repeat the game from the battle stage
    else:#if he picked something diffrent from yes or no he gets the message again
        print("do you want another round (yes or no)")
play()