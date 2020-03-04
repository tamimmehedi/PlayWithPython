def weather_condition(temparature):
    if temparature > 7 :
        return 80
    else:
        return 70

user_input = float(input("Enter temparature: "))
print(weather_condition(user_input))
