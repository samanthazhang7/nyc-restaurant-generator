# Samantha Zhang, samanthz@usc.edu
# ITP 115 Final Project
# Python File 2 of 3

import pandas as pd
import csv

class User(object):
    def __init__(self, username, zip_code, restaurant_type, price_range, preferred_feature):
        self.username = username
        self.zip_code = zip_code
        self.restaurant_type = restaurant_type
        self.price_range = price_range
        self.preferred_feature = preferred_feature

    # Generates a list of the genres (American, Chinese, etc.) available in the database to be used for error checking.
    def getGenres(self):
        data = pd.read_csv("restaurant_week_2018_final.csv")  # convert CSV file to Pandas dataframe
        listOfGenresRepeats = data["restaurant_type"]  # convert a column of the dataframe to a list
        listOfGenres = []
        for genre in listOfGenresRepeats:  # Use for loop to avoid printing out repeated genres
            if genre not in listOfGenres:
                listOfGenres.append(genre)
        listOfGenres.sort()
        return listOfGenres

    # Generates a list of the zip codes available in the database to be used for error checking.
    def getZipCodes(self):
        data = pd.read_csv("restaurant_week_2018_final.csv")
        listOfZipsRepeats = data["postal_code"]
        listOfZips = []
        for zip in listOfZipsRepeats:
            if zip not in listOfZips:
                listOfZips.append(zip)
        listOfZips.sort()
        return listOfZips

    # Gets username input from a user, error checks to make sure the username is not taken, return the username
    def getUserName(self):
        usernameInput = input("Please enter a username: ")
        while User.checkUserName(self, usernameInput) == True:  # check for whether the username is already taken
            print("Username is already taken. Please enter another username.")
            usernameInput = input("Please enter a username: ")
        self.username = usernameInput
        return self.username


    # Asks user for their zip code, error checks for whether the zip code is in the database or not, returns zip code
    def getUserZip(self):
        zipInput = input("Please enter your current Zip Code: ")
        zipList = User.getZipCodes(self)
        while zipInput.isdigit() == False:
            print("Invalid input. Please enter a valid zip code.")
            zipInput = input("Please enter your current Zip Code: ")
        while float(zipInput) not in zipList:
            print("The zip code you entered is not in our database. Please try again.")
            # If user enters a zip code that is not currently in our database, ask if they would like to see a list
            # of available zip codes
            viewZipListInput = input("Would you like to see a list of available zip codes? (Y/N) ")
            while viewZipListInput.lower() != "y" and viewZipListInput.lower() != "n":
                print("Invalid input. Please enter Y or N.")
                viewZipListInput = input("Would you like to see a list of available zip codes? (Y/N) ")
            if viewZipListInput.lower() == "y":
                for zip in zipList:
                    print(str(zip))
            zipInput = input("Please enter your current Zip Code: ")
        self.zip_code = zipInput
        return self.zip_code

    # Asks user for their favorite genre, error checks for whether or not the genre is in the database, returns genre
    def getUserGenre(self):
        genreInput = input("Please enter your favorite type of food: ")
        listOfGenres = User.getGenres(self)
        while genreInput.title() not in listOfGenres:
            print("The food type you entered is not in our database. Please try again.")
            viewGenreListInput = input("Would you like to see a list of available food types? (Y/N) ")
            while viewGenreListInput.lower() != "y" and viewGenreListInput.lower() != "n":
                print("Invalid input. Please enter Y or N.")
                viewGenreListInput = input("Would you like to see a list of available food types? (Y/N) ")
            if viewGenreListInput.lower() == "y":
                for genre in listOfGenres:
                    print(genre.title())
            genreInput = input("Please enter your favorite type of food: ")
        self.restaurant_type = genreInput
        return self.restaurant_type

    # Ask user for their preferred price range, error checks, returns price range
    def getPriceRange(self):
        print("What is your preferred price range?")
        print("A) Under $30")
        print("B) $31 to $50")
        print("C) $50 and over")
        priceInput = input("> ")
        while priceInput.lower() != "a" and priceInput.lower() != "b" and priceInput.lower() != "c":
            print("Invalid input. Please enter A, B, or C.")
            priceInput = input("> ")
        if priceInput.lower() == "a":
            priceInput = "Under $30"
        elif priceInput.lower() == "b":
            priceInput = "$31 to $50"
        elif priceInput.lower() == "c":
            priceInput = "$50 and over"
        self.price_range = priceInput
        return self.price_range

    # Ask user for their preferred quality (ambiance, value, etc), error check, and return most valued quality.
    def getFavQuality(self):
        print("\nWhat are you most looking for in a restaurant?")
        print("A) Quality of food")
        print("B) Quality of service")
        print("C) Ambiance")
        print("D) Value")
        featureInput = input("> ")
        while featureInput.lower() != "a" and featureInput.lower() != "b" and featureInput.lower() != "c" and featureInput.lower() != "d":
            print("Invalid input. Please enter A, B, C, or D.")
            featureInput = input("> ")
        if featureInput.lower() == "a":
            featureInput = "Food"
        elif featureInput.lower() == "b":
            featureInput = "Service"
        elif featureInput.lower() == "c":
            featureInput = "Ambiance"
        elif featureInput.lower() == "d":
            featureInput = "Value"
        self.preferred_feature = featureInput
        return self.preferred_feature

    # Write to a current CSV file with user information so that it is stored for future use
    # Take username, user preferences, and user's current zip code as parameters
    def writeFile(self, username, zip_code, restaurant_type, price, feature):
        fileIn = open("user_data.csv", "a", newline="")
        writer = csv.writer(fileIn)
        writer.writerow([username, zip_code, restaurant_type, price, feature])
        fileIn.close()

    # Take username as a parameter, check whether or not the username has been taken (whether or not it currently exists
    # in the CSV file). Returns True if the Username is already used, False if not.
    def checkUserName(self, username):
        data = pd.read_csv("user_data.csv")
        listOfUserNames = data["username"].tolist()  # Convert the "usernames" column of the CSV to a list
        if username in listOfUserNames:
            return True  # return True if Username is a repeat
        else:
            return False

    # Takes no parameters, edits user profile as it currently exists in the csv file.
    # Prints out list of options pertaining to which aspect of user's profile they want to edit
    # Then, prints out final profile when done making the edits
    def editUserInfo(self, username):
        data = pd.read_csv("user_data.csv", index_col="username")  # convert CSV to pandas dataframe
        print("What would you like to edit?")
        print("A) Zip Code")
        print("B) Preferred Restaurant Type")
        print("C) Price Range")
        print("D) Preferred feature")
        editChoice = input("> ")
        while editChoice.lower() != "a" and editChoice.lower() != "b" and editChoice.lower() != "c" and editChoice.lower() != "d":
            print("Invalid input. Please enter A, B, C, or D.")
            editChoice = input("> ")

        # Run the corresponding function to error check user input, then write to CSV file in the corresponding cell
        if editChoice.lower() == "a":  # user wants to edit their zip code
            newZip = User.getUserZip(self)
            data.at[username, "zip_code"] = int(newZip)
        elif editChoice.lower() == "b":  # user wants to edit their preferred restaurant type
            newRestaurantType = User.getUserGenre(self)
            data.at[username, "preferred_restaurant_type"] = newRestaurantType.lower()
        elif editChoice.lower() == "c":  # user wants to edit price range
            newPriceRange = User.getPriceRange(self)
            data.at[username, "price_range"] = newPriceRange
        elif editChoice.lower() == "d":  # user wants to edit preferred feature
            newQuality = User.getFavQuality(self)
            data.at[username, "preferred_feature"] = newQuality

        data.to_csv("user_data.csv")  # convert back to CSV format

    # After a returning user's features have been changed, this function updates all of the corresponding attributes
    # in the user class
    def updateUser(self, username):
        data = pd.read_csv("user_data.csv", index_col="username")
        userRowIndex = data.loc[username.lower()]
        userList = userRowIndex.tolist()
        self.username = username
        self.zip_code = userList[0]
        self.restaurant_type = userList[1]
        self.price_range = userList[2]
        self.preferred_feature = userList[3]

    def __str__(self):
        string = "Username: " + self.username.title() + "\nZip Code: " + str(
            self.zip_code) + "\nPreferred Restaurant Type: " + str(
            self.restaurant_type.title()) + "\nPrice Range: " + str(self.price_range) + "\nPreferred Feature: " + str(
            self.preferred_feature)
        return string



