#!/usr/bin/env python3

# initialize counter for while loop and the answer variable
round = 0
answer = " "

# loop goes forever until condition met or break used
while round < 3 and answer.lower() != "brian":
    round += 1   # increment round, game ends at round 3
    # asking the question and taking input from user for answer
    answer = input('Finish the movie title, "Monty Python\'s The Life of __________": ')
    # Begin if loop to check answer
    if answer.lower() == 'brian':
        print('Correct!')   # Correct answer given now break from the loop
    elif round == 3:
        print('Sorry, the correct answer was Brian')    # Loop is also broken when 3 rounds have gone by
    else:
        print('Sorry, try again.') # Back to beginning of the while loop
