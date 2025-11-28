import  random 
answer = ['ajayteja','akshayteja','ravinder','renuka','bhoodevi','bheem','chutki','dolakhpur']
name= random.choice(answer)
guessedname = ['_']*len(name)
attempts = 10
while attempts>0:
    print('\nCurrent name: ' + ' '.join(guessedname))
    guess = input('Guess a letter: ').lower()
    if guess in name :
        for i in range (len(name)):
            if name[i] == guess:
                guessedname[i] = guess
        print('Great Guess!')
    else:
        attempts-=1
        print('Wrong Guess! Attempts left: ' + str(attempts))
    if '_' not in guessedname:
        print('\n Congo! You guessed right! '+ name)
        break
    if attempts == 0 and '_' in guessedname:
        print('\n You\'ve run out of attempts! The name was: ' + name)
        
    
    
