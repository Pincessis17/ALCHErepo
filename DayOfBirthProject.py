import datetime

dob = input("Enter your date of birth (YYYY-MM-DD): ")
year, month, day = map(int, dob.split("-"))

date = datetime.date(year, month, day)
day =  date.strftime("%A")
print(f"You were born on a {day}.")

gender = input("Enter your gender (B or G):").strip().upper()
while gender not in ['B', 'G']:
    print("Invalid gender input. Please enter 'B' for boy or 'G' for girl.")
    gender = input("Enter gender (B for boy, G for girl): ")

GirlNames = {"Monday": "Adwoa", "Tuesday": "Abenaa", "Wednesday": "Akua",
             "Thursday": "Yaa", "Friday": "Afua", "Saturday": "Ama", "Sunday": "Akosua"}
BoyNames = {"Monday": "Kwadwo", "Tuesday": "Kwabena", "Wednesday": "Kwaku",
            "Thursday": "Yaw", "Friday": "Kofi", "Saturday": "Kwame", "Sunday": "Kwasi"}
if gender == 'B':
    name = BoyNames[day]
    print(f"Your Ashanti name is {name}.")  
else:
    name = GirlNames[day]
    print(f"Your Ashanti name is {name}.")

