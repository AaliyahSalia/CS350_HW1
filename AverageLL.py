class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def Average_List(self):
        current = self.head.next  # Start with the first node after 'Head'
        sum = 0
        count = 0
        while current:
            sum += int(current.value)
            count += 1
            current = current.next
        return sum/count

linked_list = LinkedList(Node("Head", Node(1, Node(2, Node(3)))))
average = linked_list.Average_List()
print(average)
