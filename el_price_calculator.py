NETZENTGELT = {"Kärnten": 9.67}


def current_grid_fee(month, hour):
    base_fee = NETZENTGELT["Kärnten"]
    snap_active = 4 <= month <= 9 and 10 <= hour < 16
    return base_fee * 0.8 if snap_active else base_fee


def main():
    month = int(input("Enter month (1-12): "))
    hour = int(input("Enter hour (0-23): "))

    fee = current_grid_fee(month, hour)

    print("\nCurrent grid fee:")
    print(f"{fee:.2f} ct/kWh")

    if 4 <= month <= 9 and 10 <= hour < 16:
        print("SNAP discount is active.")
    else:
        print("Standard grid fee applies.")


if __name__ == "__main__":
    main()

    #comment: just for testing