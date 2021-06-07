import random
import playsound

print("\n *** Welcome to snake water and gun game ***\n")
print("You have to choose number of chances, how many you want to play")
print("Scoring will be done accordingly and lastly all the best for your game \n")
your_points = 0
Computer_points = 0
n = int(input("Enter number of chances you want to play : "))
for i in range(0, n):
    lst = ["snake", "water", "gun"]
    com = random.choice(lst)
    a = input("Enter snake(s), water(w) or gun(g) :")
    a = a.lower()
    if a == "s":
        if com == "snake":
            print("Computer has also chosen,", com)
            print("Nobody gets points, this round tied\n")
        elif com == "gun":
            your_points = your_points
            Computer_points = Computer_points + 1
            print("Computer chosen, ", com)
            print("you have now", your_points, "points")
            print("Computer has", Computer_points, "points\n")
            playsound.playsound("rong.wav")
        else:
            Computer_points = Computer_points
            your_points = your_points + 1
            print("Computer chosen, ", com)
            print("You have now,", your_points, "points")
            print("Computer has,", Computer_points, "points\n")
            playsound.playsound("right.wav")
    elif a == "w":
        if com == "water":
            print("Computer has also chosen,", com)
            print("Nobody gets points, this round tied\n")
        elif com == "gun":
            your_points = your_points + 1
            Computer_points = Computer_points
            print("Computer chosen, ", com)
            print("you have now", your_points, "points")
            print("Computer has", Computer_points, "points\n")
            playsound.playsound("right.wav")
        else:
            your_points = your_points
            Computer_points = Computer_points + 1
            print("Computer chosen, ", com)
            print("You have now,", your_points, "points")
            print("Computer has,", Computer_points, "points")
            playsound.playsound("rong.wav")
    elif a == "g":
        if com == "gun":
            print("Computer has also chosen,", com)
            print("Nobody gets points, this round tied\n")
        elif com == "water":
            your_points = your_points
            Computer_points = Computer_points + 1
            print("Computer chosen, ", com)
            print("you have now", your_points, "points")
            print("Computer has", Computer_points, "points")
            playsound.playsound("rong.wav")
        else:
            your_points = your_points + 1
            Computer_points = Computer_points
            print("Computer chosen, ", com)
            print("You have now,", your_points, "points")
            print("Computer has,", Computer_points, "points")
            playsound.playsound("right.wav")
    else:
        print("Please enter some valid character")

if your_points > Computer_points:
    print("Congo! you are the winner, party hard\n")
    print("You won the game by", your_points - Computer_points, "points\n")
    playsound.playsound("game_win.wav")
elif Computer_points > your_points:
    print("You lose, try try don't cry\n")
    print("You lose the game by", Computer_points - your_points, "points\n")
    playsound.playsound("game_over.wav")
else:
    print("Game was very exciting but tied\n")
    playsound.playsound("full_tie.wav")

print("****    Thanks for playing this game     *****")
