import datetime
from time import strftime

Date= input ("Enter Date: YYYY-MM-DD")
print (Date)

#Enter Date of birth

Year, Month, Day = map(int, Date.split("-"))
date = datetime.date(Year, Month, Day)
Day= date.strftime("%A")
print("The Day you were born is "+Day)

#Enter Gender
Gender= input ("Enter Gender: Male or Female")
while Gender not in ["Male","Female"]:
    print("Gender not recognized")
    Gender= input ("Enter Gender: Male or Female")

asante_male_names = {"Monday": "Kwadwo", "Tuesday": "Kwabena","Wednesday": "Kwaku","Thursday": "Yaw","Friday": "Kofi","Saturday": "Kwame","Sunday": "Kwasi"}
asante_female_names = {"Monday": "Adwoa", "Tuesday": "Abenaa", "Wednesday": "Akua", "Thursday": "Yaa", "Friday": "Afua", "Saturday": "Ama", "Sunday": "Akosua" }

if Gender == "Male":

    asante_name = asante_male_names[Day]
    print("Your Asante name is "+asante_name)
else:
    asante_name = asante_female_names[Day]
    print("Your Asante name is "+asante_name)