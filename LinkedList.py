class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        if temp == None:
            print("Linked list is empty.")
            return
        else:
            print("\nLinked list is as following")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

    def add(self, data):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def delete(self, data):
        temp = self.head
        prev = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                return
            else:
                while temp.next.data != data:
                    temp = temp.next
                if temp.next.next is not None:
                    prev = temp
                    print(prev.data)
                    temp = temp.next
                    prev.next = temp.next
                else:
                    temp.next = None
                
    def search(self, data):
        temp = self.head
        flag=0
        while temp is not None:
            if temp.data == data:
                print("Item found")
                flag=1
                break
            temp = temp.next
        if flag==0:
            print("Item not found")
        


if __name__=="__main__":
    ll = Linkedlist()
    while True:
        print("\n1. Add element")
        print("2. Delete element")
        print("3. Traverse")
        print("4. Search")
        print("5. Exit")
        choice = int(input("\nEnter your choice : "))
        if choice==1:
            if ll.head==None:
                val = int(input("Enter value to be added : "))
                ll.head = Node(val)
            else:
                val = int(input("Enter value to be added : "))
                ll.add(val)
                
        elif choice==2:
            if ll.head == None:
                print("Linked list is empty")
            else:
                val = int(input("Enter the value to be deleted : "))
                ll.delete(val)
            
        elif choice==3:
            ll.traverse()

        elif choice==4:
            if ll.head == None:
                print("Linked list is empty")
            else:
                val = int(input())
                ll.search(val)

        elif choice==5:
            break

        else:
            print("Wrong choice")
            
        
