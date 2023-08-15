class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address



class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def check_in(self, club):
        pass


class Single_Club_Member(Member):
    def __init__(self, member_id, name, club):
        super().__init__(member_id, name)
        self.club = club


    def check_in(self, club):
        if club == self.club:
            print("Checked in!")
            ##print a response here
            ##need to add membership points
        else:
            print("Sorry, your current membership doesn't allow access to this location.")

class MultiClubMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.membership_points = 0

    def check_in(self, club):
        self.membership_points += 1
        print(f"Checked in to {club.name}. Membership points: {self.membership_points}")