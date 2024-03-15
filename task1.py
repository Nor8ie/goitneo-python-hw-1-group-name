from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Prepare data structure to store birthdays for each day of the week
    birthdays_per_week = defaultdict(list)

    # Get current date
    today = datetime.today().date()

    # Iterate through each user
    for user in users:
        # Extract user's name and birthday
        name = user["name"]
        birthday = user["birthday"].date()

        # Convert birthday to the current year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday for this year has passed, consider next year's birthday
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference in days between birthday and current date
        delta_days = (birthday_this_year - today).days

        # Check if birthday is within the next week
        if 0 <= delta_days < 7:
            # Determine the day of the week for the birthday
            birthday_weekday = birthday_this_year.strftime("%A")

            # If birthday falls on a weekend, move it to Monday
            if birthday_weekday == "Saturday":
                birthday_weekday = "Monday"
            elif birthday_weekday == "Sunday":
                birthday_weekday = "Monday"

            # Store the user's name for the corresponding day of the week
            birthdays_per_week[birthday_weekday].append(name)

    # Display the collected names by day of the week
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 3, 16)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 15)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 3, 15)},
    {"name": "John Doe", "birthday": datetime(1990, 3, 12)} ]

get_birthdays_per_week(users)