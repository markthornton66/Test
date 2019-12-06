# this is exercise 9.2

class Restaurant():
    """this creates a class which describes a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializes the description of a particular restaurant"""
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"My favourite restaurant is {self.restaurant}. My favourite type of food is {self.cuisine}")

    def open_restaurant(self):
        """displays a message that describes when a restaurant is open"""
        print("This restaurant is now open")


restaurant = Restaurant('Oasis', 'Italian')
restaurant_two = Restaurant('Hillbillies', 'European')
restaurant_three = Restaurant('Tung Sing', 'Chinese')

restaurant.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()
