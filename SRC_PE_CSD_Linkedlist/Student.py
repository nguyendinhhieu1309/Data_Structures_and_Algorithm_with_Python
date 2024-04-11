class Student:
    def __init__(self, id = "", name = "", address = "", score = -1):
        self.Id = id
        self.Name = name
        self.Address = address
        self.Score = score
    def __repr__(self):
        return f"({self.Id}, {self.Name}, {self.Address}, {self.Score})"
