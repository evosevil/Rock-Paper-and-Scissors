import random, math

human_choice = input("Choose any one- 0.Rock 1.Paper 2.Scissors: ")
human_choice= int(human_choice)
def computer_choice():
    return math.floor(random.random() * 3 )
    #return random.random() + 1

Dict = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}
x= computer_choice()
human = Dict[human_choice]
bot = Dict[x]


print("You: " + human )
print("Computer: " + bot)
if human=="Rock" and bot=="Paper":
    print("You Lose!")
elif human=="Paper" and bot =="Scissors":
    print("You Lose!")
elif human=="Scissors" and bot == "Rock":
    print("You Lose!")
elif human=="Rock" and bot == "Rock":
    print("Tied!")
elif human=="Paper" and bot == "Paper":
    print("Tied!")
elif human=="Scissors" and bot == "Scissors":
    print("Tied!")
elif human=="Rock" and bot == "Scissors":
    print("You Won!")
elif human=="Paper" and bot == "Rock":
    print("You Won!")
elif human=="Scissors" and bot == "Paper":
    print("You Won!")
else:
    print("Invalid Choice!")
