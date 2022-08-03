import random

places_to_vist_US = ["New York City", "Seattle", "Chicago", "Miami"]
places_to_vist_SE_Asia = ["Saigon", "Singapore", "Bali", "Hanoi"]
things_to_do_US = ["doing a City tour", "trying out expensive resturuants", "going to the casino", "going to a concert"]
things_to_do_SE_Asia = ["going on a boat tour", "going hiking", "doing a Street food tour", "visiting a religious temple"]
transportation_US = ["car", "train", "plane"]
transportation_SE_Asia = ["boat", "plane"]
places_to_stay_US = ["airBnB", "hotel", "motel"]
places_to_stay_SE_Asia = ["hotel", "hostel", "airBnB"]
main_loop = True

def random_list_selector(list):
    selected_item = random.choice(list)
    return selected_item

#Old Code without function or random properties
    # country_select = input("Hello, this is your trip advisor. To start things off would you like to travel to SE Asia or the US. ")
    # while main_loop == True:
    #     if country_select == "SE Asia":
    #         for item_SE_0 in places_to_vist_SE_Asia:
    #             SE_visit_select = input(f"Ok! would you like to visit {item_SE_0} in SE Asia? Yes or No. ")
    #             if item_SE_0[-1]:
    #                 continue
    #             if SE_visit_select == "Yes":
    #                 SE_user_location = item_SE_0
    #                 print(f"You will be staying in {item_SE_0}.")
    #                 break
    #             elif SE_visit_select == "No":
    #                 continue
    #             else:
    #                 print("Please select Yes or No")
    #                 continue
    #         for item_SE_1 in things_to_do_SE_Asia:
    #             SE_activity_select = input(f"Would you like to {item_SE_1}? Yes or No. ")
    #             if SE_activity_select == "Yes":
    #                 SE_user_activity = item_SE_1
    #                 print(f"You will be {item_SE_1}")
    #                 break
    #             elif SE_activity_select == "No":
    #                 continue
    #             else:
    #                 print("Please select Yes or No")
    #                 continue
    #         for item_SE_2 in transportation_SE_Asia:
    #             SE_transportation_select = input(f"Would you like travel by {item_SE_2}? Yes or No. ")
    #             if SE_transportation_select == "Yes":
    #                 SE_user_transportation = item_SE_2
    #                 print(f"You will be travelling by {item_SE_2}")
    #                 break
    #             elif SE_transportation_select == "No":
    #                 continue
    #             else:
    #                 print("Please select Yes or No")
    #                 continue
    #         for item_SE_3 in places_to_stay_SE_Asia:
    #             SE_accomodation_select = input(f"Would you like to stay at a {item_SE_3}? Yes or No. ")
    #             if SE_accomodation_select == "Yes":
    #                 SE_user_accomodation = item_SE_3
    #                 print(f"You will be staying in a {item_SE_3}.")
    #                 break
    #             elif SE_accomodation_select == "No":
    #                 continue
    #             else:
    #                 print("Please select Yes or No")
    #                 continue
    #         confirmation = input(f"This is what your trip to SE Asia will look like. You will be visiting {item_SE_0}. You will be travelling by a {item_SE_2}. You will be staying in a {item_SE_3}. And you will be {item_SE_1} for your main activity. Is this trip okay? Yes or No. ")
    #         if confirmation == "Yes":
    #             print("We hope you enjoy your trip!")
    #             main_loop = False
    #         elif confirmation == "No":
    #             print("Ok! lets restart this process.")
