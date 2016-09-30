import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    }

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }

def order():
    print 'Answer the five questions with a "y" or "n"'
    preferences = {}
    for key, value in questions.items():
        answer = raw_input(value)
        if answer.lower() in ["y", "yes"]:
            preferences[key] = True
        else:
            preferences[key] = False
    return preferences
    
    

def bev(preferences):
        drink = []
        for ingredient_type, liked in preferences.items():
            if liked:
                drink.append(random.choice(ingredients[ingredient_type]))
        return drink
        
def drink_name():
    adjectives = ['sweet', 'fluffy', 'tart']
    nouns = ['dog', 'barrel', 'punch']
    drink_adjective = random.choice(adjectives)
    drink_noun = random.choice(nouns)
    name = drink_adjective + ' ' + drink_noun
    return name 
        
def main():
    while True:
        preferences = order()
        drink = bev(preferences)
        print drink
        print drink_name()
        another_drink = raw_input('Would you like another drink? ')
        if another_drink != 'y':
            break
        
        
if __name__ == '__main__':
    main()

    