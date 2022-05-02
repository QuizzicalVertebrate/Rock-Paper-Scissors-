#IDEAS map their pattern instead of mine and see what happens 
#I must have been wrong about who goes first. Why does index plus2 get the right result and not index plus one 
#if their list starts off with a seed of something and they play first. Than to ge ther reponses to my play i need 
#to be two ahead of them


import random 
#created a record of my own previous guesses as a arg in the function. The new info is that you can keep 
#info in the function over time by using some type of a data structure as a fucntion argument and adding to 
#it. Usually the function is created anew each time it is called. Created a function to reverse whatever I 
#think will be played to beat that move. The better way is to map the data as a dict. I didn't chap that. 
def player(prev_play, opponent_history=[],prev_guess = []):
    opponent_history.append(prev_play)
    def winner(x):
        y = "R"
        if x == "R":
            y = "P"
        if x == "P":
            y = "S"
        if x == "S":
            y = 'R'
        return y
#wrapped in a try/except block cuz there wont be the right data for a while. Easier than making a contingency 
    try: 
#creates a list of the indexes(numeric) in my history where I played the same play that I played last time

        indexes_last_play = [index for (index, item) in enumerate(prev_guess) if item == prev_guess[-1]]
#because that list of indexes will grab my last play as well and its hard to grab the second to last index of 
#something create a seperate var grabbing the second to last var in that list which will be the prev instance 
        prev_play = indexes_last_play[-2]
#grab that index plus one from the opponents history which will be how they responded to that play = my prediction
        opp_next_play = opponent_history[prev_play +2]
#reverse the predicted play, to win 
        guess = winner(opp_next_play)
        prev_guess.append(guess)
    
    except:
        guess = random.choice(["R", "P", "S"])
        prev_guess.append(guess)
        print("exception")
   
            
    return guess




