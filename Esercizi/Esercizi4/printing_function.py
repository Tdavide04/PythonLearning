def printing(manufacturer, model, color, seats):
    profile = {"manufacturer" : manufacturer,
               "model" : model,
               "color" : color,
               "seats" : seats
               }
    
    print(f"your car's profile is: {profile}")
    return profile
