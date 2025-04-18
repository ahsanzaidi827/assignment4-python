

def mad_lib():

    name = input("Give a name: ")
    place = input("Give me a place: ")
    funny_adjective = input("Give me a funny adjective: ")
    random_object = input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action verb: ")

    story = f'''
    Once upon a time there was a person {name} who lived in {place}.
    One day, they found a {funny_adjective} {random_object} that belonged to a {animal}.
    The {animal} was very upset and started to {action_verb} around.
    {name} could not help but laugh and shouted. '''

    print(story)

if __name__ == "__main__":
    mad_lib()




    


