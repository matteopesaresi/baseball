from dataclasses import dataclass


@dataclass
class Team:
    ID : int
    year : int
    teamCode : int
    divID : str
    div_ID : int
    teamRank : int
    name : str

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return f"{self.ID} : {self.name}"
