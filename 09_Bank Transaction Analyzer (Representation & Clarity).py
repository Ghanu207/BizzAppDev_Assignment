def bank_transaction_analyzer():
    print("🏦 Welcome to the Bank Transaction Analyzer!")
    print("Enter transactions like: credit 1000 or debit 500")
    print("Type 'done' when finished.\n")

    # Step 1: Initialize balance and transaction list
    balance = 0
    transactions = []

    # Step 2: Take user input in a loop
    while True:
        entry = input("Enter transaction: ").strip().lower()

        # Exit condition
        if entry == 'done':
            break

        # Step 3: Parse input
        parts = entry.split()
        if len(parts) != 2:
            print("❌ Format Error. Use: credit <amount> or debit <amount>\n")
            continue

        action, amount_str = parts

        # Step 4: Validate the amount
        try:
            amount = float(amount_str)
        except ValueError:
            print("❌ Invalid amount. Enter a number.\n")
            continue

        # Step 5: Process transaction
        if action == 'credit':
            balance += amount
            transactions.append(('Credit', amount, balance))  # record transaction
        elif action == 'debit':
            balance -= amount
            transactions.append(('Debit', amount, balance))  # record transaction
        else:
            print("❌ Unknown transaction type. Use 'credit' or 'debit'.\n")
            continue

        # Step 6: Print current balance
        print(f"✅ {action.capitalize()} of ₹{amount:.2f} recorded. Balance: ₹{balance:.2f}\n")

    # Step 7: Final Summary
    print("\n📊 Transaction Summary")
    print("{:<10} {:>10} {:>20}".format("Type", "Amount", "Balance After"))
    print("-" * 42)
    for t_type, amt, bal in transactions:
        print("{:<10} ₹{:>9.2f} ₹{:>18.2f}".format(t_type, amt, bal))

    # Step 8: Print final balance
    print("\n💰 Final Balance: ₹{:.2f}".format(balance))


# Run the analyzer
bank_transaction_analyzer()
