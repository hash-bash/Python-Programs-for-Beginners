class Flower:
    color = 'unknown'


rose = Flower()
rose.color = "Red"
violet = Flower()
violet.color = "Blue"
this_pun_is_for_you = "This pun is for you."
print("Roses are {},".format(rose.color))
print("Violets are {},".format(violet.color))
print(this_pun_is_for_you)


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())


class Person:
    name = ""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "You just called __str__ method."

    def greeting(self):
        """Returns Greeting Text."""
        return "hi, my name is " + self.name + "."


some_person = Person("Cool Dude")
print(some_person.greeting())
print(some_person)


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
