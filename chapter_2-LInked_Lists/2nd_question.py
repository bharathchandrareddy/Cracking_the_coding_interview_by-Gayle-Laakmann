'''
Implement and algorithm to find the kth to last element of a single linked list
'''
class Node():
    def __init__(self,value):
        
        self.value = value
        self.next = None

class Linked_List():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

def find_k_from_last(ll,k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow

linked_list = Linked_List(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

print(find_k_from_last(linked_list,5).value)
        

