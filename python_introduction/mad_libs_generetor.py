
def mad_libs_generator() :
    print("\nPlease provide the words asked below\n")

    weather_adjective = input("Enter a weather of your choice (e.g. cloudy, sunny, rainy, stormy, etc...) : ")
    monkey_adjective = input("Enter a monkey color of you choice(e.g. brown, white, black, ...) : ")
    lion_adjective = input("Desccribe the lions mood by one word :")
    animal = input("Enter an animal that you like : ")
    feeling = input("Enter a feeling of your choice(e.g. fear, anger, excited, happy, etc...) : ")


    if feeling.lower() == "fear" :
        twist = "It was an experience that truly froze me with fear!"
    elif feeling.lower() == "exited" :
        twist = "I really can't wait to relive the same experience, i loved the scene so much!"
    elif feeling.lower() == "anger" :
        twist = "I was so furious at what happened, i’d never want to relive that scene again!"
    else :
        twist = f"What a wild and { feeling } experience!"


    print("\nYour story is right down here!\n")

    story = f"""On a beautiful { weather_adjective } day, I went to the zoo. \nI saw a funny { monkey_adjective } monkey swinging from the trees. Then, \nI spotted a majestic { lion_adjective } lion lounging in the sun. 
    \nSuddenly, one { animal } emerged from the greenery."""

    
    print(story)
    print(twist)

mad_libs_generator()