while main_loop == True:
    country_select = input("Hello, this is your trip advisor. To start things off would you like to travel to SE Asia or the US. ")
    if country_select == "SE Asia":
        SE_visit = True
        while SE_visit == True:
            SE_visit_random = random_list_selector(places_to_vist_SE_Asia)
            SE_visit_user_select = input(f"Ok! Would you like to visit {SE_visit_random}? Yes or No. ")
            if SE_visit_user_select == "Yes":
                print(f"You will be visiting {SE_visit_random}")
                SE_visit = False
            elif SE_visit_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        SE_activity = True
        while SE_activity == True:
            SE_activity_random = random_list_selector(things_to_do_SE_Asia)
            SE_activity_user_select = input(f"Ok! Does {SE_activity_random} sound good for your main activity? Yes or No. ")
            if SE_activity_user_select == "Yes":
                print(f"You will be {SE_activity_random}")
                SE_activity = False
            elif SE_activity_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        SE_transportation = True
        while SE_transportation == True:
            SE_transportation_random = random_list_selector(transportation_SE_Asia)
            SE_transportation_user_select = input(f"Ok! Does travelling by {SE_transportation_random} sound good? Yes or No. ")
            if SE_transportation_user_select == "Yes":
                print(f"You will be travelling by {SE_transportation_random}.")
                SE_transportation = False
            elif SE_transportation_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        SE_accomodation = True
        while SE_accomodation == True:
            SE_accomodation_random = random_list_selector(places_to_stay_SE_Asia)
            SE_accomodation_user_select = input(f"Ok! Do you want to stay in a {SE_accomodation_random}? Yes or No. ")
            if SE_accomodation_user_select == "Yes":
                print(f"You will be staying in a {SE_accomodation_random}.")
                SE_accomodation = False
            elif SE_accomodation_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        confirmation = input(f"Ok! You will travel to {SE_visit_random}. You will be travelling by {SE_transportation_random}. You will be staying in a {SE_accomodation_random}. And you will be {SE_activity_random} for your main activity. Does this sound good? Yes or No. ")
        if confirmation == "No":
            print("Ok! Lets try again.")
            continue
        elif confirmation == "Yes":
            print("Ok! Enjoy your trip.")
            main_loop == False
    elif country_select == "US":
        US_visit = True
        while US_visit == True:
            US_visit_random = random_list_selector(places_to_vist_US)
            US_visit_user_select = input(f"Ok! Would you like to visit {US_visit_random}? Yes or No. ")
            if US_visit_user_select == "Yes":
                print(f"You will be visiting {US_visit_random}")
                US_visit = False
            elif US_visit_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        US_activity = True
        while US_activity == True:
            US_activity_random = random_list_selector(things_to_do_US)
            US_activity_user_select = input(f"Ok! Does {US_activity_random} sound good for your main activity? Yes or No. ")
            if US_activity_user_select == "Yes":
                print(f"You will be {US_activity_random}.")
                US_activity = False
            elif US_activity_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        US_transportation = True
        while US_transportation == True:
            US_transportation_random = random_list_selector(transportation_US)
            US_transportation_user_select = input(f"Ok! Would you like to travel by {US_transportation_random}? Yes or No. ")
            if US_transportation_user_select == "Yes":
                print(f"You will be travelling by a {US_transportation_random}.")
                US_transportation = False
            elif US_transportation_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        US_accomodation = True
        while US_accomodation == True:
            US_accomodation_random = random_list_selector(places_to_stay_US)
            US_accomodation_user_select = input(f"Ok! Would you like to stay in a {US_accomodation_random}? Yes or No. ")
            if US_accomodation_user_select == "Yes":
                print(f"You will be staying in a {US_accomodation_random}.")
                US_accomodation = False
            elif US_accomodation_user_select == "No":
                continue
            else:
                print("Please enter Yes or No.")
        confirmation = input(f"Ok! You will travel to {US_visit_random}. You will be travelling by {US_transportation_random}. You will be staying in a {US_accomodation_random}. And you will be {US_activity_random} for your main activity. Does this sound good? Yes or No. ")
        if confirmation == "No":
            print("Ok! Lets try again.")
            continue
        elif confirmation == "Yes":
            print("Ok! Enjoy your trip.")
            main_loop == False
    else:
        print("Please select SE Asia or US.")


    
    
        

        
            
        




