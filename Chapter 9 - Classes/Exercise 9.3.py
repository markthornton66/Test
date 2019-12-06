class User():
    """creates a class about a user"""
    def __init__(self,first_name,last_name,age,gender):
        """initializes description of a user"""
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):

        print(f"My first name is {self.fname}")
        print(f"\nMy last name is {self.lname}")
        print(f"\nI am {self.age} years old")
        print(f"\nI am a {self.gender}")

    def greet_user(self):
        """greets a user by their name"""
        full_name = "{self.fname} + {self.lname}"
        print(f"Hello {full_name}, Welcome!!!")

mark = User('Mark','Thornton',26,'male')
mark.describe_user()
mark.greet_user()