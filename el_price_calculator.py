NETZENTGELT = {"Kärnten": 9.67}

#calculates current grid fee and applies SNAP discount if necessary
def current_grid_fee(month, hour):
    base_fee = NETZENTGELT["Kärnten"]
    snap_active = 4 <= month <= 9 and 10 <= hour < 16
    return base_fee * 0.8 if snap_active else base_fee

#makes sure that the entered numbers stay within 1-12 and 0-23
def get_valid_number(prompt, min_value, max_value):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if min_value <= value <= max_value:
                return value
        print(f"Invalid input. Enter a number from {min_value} to {max_value}.")

#handles user input and prints the result
def main():
    month = get_valid_number("Enter month (1-12): ", 1, 12)
    hour = get_valid_number("Enter hour (0-23): ", 0, 23)
    fee = current_grid_fee(month, hour)

    print("\nCurrent grid fee:")
    print(f"{fee:.2f} ct/kWh")

    if 4 <= month <= 9 and 10 <= hour < 16:
        print("SNAP discount is active.")
    else:
        print("Standard grid fee applies.")

#runs the function when the file is started directly
if __name__ == "__main__":
    main()