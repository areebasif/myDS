class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        prev_node = self.head
        while prev_node.next:
            prev_node = prev_node.next
        prev_node.next = new_node

    def printlist(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


    def remove_node(self,key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node.next = None
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            print("not found")
            return
        prev.next = curr_node.next
        curr_node = None

    def remove_node_by_index(self,idx):
        curr_node = self.head
        if idx == 0:
            self.head = curr_node.next
            curr_node = None
            return
        count = 0
        prev = None

        while count != idx and curr_node:
            prev_node = curr_node
            curr_node = curr_node.next
            count = count+1
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None


    def iterative_length(self):
        count = 0
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
            count = count+1
        return count

    def recursive_length(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_length(node.next)



    # def swap_nodes(self,key1,key2):
    #     if key1 ==key2:
    #         return
    #     prev1 = None
    #     curr_node1 = self.head
    #     while curr_node1 and curr_node1.data != key1:
    #         prev1 = curr_node1
    #         curr_node1 = curr_node1.next
    #
    #     prev2 = None
    #     curr_node2 = self.head
    #     while curr_node2 and curr_node2.data != key2:
    #         prev2 = curr_node2
    #         curr_node2 = curr_node2.next
    #
    #     if not curr_node1 or not curr_node2:
    #         return
    #     if prev1:
    #         prev1.next = curr_node2
    #     else:
    #         self.head = curr_node2
    #     if prev2:
    #         prev2.next = curr_node1
    #     else:
    #         self.head = curr_node1
    #
    #     curr_node1.next, curr_node2.next = curr_node2.next, curr_node1.next

    def swap_node(self,key1,key2):
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data!=key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next


        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        if prev2:
            prev2.next = curr1
        else:
            self.heaf = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_list_iterative(self):
        curr = self.head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    def reverse_list_recursive(self):
        def reverse_list_recursive(prev,curr):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return reverse_list_recursive(prev,curr)
        self.head = reverse_list_recursive(prev = None,curr = self.head)


    def merge_linked_list(self,llist):
        p = self.head
        q = llist.head
        s=None

        if not p:
            return q
        if not q:
            return p

        if p and q:

            if p.data > q.data:
                s = q
                q = s.next
            else:
                s = p
                p = s.next

            new_head = s

            while p and q:
                if q.data  > p.data:
                    s.next = p
                    s = p
                    p = s.next

                else:
                    s.next = q
                    s = q
                    q = s.next

            if not p:
                s.next = q
            if not q:
                s.next =  p

            return new_head


    def remove_duplicates(self):
        my_dict = {}
        curr = self.head
        prev = None
        if not curr:
            return
        if prev is None:
            prev = curr
            my_dict[curr.data] = 1
            curr = curr.next

        # else:

        while curr:

            if curr.data in my_dict:
                prev.next = curr.next
                curr = None
            else:
                my_dict[curr.data] = 1
                print(my_dict)
                prev = curr
            curr = prev.next

    



































class stack:
    def __init__(self):
        self.items =[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def is_peek(self):
        return self.items[-1]
    def get_stack(self):
        return self.items

def reverse_str(input_str):
     s = stack()
     out_str = ''
     for i in input_str:
         s.push(i)
     while not s.is_empty():
        out_str = out_str + s.pop()
     return out_str


























# llist = LinkedList()
# llist.append('a')
# llist.append('b')
# llist.append('c')
# # llist.printlist()
# # llist.remove_node('a')
# # llist.printlist()
# llist.printlist()
# # llist.remove_node_by_index(1)
# # llist.printlist()
# print(llist.iterative_length())
# print(llist.recursive_length(llist.head))
# print(reverse_str("areeb"))
# llist.printlist()
# # llist.swap_node('b','c')
# llist.printlist()
# llist.reverse_list_recursive()
# llist.printlist()
llist = LinkedList()
llist1 = LinkedList()
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(6)
llist.append(8)
# llist.printlist()
# print("\n")
# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.printlist()
# llist1.merge_linked_list(llist)
# llist.merge_linked_list(llist1)
# print("\n")
# llist.printlist()
# print("\n")
# llist1.merge_linked_list(llist)
llist.append(2)
llist.append(3)
llist.printlist()
print("\n")
llist.remove_duplicates()
llist.printlist()