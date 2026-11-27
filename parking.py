def calculate_parking_fee():
    print("--- Parking Fee Calculator ---")
    print("Vehicle Types: Two-wheeler, Four-wheeler, Heavy vehicle")
    
    vehicle_type = input("Enter vehicle type: ").strip().lower()
    hours = float(input("Enter parking duration (in hours): "))

    if vehicle_type == "two-wheeler":
        rate = 20
        display_type = "Two-wheeler"
    elif vehicle_type == "four-wheeler":
        rate = 50
        display_type = "Four-wheeler"
    elif vehicle_type == "heavy vehicle":
        rate = 100
        display_type = "Heavy vehicle"
    else:
        print("Invalid vehicle type entered.")
        return

    total_fee = rate * hours

    print("\n--- Parking Receipt ---")
    print(f"Vehicle Type     : {display_type}")
    print(f"Parking Duration : {hours} hours")
    print(f"Total Parking Fee: Rs. {total_fee:.2f}")

if __name__ == "__main__":
    calculate_parking_fee()