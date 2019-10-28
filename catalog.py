class Item:
    def __init__(self, movie = "", category = ""):
        self.__name = movie
        self.__category = category

    def set_name(self, name = ""):
        self.__name = name
    
    def set_category(self, category =""):
        self.__category = category

    def __str__(self):
        print()
        return "Name: {}, Category: {}".format(self.__name, self.__category)


class Catalog:
    def __init__(self, name, collection = []):
        self.__name = name
        self.__collection = collection

    def add(self, item):
        self.__collection.append(str(item))

    def remove(self, item):
        self.__collection.remove(str(item))

    def set_name(self, name = ""):
        self.__name = name

    def clear(self):
        self.__collection = ""

    #def find_item_by_name(self, name):


    def __str__(self):
        return "Catalog {}: {}".format(self.__name, self.__collection)



item1 = Item("Green Book", "Biography")
print(item1)

item2 = Item("The God", "Crime")
print(item2)
item2.set_name("The Godfather")
print(item2)

item3 = Item("Schindler's List", "Biography")
print(item3)
item3.set_category("Drama")
print(item3)

catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
print(catalog)

catalog.remove(item2)
print(catalog)

catalog.set_name("Favorite Movies")
print(catalog)

#print(catalog.find_item_by_name("Green Book"))
#print(catalog.find_item_by_name("The Godfather"))

catalog.clear()
print(catalog)