def main():
    print("You are accused of choosing CIS as your career:/\nYou have a chance to save your life!\nGuess the word in given turns \
    otherwise you will be hanged :D")
    print()
    print('RULES::')
    print('     1)You have 6 turns and 3 warnings')
    print('     2)If you guess a vowel character and it does not match you will lose 2 turns else you will lose 1 turn')
    print('     3)Each time you pass a character other than alphabet or more than one character or the alphabet you already guessed\
    you will recieve a warning message.In case of no warnings left you will loose a turn')
    print('     4)You will lose the game if you run out of the turns')
    print()
    input('Press enter to start the game')
    print()
    f=open('words.txt')
    a=f.read()
    f.close()
    answer_list=a.split( )
    import random
    import string
    random.shuffle(answer_list)
    answer=list(answer_list[0])
    print('The word has',len(answer),'characters')
    display=[]
    display.extend(answer)
    for i in range (len(display)):
        display[i]='_'
    print(' '.join(display))
    print()
    turns=6
    warnings=3
    count=0
    Remaining_Alphabets=list(string.ascii_lowercase)
    while count<len(answer):
        if turns<=6:
            if turns==6:
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |  ____/_\____ ")
                print('          |  | | | | | | ')
            elif turns==5:
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |  ____/_\____ ")
                print('          |  | | | | |   ')
            elif turns==4:
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |  ____/_\____ ")
                print('          |    | | | |   ')
            elif turns==3:
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |  ____/_\____ ")
                print('          |    | | |     ')
            elif turns==2:
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |  ____/_\____ ")
                print('          |      | |     ')
            elif turns==1:
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |  ____/_\____ ")
                print('          |      |       ')
            elif turns==0:
                word=''.join(answer)
                print('You are out of guesses\nYou were unable to guess the word \'',word,'\'\n\nYou lose\n        YOUR LIFE!!!!!\n')
                print(' |   |    /\    |\  |    /\     |--  |\  ')
                print(' | _ |   /_ \   | \ |   /   _   |--  | \ ')
                print(' |   |__/    \__|  \|__/___| |__|--__|_/ ')
                print()
                print('           _______       ')
                print('          |       |      ')
                print('          |       o      ')
                print('          |      -|-     ')
                print("          |      / \     ")
                print('          |              ')
                break
            print()
            print('=====~~~~~=====~~~~~=====~~~~~=====')
        print('Remaining_Alphabets: ',Remaining_Alphabets)
        print()
        print('You have',turns,'turns')
        print('You have',warnings,'warnings')
        print()
        guess=input('Guess a character: ')
        guess=guess.lower()
        if 'A'<=guess<='Z' or 'a'<=guess<='z':
            for i in range(len(answer)):
                if guess==display[i]:
                    break
                elif answer[i]==guess:
                    display[i]=guess
                    count+=1
            if len(guess)>1:
                print('Enter a single character in one turn')
                if warnings>0:
                    warnings-=1
                elif warnings<=0:
                    if turns>0:
                        turns-=1
                        print('You had no warning left so you lost one turn\n')
            if guess not in display and len(guess)==1:
                if guess in 'AEIOUaeiou':
                    print('Oops! Wrong guess...!\nYou missed a vowel!\n')
                    if turns>1:
                        turns-=2
                    elif turns<=1:
                        turns-=1
                else:
                    print('Oops! wrong guess...!\nYou missed a consonent!\n')
                    if turns>0:
                        turns-=1
            if guess not in Remaining_Alphabets and len(guess)==1:
                print('You have already guess that alphabet\nTry another')
                if warnings>0:
                    warnings-=1
                elif warnings<=0:
                    if turns>0:
                        turns-=1
                        print('You had no warning left so you lost one turn\n')
            elif guess in Remaining_Alphabets:
                Remaining_Alphabets.remove(guess)
        else:
            print('Enter a valid alphabet!\n')
            if warnings>0:
                warnings-=1
            elif warnings<=0:
                turns-=1
                print('You had no warning left so you lost one turn\n')
        print(' '.join(display))
        print()
    else:
        print('Congratulations! You guessed the word and saved your life')
        Your_Score=turns*len(''.join(set(answer)))
        print('Your score is: ',Your_Score)
