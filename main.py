def main(): 
    clubs = [
        Club("Club A", "Address A"),
        Club("Club B", "Address B"),
        Club("Club C", "Address C"),
        Club("Club D", "Address D"),
    ]

members = []

while True:
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Display Member Information")
    print("4. Check in Member")
    print("5. Generate Bill")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1: #add member
        pass
    elif choice == 2: #remove member
        pass
    elif choice == 3: #display member info
        pass
    elif choice == 4: #check in member
        pass
    elif choice == 5: #generate bill
        pass
    elif choice == 6: #exit
        print("Exiting  ")
        break
    else: 
        print("Invalid choice. Please select again.")

if __name__== "__main__":
    main()