import time
import fontstyle 
class Person:
    def __init__(self, fname:str, lname:str,dob:list):
        self.firstName = fname
        self.lastName = lname
        self.dob = dob

    def print(self):
        print(self.firstName)

    def printAge():
        pass


# mehendi = Person("Mehendi","hasan",[27,2,2004])
# mehendi.print()


class Restaurant:
    def __init__(self,name=None, address=None,tables_no=10):
        self.name = name
        self.address = address
        self.menu_items = {}
        self.tables = {}
        for i in range(1,tables_no,1):
            self.tables[i] = "Available"

    def add_menu_items(self, *args, **kargs):
        for i in args:
            self.menu_items[i[0]] = i[1]

    def show_menu(self):
        if (self.name):
            print(fontstyle.apply("\n\t" +self.name +"\n\tMenu Card\n",'bold/Italic/red/GREEN_BG'))
        else:
            print(fontstyle.apply("\n\tRestaurant" +"\n\tMenu Card", 'bold/Italic/red/GREEN_BG'))
        print("Item\t\tPrice")
        for i,j in self.menu_items.items():
            print(i,"\t\t",j)


    def book_table(self,table_no=None):
        if(table_no):
            if(self.tables[table_no] == "Reserved" or table_no not in self.tables):
                print("Table not available")
            else:
                self.tables[table_no] = "Reserved"
                return

        for i,j in self.tables.items():
            print(i,"\t\t",j)
        ask = int(input("Enter Table Number to be booked: "))
        if(self.tables[ask] == "Reserved" or ask not in self.tables):
                print("Table not available")
                return
        self.tables[ask] = "Reserved"
    
    def show_tables(self):
        for i,j in self.tables.items():
            print(i,"\t\t",j)

res1 = Restaurant("Hulululu", "Malka Ganj")
res1.add_menu_items(["Ganja",200])
res1.add_menu_items(["Sweety Supari", 5],["Rosgulla",799],['Gulab Jamun',100])
res1.show_menu()
res1.book_table()
res1.book_table(2)
res1.show_tables()