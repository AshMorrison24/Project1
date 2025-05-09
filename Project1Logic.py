import csv
import os

class Voting:
    def __init__(self, filename='votes.csv'):
       self.filename = filename
    def voter_valid(self,voter_id: int):
       """This function checks whether a voter is valid."""
       if voter_id.isdigit() is False:
           return False, "Voter ID must be a 9 digit number"
       elif len(voter_id) != 9:
           return False, "Voter ID must be a 9 digit number"
       return True, ""

    def check_vote(self,voter_id: int):
        """This function checks whether a voter has voted or not."""
        if os.path.isfile(self.filename) is False:
            return True, ""
        with open('votes.csv',  'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if voter_id == row[0]:
                    return False, "Voted already"
        return True, ""


    def append_id(self,voter_id: int, candidate: str):
        """This function appends the voter ID and chosen candidate."""
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([voter_id, candidate])
