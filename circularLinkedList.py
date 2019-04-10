class Node:
    def __init__(self,data):
        self.data = data
class CircularList:
    def __init__(self):
        self.head = None

    def len(self):
        curr = self.head
        count = 0
        while curr:
            count +=1
            curr = curr.next
            if curr == self.head:
                break
        return count



    def append(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def prepend(self,data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head

        if self.head == None:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    def show_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

    def remove_node(self,key):

        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next

        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr =curr.next
                if curr.data == key:
                    prev.next = curr.next
                    curr = curr.next

    def remove_node_bynode(self,node):

        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next

        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr =curr.next
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next


    def josephus_circle(self,step):
        curr = self.head
        while self.len() != 1:
            count = 1
            while count != step:
                curr = curr.next
                count = count +1
            self.remove_node_bynode(curr)
            curr = curr.next

    def is_circular(self):
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr == self.head:
                return True
        return False



clist = CircularList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.prepend(4)
# clist.remove_node_bynode(clist.head)
# clist.append(4)
# clist.show_list()
# # print(clist.len())
# print("\n")
# clist.josephus_circle(2)
# clist.show_list()
print(clist.is_circular())