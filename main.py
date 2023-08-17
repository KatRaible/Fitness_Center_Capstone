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
        print()

        choice = int(input("Enter your choice: "))
        print()

        if choice == 1: 
            member_id = input("Enter Member ID: ")
            name = input("Enter member name: ")
            print("Select club for the member:")
            for index, club in enumerate(clubs, start=1):
                print(f"{index}. {club.name}")
            club_choice = int(input("Enter club choice: "))
            club_choice = club_choice - 1
            member_type = input("Enter member type (Single/Multi): ").lower()
            if member_type == "single":
                members.append(Single_Club_Member(member_id, name, clubs[club_choice]))
            elif member_type == "multi":
                members.append(MultiClubMember(member_id, name))
            else:
                print("error")
            print()
        elif choice == 2:  # remove member
            member_id = input("Enter member ID to remove: ")
            #print(len(members))
            for member in members:
                if member_id == member.member_id:
                    members.remove(member)
                    print("Member removed.")
                    break
            else:
                print("Member not found.")
            print()
        elif choice == 3:  # display member info
            member_id = input("\nEnter member ID to display info: ")
            for member in members:
                if member.member_id == member_id:
                    print(f"Member ID: {member.member_id}")
                    print(f"Member Name: {member.name}")
                    if isinstance(member, Single_Club_Member):
                        print(f"Club: {member.club.name}")
                    elif isinstance(member, MultiClubMember):
                        print(f"Membership Points: {member.membership_points}")
                    break
            else:
                print("Member not found.")
            print()
        elif choice == 4: #check in member
            member_id = input("Enter member ID to check in: ")
            for member in members:
                if member.member_id == member_id:
                    if isinstance(member, Single_Club_Member):
                        member.club.check_in_member(member)
                        print(f"Member {member.name} checked in at {member.club.name}")
                    elif isinstance(member, MultiClubMember):
                        print("Multi Club Members cannot be checked in individually. ")
                    break
            else:
                print("Member not found or ineligible for check-in.")  
            print()          
        elif choice == 5: #generate bill
            member_id = input("Enter Member ID to generate bill: ")
            billed_member =  None
            for member in members:
                if member.member_id == member_id:
                    billed_member = member
                    break
            if billed_member: 
                print("Bill")
                if MultiClubMember:
                    print("$60")
                else: 
                    print("$50")
            else: 
                print("Member not found or ineligible for check-in.")
            print()
        elif choice == 6: #exit
            print("Exiting  ")
            break
        else: 
            print("Invalid choice. Please select again.")
        print()

if __name__== "__main__":
    main()