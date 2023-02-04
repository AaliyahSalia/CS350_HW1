class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append(head, new_data):
    new_node = Node(new_data)
    if head is None:
        head = new_node
        return head
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def Delete_Linked_List_Node(head, key):
    temp = head
    prev = None
    
    while (temp != None and temp.data == key):
        head = temp.next 
        temp = head

    while (temp != None):

        while (temp != None and temp.data != key):
            prev = temp
            temp = temp.next

        if (temp == None):
            return head
        
        prev.next = temp.next

        temp = prev.next
    return head

def printList(node):
    while (node != None):
        print(node.data, end = " ")
        node = node.next

if __name__=='__main__':

    head = None

    head = append(head, 1)
    head = append(head, 2)
    head = append(head, 1)
    head = append(head, 3)
    

    key = 1

    print("\nCreated Linked List: ")
    printList(head)

    head = Delete_Linked_List_Node(head, key)
    print("\nLinked List after Deletion is: ")

    printList(head)
