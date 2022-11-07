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

StudentLine = LinkedList()

StudentLine.insert("lily",456987,"blue")

StudentLine.insert("kevin",123987,"blue")

StudentLine.insert("sebastian",4,"blue")

StudentLine.insert("jesse",4587,"blue")

StudentLine.insert("lukas",1987,"blue")

StudentLine.insert("simon",546,"blue")

LinkedList.printList(StudentLine)
