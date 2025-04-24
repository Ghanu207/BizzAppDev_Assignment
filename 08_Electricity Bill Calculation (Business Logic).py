"""
Approach:
1. Accept electricity usage input from the user.
2. Calculate cost for each slab.
3. Print detailed breakdown and total bill.
"""

def calculate_bill(units):
    total = 0
    breakdown = []

    if units <= 100:
        total = units * 5
        breakdown.append(f"0-100 units @ 5/unit = {total} ₹")
    elif units <= 300:
        total = 100 * 5 + (units - 100) * 7
        breakdown.append("0-100 units @ 5/unit = 500 ₹")
        breakdown.append(f"101-{units} units @ 7/unit = {(units - 100) * 7} ₹")
    elif units <= 500:
        total = 100 * 5 + 200 * 7 + (units - 300) * 10
        breakdown.append("0-100 units @ 5/unit = 500 ₹")
        breakdown.append("101-300 units @ 7/unit = 1400 ₹")
        breakdown.append(f"301-{units} units @ 10/unit = {(units - 300) * 10} ₹")
    else:
        total = 100 * 5 + 200 * 7 + 200 * 10 + (units - 500) * 15
        breakdown.append("0-100 units @ 5/unit = 500 ₹")
        breakdown.append("101-300 units @ 7/unit = 1400 ₹")
        breakdown.append("301-500 units @ 10/unit = 2000 ₹")
        breakdown.append(f"501-{units} units @ 15/unit = {(units - 500) * 15} ₹")

    return breakdown, total

# Example usage
try:
    usage = int(input("Enter electricity usage in kWh: "))
    bill_details, total_amount = calculate_bill(usage)

    print("\nElectricity Bill:")
    for line in bill_details:
        print(line)
    print(f"Total Amount Payable = {total_amount} ₹")

except ValueError:
    print("Invalid input. Please enter a valid number of units.")
