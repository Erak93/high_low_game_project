import art
from game_data import data
import random
# 1) I need to create a variable where I can store the score and add in case of correct answer

# 2)I need to find a way to pick always a new random person from the data to compare with the current person
# 3)I could create a variable current person which will hold the person being the right guess as dictionary

# 4)GAME OVER. The game is over when you miss a guess


#1)
current_score=0
people_already_used=[]

def pick_a_person():
    random_person=random.choice(data)
    if random_person not in people_already_used:
        people_already_used.append(random_person)
        return random_person
    else:
        pick_a_person()

person_1=pick_a_person()
person_2=pick_a_person()


print(person_1)
print(person_2)



def compare_follower():
    person_1_followers=int(person_1["follower_count"])
    person_2_followers=int(person_2["follower_count"])
    
    if person_1_followers>person_2_followers:
        person_with_more_followers=person_1
    else:
        highest_followers_count=person_2_followers
        person_with_more_followers=person_2
    return person_with_more_followers



    

def make_your_guess():
    print(f'Compare A: {person_1["name"]}, {person_1["description"]} from {person_1["country"]}')
    print(art.vs)
    print(f'Against B: {person_2["name"]}, {person_2["description"]} from {person_2["country"]}')
    print()
    player_choice=input("Who do you think has more followers? A or B?")
    if player_choice=='A':
        player_choice=person_1
    elif player_choice=='B':
        player_choice=person_2
    return player_choice



game_is_not_over=True

def calculate_results():
    if make_your_guess()==compare_follower():
        print("you guessed right")
        current_score=+1
        return "new round"
        
    else:
        print("game over")
        return "game over"
        game_is_not_over=False

calculate_results()

print(current_score)

print(person_1)
print(person_2)

while game_is_not_over==True:

    person_1=compare_follower()
    person_2=pick_a_person()

    compare_follower()
    make_your_guess()
    if calculate_results()=="game over":
        game_is_not_over=False