import random

places_to_vist_US = ["New York City", "Seattle", "Chicago", "Miami"]
places_to_vist_SE_Asia = ["Saigon", "Singapore", "Bali", "Hanoi"]
things_to_do_US = ["City tour", "Try out expensive resturuants", "Go to the casino", "Go to a concert"]
things_to_do_SE_Asia = ["Going on a boat tour", "Going hiking", "doing a Street food tour", "Visiting a religious temple"]
transportation_US = ["Car", "Train", "Plane"]
transportation_SE_Asia = ["Boat", "Plane"]
places_to_stay_US = ["AirBnB", "Hotel", "Motel"]
places_to_stay_SE_Asia = ["Hotel", "Hostel", "AirBnB"]
main_loop = True



country_select = input("Hello, this is your trip advisor. To start things off would you like to travel to SE Asia or the US. ")
while main_loop == True:
    if country_select == "SE Asia":
        for item_SE_0 in places_to_vist_SE_Asia:
            SE_visit_select = input(f"Ok! would you like to visit {item_SE_0} in SE Asia? Yes or No. ")
            if item_SE_0[-1]:
                continue
            if SE_visit_select == "Yes":
                SE_user_location = item_SE_0
                print(f"You will be staying in {item_SE_0}.")
                break
            elif SE_visit_select == "No":
                continue
            else:
                print("Please select Yes or No")
                continue
        for item_SE_1 in things_to_do_SE_Asia:
            SE_activity_select = input(f"Would you like to {item_SE_1}? Yes or No. ")
            if SE_activity_select == "Yes":
                SE_user_activity = item_SE_1
                print(f"You will be {item_SE_1}")
                break
            elif SE_activity_select == "No":
                continue
            else:
                print("Please select Yes or No")
                continue
        for item_SE_2 in transportation_SE_Asia:
            SE_transportation_select = input(f"Would you like travel by {item_SE_2}? Yes or No. ")
            if SE_transportation_select == "Yes":
                SE_user_transportation = item_SE_2
                print(f"You will be travelling by {item_SE_2}")
                break
            elif SE_transportation_select == "No":
                continue
            else:
                print("Please select Yes or No")
                continue
        for item_SE_3 in places_to_stay_SE_Asia:
            SE_accomodation_select = input(f"Would you like to stay at a {item_SE_3}? Yes or No. ")
            if SE_accomodation_select == "Yes":
                SE_user_accomodation = item_SE_3
                print(f"You will be staying in a {item_SE_3}.")
                break
            elif SE_accomodation_select == "No":
                continue
            else:
                print("Please select Yes or No")
                continue
        confirmation = input(f"This is what your trip to SE Asia will look like. You will be visiting {item_SE_0}. You will be travelling by a {item_SE_2}. You will be staying in a {item_SE_3}. And you will be {item_SE_1} for your main activity. Is this trip okay? Yes or No. ")
        if confirmation == "Yes":
            print("We hope you enjoy your trip!")
            main_loop = False
        elif confirmation == "No":
            print("Ok! lets restart this process.")


    
    
        

        
            
        




