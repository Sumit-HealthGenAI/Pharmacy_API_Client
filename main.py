from api_client import get_medicine, validate_medicine_id
from menu import display_menu
from requests.exceptions import RequestException

print("Running main application")


while True:
    choice = display_menu()

    if choice == "1":
        print("Retrieving medicine...")

        try:
            medicine_id = input("Enter medicine ID: ")

            validated_id = validate_medicine_id(medicine_id)

            medicine = get_medicine(validated_id)
            print(medicine)

        except ValueError as error:
            print(f"Invalid medicine ID: {error}")

        except RequestException as error:
            print(f"API request failed: {error}")

    elif choice == "2":
        print("Exiting application...")
        break

    else:
        print("Invalid choice!")
