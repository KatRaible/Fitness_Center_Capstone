from FitnessClass import *

def main(): 
    clubs = [
        Club("Green Fitness", "Coast City"),
        Club("Red Fitness", "Starling City"),
        Club("Daily Fitness", "Metropolis"),
        Club("Bat Fitness", "Gotham City")
    ]

    members = []

    while True:
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Display Member Information")
        print("4. Check in Member")
        print("5. Display Bill")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1: 
            member_id = input("Enter Member ID: ")
            name = input("Enter member name: ")
            print("Select club for the member:")
            for index, club in enumerate(clubs, start=1):
                print(f"{index}. {club.name}")
            club_choice = int(input("Enter club choice: "))
            member_type = input("Enter member type (Single/Multi): ").lower()
            if member_type == "single":
                members.append(Single_Club_Member(member_id, name, clubs[club_choice]))
            elif member_type == "multi":
                members.append(MultiClubMember(member_id, name))
            else:
                print("error")
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