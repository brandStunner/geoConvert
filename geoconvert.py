
def dms_to_dd_main():
    """Your DMS to DD conversion program"""
    print("Enter your longitude coordinates")
    lon = parts(coordinate_type="longitude")

    print("Enter your latitude coordinates")
    lat = parts(coordinate_type="latitude")

    print(f"Longitude: {lon}, \nLatitude: {lat}")

def parts(coordinate_type="coordinates"):
    """Your DMS input and conversion function"""
    print(f"\nEnter your {coordinate_type} coordinates in dms format")

    degree = int(input(f"Enter your {coordinate_type} degree value: ").strip())
    minute = int(input(f"Enter your {coordinate_type} minute value: ").strip())
    seconds = float(input(f"What's your {coordinate_type} seconds value: ").strip())

    if coordinate_type.lower() == 'longitude':
        direction = input("Enter direction,E for East and W for West: ").strip().upper()
        if direction == "W":
            sign = -1
        else:
            sign = 1
    else:
        direction = input("Enter direction,N for North, S for South: ").strip().upper()
        if direction == "N":
            sign = 1
        else:
            sign = -1

    # Convert DMS to Decimal Degrees
    dd = degree + (minute / 60) + (seconds / 3600)
    dd = round(dd, 6)
    dd *= sign
    return dd

def dd_to_dms_main():
    """Your DD to DMS conversion program"""
    print("Welcome to geoConvert")
    current_coordinate = input("Enter coordinates in decimal degrees (longitude, latitude), separated by comma: ")
    try:
        lon, lat = current_coordinate.strip().split(",")
        lon = float(lon)
        lat = float(lat)

        lon_dms = decimal_to_dms(lon, is_latitude=False)
        lat_dms = decimal_to_dms(lat, is_latitude=True)

        print(f"Converted Coordinates:\nLongitude: {lon_dms}\nLatitude:  {lat_dms}")

    except ValueError:
        print("Invalid input. Please enter two decimal numbers separated by a comma.")

def decimal_to_dms(decimal, is_latitude=True):
    """Your decimal to DMS conversion function"""
    # Store direction based on sign
    direction = ""
    if is_latitude:
        direction = "N" if decimal >= 0 else "S"
    else:
        direction = "E" if decimal >= 0 else "W"

    # Work with absolute value
    decimal = abs(decimal)
    degrees = int(decimal)
    minutes_decimal = (decimal - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = round((minutes_decimal - minutes) * 60, 2)

    return f"{degrees}° {minutes}′ {seconds}″ {direction}"

def main_menu():
    """Main menu to choose conversion type"""
    while True:
        print("\n" + "="*50)
        print("         WELCOME TO COORDINATE CONVERT")
        print("="*50)
        print("1. Convert DMS to Decimal Degrees")
        print("2. Convert Decimal Degrees to DMS")
        print("3. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n--- DMS to Decimal Degrees ---")
            dms_to_dd_main()
        elif choice == '2':
            print("\n--- Decimal Degrees to DMS ---")
            dd_to_dms_main()
        elif choice == '3':
            print("Thank you for using the Coordinate Converter!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        # Ask if user wants to continue
        if choice in ['1', '2']:
            continue_choice = input("\nWould you like to perform another conversion? Type y if Yes or n if no: ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("Thank you for using the Coordinate Converter!")
                break

if __name__ == "__main__":
    main_menu()