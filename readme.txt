"NYC Restaurant Generator" is a program that allows users to select a restaurant from a database that is matched to
their food, price, and location preferences.

Motivation:
The program was written inspired by my personal passion for food, as well as a desire to further explore restaurants
in New York City, the place I am lucky enough to call home! This project was a wonderful summation of Python, as well 
as a great introduction to PANDAS and basic data analysis. In the future, I hope that the project can become applicable
on a larger scale through gaining more and more data. The program should continue to run if additional rows are added 
onto the initial CSV file, but I would also love to integrate information such as a distance calculation (using Google 
Places API), or information on restaurants in other cities and states.

How the Program Works:
The program involves 3 Python files ("main", "User", and "Restaurant"), as well as 2 CSV files ("user_data" and
"restaurant_week_2018_final"). The program can be run simply by running the "main" file.

Upon starting the program, users will be asked if they are new or returning users. If they are new users, they will
be instructed to enter information about their location, tastes, and other preferences. This information is then 
written to the "user_data" CSV file (there are currently a few examples of users already written to the file), so it 
can be accessed in the future, and stored as an object in the User class. If the user is a returning user, they can 
access their old information via their unique username and make edits accordingly. These edits will then be changed in 
the CSV file and saved as an object.

The Restaurant file contains the Restaurant class, which has attributes such as name, address, and a brief description
of the restaurant. The Restaurant class contains a function which takes user preferences as a parameter, and generates
a restaurant recommendation based on these preferences. To do so, it converts the original Restaurant data to a PANDAS
dataframe, and filters out data according to preferences. The program prioritizes (1) location, (2) type of restaurant,
(3) price, and (4) restaurant features. The class also includes a random feature, which generates a random 
restaurant from the spreadsheet. After generating the restaurant recommendation, the restaurant's information is saved 
as individual attributes in the Restaurant class, so that the restaurant's information can be printed and displayed 
to the user.

Acknowledgements: 
This program was made using Python 3.8, and utilizes the PANDAS module, which can be installed 
here: https://pandas.pydata.org/

The original restaurant data used in the program can be found on Kaggle here: 
https://www.kaggle.com/popoandrew/restaurant-week-2018
It was uploaded by Kaggle User "popoandrew" and uses data that was scraped from OpenTable.

Author: 
"NYC Restaurant Generator" was written by Samantha Zhang (samanthz@usc.edu) in April of 2019.