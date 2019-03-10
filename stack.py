
class Element(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current = self.head
        if self.head:
            self.head = new_element
            new_element.next = current
		"if it is empty stack "
        else:
            self.head = new_element
        
        

    def delete_first(self):
        current = self.head
        if self.head:
            self.head =  current.next
            return current
        #return None
        #current = None
        
    def display(self):
        current = self.head
        while current:
            print(current.value,sep='->', end='->')
            current = current.next
            
class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        x = self.ll.delete_first()
        return x   

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#ll = LinkedList(e1)
# Start setting up a Stack
stack = Stack(e1)

stack.push(e2)
stack.push(e3)

#ll.display()
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())

stack.push(e4)

print(stack.pop().value)
