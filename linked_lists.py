class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    # Append an element in list
    def append(self, data):
        cur = self.head
        new_node = node(data)
        while (cur.next != None):
            cur = cur.next
        cur.next = new_node

    # Length of linked list
    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        print(count)

    # insert at the beginning
    def insertBegin(self, data):
        new_node = node(data)
        cur = self.head
        new_node.next = cur.next
        cur.next = new_node

    # insert at nth pos
    def insertnth(self, data, n):
        temp = self.head
        new_node = node(data)
        while (n > 0):
            temp = temp.next
            n -= 1
        new_node.next = temp.next
        temp.next = new_node

    # insert at mid
    def insertmid(self, data):
        cur = self.head
        cur1 = self.head
        new_node = node(data)
        while (cur != None):
            cur = cur.next
            cur = cur.next
            cur1 = cur1.next
        new_node.next = cur1.next
        cur1.next = new_node

    # search the linked list
    head1 = node()

    def itersearch(self, k):
        cur = self.head
        flag = 0
        count = 0
        while cur.next != None:
            cur = cur.next
            count+=1
            if cur.data == k:
                flag = count
        return flag

    # delete a node at a give position
    def deletenode(self, position):
        cur = self.head
        if position == 0:
            self.head = cur.next
            cur = None
            return
        while cur.next != None and position > 1:
            cur = cur.next
            position -= 1

        next1 = cur.next.next

        cur.next = None
        cur.next = next1

    # Display the linked list
    def display(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data, end=" ")
        print()


my_ll = linked_list()
my_ll.append(10)
my_ll.display()
my_ll.append(12)
my_ll.display()

my_ll.append(23)
my_ll.display()

my_ll.append(34)
my_ll.display()

my_ll.append(56)
my_ll.display()

my_ll.insertmid(42069)
my_ll.display()

my_ll.insertBegin(100)
my_ll.display()

my_ll.insertBegin(200)
my_ll.display()

my_ll.insertBegin('pranav')
my_ll.display()

my_ll.insertnth('sawant', 3)
my_ll.display()

my_ll.insertnth(1000, 6)
my_ll.display()

my_ll.insertmid('ex')
my_ll.display()

my_ll.length()
my_ll.display()
print()
my_ll.deletenode(4)
print("hi")
my_ll.display()
print(my_ll.itersearch('pranav'))
