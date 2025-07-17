'''
write code to remove duplicates from an unsorted linkedlist
followup:
how would you solve this problem is a temporary buffer is not allowed

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
def remove_duplicate(ll):
    '''
    time_complexity = O(n)
    space_complexity = O(n)
    '''
    if ll.head == None and ll.tail == None:
        return None
    seen = set()
    current = ll.head
    seen.add(current)
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return seen

linked_list = Linked_List(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(1)
linked_list.append(4)
linked_list.append(0)
linked_list.append(6)

result = remove_duplicate(linked_list)
print(result)

############################ FOLLOW UP ######################
def remove_duplicate_2(ll):
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next= runner.next.next
            else:
                runner = runner.next
        current = current.next
    return ll

linked_list_2 = Linked_List(0)
linked_list_2.append(1)
linked_list_2.append(2)
linked_list_2.append(1)
linked_list_2.append(4)
linked_list_2.append(0)
linked_list_2.append(6)

result = remove_duplicate_2(linked_list_2)
print(result)

