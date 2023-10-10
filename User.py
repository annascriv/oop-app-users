# your User class goes here

class Users: 

    def __init__(self,name,email,dil):
        self.name=name
        self.email=email
        self.dil= dil

    def __str__(self):
        return f"{self.name}'s email is {self.email} and their driver's license number is {self.dil}."
    
    def share(self):
        print(f"")

emily = Users("Emily","ehk@gmail.com", 123456789)
print(emily)