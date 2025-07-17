

current_weather = input("What's the weather like today?(e.g. sunny, rainy, cold) :")

if current_weather == "sunny" :
    today_clothes = "a t-shirt and sunglasses."
    print(f"The weather is {current_weather} you should wear {today_clothes}")
elif current_weather == "rainy" :
    today_clothes = "umbrella and a raincoat."
    print(f"Don't forget your {today_clothes}")
elif current_weather == "cold" :
    today_clothes = "heavy coats and a thermal underwear"
    print(f"The weather is {current_weather} i should wear {today_clothes}")
else:
    print("Sorry, I don't have recommendations for this weather.")
