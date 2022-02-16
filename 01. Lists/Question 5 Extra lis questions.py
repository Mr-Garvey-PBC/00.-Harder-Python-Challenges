# Program name: Top game score.py
# Program accepts user ID, and checks if it is in the list of players
# If not, it is appended to the list, with a score of 0.
# User plays the game and is assigned a random score between 50 and 200
# Program checks if it is greater than the score held.
# If so, it replaces it.
# The user ID and score is then printed out.

import random
# 2 Dimensional list is a group of lists within a list
player_info = [["AAA01",135],
          ["BBB01",87],
          ["CCC01",188],
          ["DDD01",109]] # a

random_val=random.randint(50,201)
print(f'Random number is {random_val}')
list_length=len(player_info)
found=False

user_id=str(input('Enter user ID or enter xxx to end: '))


while user_id!='xxx':
    
    for i in range(list_length):
        if user_id in player_info[i]:
            print(f'Player name is in the list at position {i}')
            found=True
    
            for i in range(list_length):
                if user_id in player_info[i]:
        
                     if player_info[i][1] < random_val:
                        player_info[i][1]=random_val
    
    if found!=True:
        print('User not found but has been added to the list')
        player_info.append([user_id,0])


    user_id=str(input('Enter another user ID: '))

print(player_info)
print('End of program')

# C
# for i in range(list_length):
#     if user_id in player_info[i]:
#         
#         if player_info[i][1] < random_val:
#             player_info[i][1]=random_val
# 
# b
# for i in range(list_length):
#     if user_id in player_info[i]:
#         print('Player name is in the list')
#         print(f'{i}')
#         found=True
# 
# if found!=True:
#     print('User not found')
#     player_info.append([user_id,0])
# 

        
    
            
            
            
            
            
            
            
            
            