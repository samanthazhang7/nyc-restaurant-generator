# Samantha Zhang, samanthz@usc.edu
# ITP 115 Final Project
# Python File 3 of 3

import pandas as pd
import random


class Restaurant(object):
    def __init__(self, name, address, restaurant_type, price_range, description):
        self.name = name
        self.address = address
        self.restaurant_type = restaurant_type
        self.price_range = price_range
        self.description = description

    # Takes the user's preferences as parameters, and returns the name of a restaurant that is best matched to them
    def generateRecommendation(self, userZip, userType, userPrice, userFeature):
        df = pd.read_csv("restaurant_week_2018_final.csv")

        # Create a new column with a weighted score based on User's favorite feature.
        if userFeature == "Food":
            df["weighted_score"] = 0.6 * df["food_review"] + 0.1 * df["ambience_review"] + 0.1 * df["value_review"
            ] + 0.1 * df["service_review"]
        elif userFeature == "Ambiance":
            df["weighted_score"] = 0.1 * df["food_review"] + 0.6 * df["ambience_review"] + 0.1 * df["value_review"
            ] + 0.1 * df["service_review"]
        elif userFeature == "Value":
            df["weighted_score"] = 0.1 * df["food_review"] + 0.1 * df["ambience_review"] + 0.6 * df["value_review"
            ] + 0.1 * df["service_review"]
        elif userFeature == "Service":
            df["weighted_score"] = 0.1 * df["food_review"] + 0.1 * df["ambience_review"] + 0.1 * df["value_review"
            ] + 0.6 * df["service_review"]

        # Create different dataframes matched to each level of user input. The program prioritizes:
        # 1. Matching zip code
        # 2. Matching restaurant genre (Italian, Vietnamese, etc.)
        # 3. Price preference
        # 4. Feature preference (based on weighted score)
        df["postal_code"] = pd.to_numeric(df["postal_code"])  # convert the entire column to int
        correctZip = df.loc[df["postal_code"] == int(userZip)]
        userTypeDF = df.loc[(df["postal_code"] == int(userZip)) & (df["restaurant_type"] == userType.title())]
        priceRangeDF = df.loc[(df["postal_code"] == int(userZip)) & (df["restaurant_type"] == userType.title()) &
                              (df["price_range"] == userPrice)]
        finalDF = priceRangeDF.sort_values(by=["weighted_score"], ascending=False)
        if len(correctZip.index) == 1 or len(userTypeDF) == 0:  # only one restaurant whose zip matches user's zip
            return correctZip.iloc[0, 0] # return the first column of the first cell (name of the restaurant)
        else:  # filter by matching zip and type of food
            if len(userTypeDF.index) == 1 or len(priceRangeDF.index) == 0:
                return userTypeDF.iloc[0, 0]
            else:  # filter by matching zip, type of food, and price range
                if len(priceRangeDF.index) == 1:
                    return priceRangeDF.iloc[0, 0]
                else:
                    # all the restaurants currently in the data frame match the user's preferences, so sort their
                    # weighted scores from highest to lowest and return the first one
                    finalDF = priceRangeDF.sort_values(by=["weighted_score"], ascending=False)
                    return finalDF.iloc[0, 0]

    # Generates a list of all restaurant names and returns the name of a random restaurant
    def generateRandomRestaurant(self):
        df = pd.read_csv("restaurant_week_2018_final.csv")
        listOfRestaurants = df["name"].tolist()
        return random.choice(listOfRestaurants)

    # Takes the restaurant's name as a parameter, reads the CSV file to set the restaurant's attributes to the
    # corresponding values from the CSV.
    def getRestaurant(self, name):
        df = pd.read_csv("restaurant_week_2018_final.csv", index_col="name")
        restaurantList = df.loc[name].tolist()
        self.name = name
        self.address = restaurantList[0]
        self.restaurant_type = restaurantList[5]
        self.price_range = restaurantList[11]
        self.description = restaurantList[17]


    # In order to prevent the description from printing on one long line, reformat the string so that it includes
    # a line break every twenty words.
    def getFormattedDesc(self, description):
        list = description.split(" ")
        formattedString = ""
        counter = 0
        for word in list:
            if counter % 20 == 0:
                formattedString += "\n" + word
            else:
                formattedString += " " + word
            counter += 1
        self.description = formattedString


    def __str__(self):
        string = "Name: " + str(self.name) + "\nAddress: " + str(self.address) + "\nType of Food: " + str(
            self.restaurant_type) + "\nPrice Range: " + str(self.price_range) + "\nDescription: " + str(
            self.description)
        return string
