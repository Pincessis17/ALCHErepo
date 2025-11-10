from datetime import datetime

#a function that takes dob and return corresponding day index.
def get_day(day,month,year):
    birthday = datetime(year,month,day)
    return birthday.weekday()

#a function that takes in user details and calls get date function
def collect_input():
    user_year = int(input("Enter your year of birth: "))
    user_month = int(input("Enter the month of birth( eg, Enter 2 if your month is February: "))
    user_day = int(input("Enter your day of birth: ")) + 1
    return get_day(user_day,user_month,user_year)

# a function that calls collect input function and allocates name
def allocate_name():
    user_gender = input("Enter your gender (male/female): ")
    female_names = ["Akosua","Adwoa","Abeena","Akwa","Yaa","Afia","Amma"]
    male_names = ["Kwasi","Kadjo","Kwabena","Kwaku","Yaw","Kofi","Kwame"]

    if user_gender == "female":
        return print("Your name is",female_names[collect_input()])
    elif user_gender == "male":
        return print("Your name is",male_names[collect_input()])
    else:
        return print("error encountered , check your details and try again")

allocate_name()