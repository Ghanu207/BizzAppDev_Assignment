"""
Approach:
1. Take two dates as input in the format dd-mm-yyyy.
2. Convert them into date objects using datetime module.
3. Subtract the two date objects to find the difference in days.
"""

from datetime import datetime

def calculate_days_lived(birthdate_str, currentdate_str):
    try:
        # Parse the input strings into datetime objects
        birth_date = datetime.strptime(birthdate_str, "%d-%m-%Y")
        current_date = datetime.strptime(currentdate_str, "%d-%m-%Y")

        # Calculate the difference
        difference = current_date - birth_date
        return difference.days

    except ValueError:
        return "Invalid date format. Please use dd-mm-yyyy."

# Example usage
birth_input = input("Enter your birthdate (dd-mm-yyyy): ")
today_input = input("Enter today's date (dd-mm-yyyy): ")

result = calculate_days_lived(birth_input, today_input)

if isinstance(result, int):
    print(f"You have lived for {result} days.")
else:
    print(result)
