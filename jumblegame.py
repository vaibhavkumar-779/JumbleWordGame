import random

#Step 1 create A library of words for game
def choose():
    words=['century','republic','breaking','rainbow','computer','science','boating','badminton','programming','condition','amplifier','soldier','mathematics','medium','calender','player']
    pick=random.choice(words)
    return pick

# Step 2 function to jumble the letters
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

#Step 3 function to give ending lines of game
def thank(p1n,p2n,p1,p2):
    print(p1n.upper(),' Your score is:',p1)
    print(p2n.upper(),' Your score is:',p2)
    print('Thanks for playing\n')
    print('It was a nice game, bye!')

#Step 4 Defining the game
def play():
    player1=input('player 1, please enter your name\t\n')
    player2=input('player 2, please enter your name\t\n')
    pp1=0
    pp2=0
    turn=0
    while (1):
        #computer's task
        picked_word=str(choose())
        #create question
        ques=jumble(picked_word)
        print ('word is:',ques,)
        # player1
        if turn%2==0:
            print(player1,'  Your Turn')
            ans=input('What is the word\t\n\n')
            if ans==picked_word:                 #comparing the words
                pp1=pp1+1
                print('correct -updated score:',pp1)
            else:
                print('you missed! the word was :',picked_word)
        # player 2
        else:
            print(player2,'  Your Turn')
            ans=input('What is the word\t\n\n')
            if ans==picked_word:               #comparing the words
                pp2=pp2+1
                print('updated score is: ',pp2)
            else:
                print('You missed it!,be right next time\n')
                print('the word is  ',picked_word)
        turn=turn+1
        c=input('Press 1 to continue or 0 to end the game\n')
        if c=='0':
            thank(player1,player2,pp1,pp2)
            break

play()
