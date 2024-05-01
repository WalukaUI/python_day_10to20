import random
art="""                                                             
                     .---.                                   
                     |   |               .                   
       _     _       |   |             .'|                   
 /\    \\   //       |   |           .'  |                   
 `\\  //\\ //  __    |   |          <    |            __     
   \`//  \'/.:--.'.  |   |   _    _  |   | ____    .:--.'.   
    \|   |// |   \ | |   |  | '  / | |   | \ .'   / |   \ |  
     '     `" __ | | |   | .' | .' | |   |/  .    `" __ | |  
            .'.''| | |   | /  | /  | |    /\  \    .'.''| |  
           / /   | |_'---'|   `'.  | |   |  \  \  / /   | |_ 
           \ \._,\ '/     '   .'|  '/'    \  \  \ \ \._,\ '/ 
            `--'  `"       `-'  `--''------'  '---'`--'  `"  """
correct=False
won=False
count=0
again=True
while again == True:
    number=random.randrange(1,100)
    print(art)
    print("welcome to the game")
    while correct == False:
        dificulty=input("choose dificulty 'easy' or 'hard' ? ")
        if dificulty == "hard":
            count=5
            correct=True
        elif dificulty == "easy":
            count=10
            correct=True
        else:
            print("please try again")
    correct = False
    while count != 0:
        guessed_number=int(input(f"Please guess a number, you have {count} chances : ")) 
        if guessed_number < number:
            print("too small")
            count -= 1
        elif guessed_number > number:
            print("too big")
            count -= 1
        else:
            won=True
            count=0
    if won == True:
        print("You *****won**** the game, congratulations......")
        print(f"correct number is {number}")
        won=False
    else:
        print("You lost the game")
        print(f"correct number is {number}")
        count=0
    answer=input("Would you like to play again, Please type 'yes' or 'no'? ")
    if answer == "no":
        again=False