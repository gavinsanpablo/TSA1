import csv

def convert_currency(amount, target_currency):
    try:
        with open('ACT4B/currency.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['code'] == target_currency:
                    rate = float(row['rate'])
                    converted_amount = amount * rate
                    return converted_amount
            return None  
    except FileNotFoundError:
        print("Currency file not found.")
        return None

def main():
    try:
        dollar_amount = float(input("How much dollar do you have? "))
        target_currency = input("What currency you want to have? ").upper()

        converted_amount = convert_currency(dollar_amount, target_currency)

        if converted_amount:
            print(f"Dollar: {dollar_amount} USD")
            print(f"{target_currency}: {converted_amount:.2f}")
        else:
            print("Target currency not found in the database.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the dollar amount.")

if __name__ == "__main__":
    main()