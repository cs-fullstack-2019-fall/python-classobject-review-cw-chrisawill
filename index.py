# ## Problem 1:

# class movie:
#     def __init__(self, movieName, rating, yearReleased):
#         self.movieName = movieName
#         self.rating = rating
#         self.yearReleased = yearReleased
#
#     def conjunctionjunction(self):
#         print(f"My favorite movie is {self.movieName}. It was released in {self.yearReleased} with a {self.rating}")
#
#     def __str__(self):
#         print("This movie was a box-office hit")
#
# film = movie("School House Rock", "100%", "2015")
# print(film.conjunctionjunction())


# ### Problem 2:
# Create a class Product that represents a product sold online.
#
# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
#
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.

class Product:
    def __init__(self, price, quantity, name):
        self.price = price
        self.quantity = quantity
        self.name = name

    def changep(self):
        self.price = "9.00"
        print(f"Todays special is {self.name}. it is {self.price} and you can get {self.quantity}")

    def __str__(self):
        print('The special for today')

item = Product("$100", "5", "f0rK")

print(item.changep())
