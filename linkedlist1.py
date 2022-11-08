class Student:
    def __init__(self,name,ID,color,next=None):
        self.name = name
        self.ID = ID
        self.color = color
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,name,ID,color):
        newStudent = Student(name,ID,color)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newStudent
        else:
            self.head = newStudent
            
    def printList(self):
        current = self.head
        while current:
            print("Student name:",current.name,", ID:", current.ID,", fav color", current.color)
            current = current.next
    def amount(self):
        current = self.head
        a = 0
        while current:
            a +=1
            current = current.next
        print(a)

    def search(self):
        current = self.head
        name = input("what person are you looking for\n")
        while current:
            if current.name == name:
                print("I have found the person")
                return True
            elif current.name != name:
                current = current.next
        print("person was not found")

StudentLine = LinkedList()
num = int(input("how many people would you like to add"))
for i in range(num):
    name = input("what is their name\n")
    number = int(input("what is their number\n"))
    color = input("what color do they like\n")
    StudentLine.insert(name,number,color)


StudentLine.printList()
StudentLine.search()
