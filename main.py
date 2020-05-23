# Samantha Zhang, samanthz@usc.edu
# ITP115 Final Project
# Python File 1 of 3

import pandas as pd
from User import User
from Restaurant import Restaurant

def main():
    print("Welcome to the NYC Restaurant Generator!")
    print("Let's find a restaurant in New York City that is perfectly matched to your tastes.")

    user = User("", 0, "", "", "") # Initialize a user object. The attributes will be updated once the
                                    # user inputs their information
    newUserInput = input("Are you a (1) new user or (2) returning user? ")
    while newUserInput.isdigit() == False:
        print("Please enter 1 or 2.")
        newUserInput = input("Are you a (1) new user or (2) returning user? ")
    while int(newUserInput) != 1 and int(newUserInput) !=2:
        print("Please enter 1 or 2.")
        newUserInput = input("Are you a (1) new user or (2) returning user? ")

    if int(newUserInput) ==1: # User is a new user
        # Call the corresponding functions in the user class to obtain user preferences:
        usernameInput = User.getUserName(user)
        zipInput = User.getUserZip(user)
        genreInput = User.getUserGenre(user)
        priceInput = User.getPriceRange(user)
        featureInput = User.getFavQuality(user)

        # Write user preferences to the CSV File
        User.writeFile(user, usernameInput.lower(), zipInput, genreInput.lower(), priceInput, featureInput)

        # Update the object attributes to user's preferences
        User.updateUser(user, usernameInput)

    elif int(newUserInput)==2: # User is a returning user
        returningUserName = input("Please enter your username: ")
        while User.checkUserName(user, returningUserName) == False: # Error-checking to make sure username exists
            print("Your username is not currently in our database. Please try again.")
            returningUserName = input("Please enter your username: ")
        User.updateUser(user, returningUserName) # update the user object with the correct information

        # Read from the CSV file to retrive user's information. This is necessary in order to print out user information
        # before it is altered by the user.
        data = pd.read_csv("user_data.csv", index_col="username")
        userRowIndex = data.loc[returningUserName.lower()]
        userList = userRowIndex.tolist()

        print("Welcome back,", returningUserName.title())
        print("Here is your current profile: ")
        print("Username:", returningUserName.title())
        print("Zip Code:", str(userList[0]))
        print("Preferred Restaurant Type:", userList[1].title())
        print("Price Range:", userList[2])
        print("Preferred Feature:", userList[3])

        editInput = input("\nWould you like to edit your profile? (Y/N): ")

        while editInput.lower()!="y" and editInput.lower()!="n":
            print("Invalid input. Please enter Y or N.")
            editInput = input("Would you like to edit your profile? (Y/N): ")

        if editInput.lower() == "y": # User wants to edit their information
            editContinue = True

            while editContinue == True:
                User.editUserInfo(user, returningUserName) # Run the function to correct ONE aspect of their profile
                User.updateUser(user, returningUserName) # Update attribute information in the User class
                print("Here is your updated profile: ")
                print(user)

                continueInput = input("Would you like to edit another feature? (Y/N) ")
                while continueInput.lower() != "y" and continueInput.lower()!= "n":
                    print("Invalid input. Please enter Y or N.")
                    continueInput = input("Would you like to edit another feature? (Y/N) ")
                if continueInput.lower()=="n": # user does not want to edit anything else
                    editContinue=False
                elif continueInput.lower()=="y": # user wants to edit something else
                    editContinue=True

    continueChoice = True
    while continueChoice == True:
        # Generate the restaurant recommendation using functions in the Restaurant class
        restaurant = Restaurant("","","","","") # Initialize the restaurant variable, which will be updated once
                                                # a restaurant is generated for the user.
        print("\nWould you like a (1) randomly generated restaurant, or (2) a restaurant based off your preferences?")
        randomRestaurantInput = input("> ")
        while randomRestaurantInput.isdigit() == False:
            print("Invalid input. Please enter 1 or 2.")
            print("\nWould you like a (1) randomly generated restaurant, or (2) a restaurant based off your preferences?")
            randomRestaurantInput = input("> ")
        while int(randomRestaurantInput) != 1 and int(randomRestaurantInput) != 2:
            print("Invalid input. Please enter 1 or 2.")
            print("\nWould you like a (1) randomly generated restaurant, or (2) a restaurant based off your preferences?")

        if int(randomRestaurantInput) == 1: # user wants a randomly generated restaurant
            # Randomly generate a restaurant name:
            restaurantName = Restaurant.generateRandomRestaurant(restaurant)

            # Using the restaurant name, retrieve the rest of the restaurant's information from the data
            Restaurant.getRestaurant(restaurant, restaurantName)

        elif int(randomRestaurantInput) == 2: # user wants a restaurant generated based on their preferences
            restaurantName = Restaurant.generateRecommendation(restaurant, user.zip_code, user.restaurant_type,
                                                               user.price_range, user.preferred_feature)
            Restaurant.getRestaurant(restaurant, restaurantName)

        # Re-formats the restaurant description so it is not printed in one long line of code:
        Restaurant.getFormattedDesc(restaurant, restaurant.description)
        print("Here is your restaurant recommendation:")
        print(restaurant)

        continueInput = input("\nWould you like to generate another recommendation? (Y/N): ")
        while continueInput.lower() != "y" and continueInput.lower() != "n":
            print("Invalid input. Please enter Y or N.")
            continueInput = input("\nWould you like to generate another recommendation? (Y/N): ")
        if continueInput.lower() == "n":
            continueChoice = False

    print("\nThanks for using the NYC Restaurant Generator. Happy eating!")

main()
