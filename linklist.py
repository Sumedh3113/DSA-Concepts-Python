class Element(object):
	"creating the node"
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    "head will point to the first element "
    def __init__(self, head=None):
        self.head = head
	"Rest of the elements are added this way"
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        
        current = self.head
        if self.head:
            x = 1
            while x:
                if x == position:
                    return current
                else:
                    current = current.next
                    #return current.value
                x = x + 1
        else:
            
            return None
        
    def insert(self, new_element, position):
        current = self.head
        if self.head:
            x = 1
            while x:
                if x == position-1:
                    new_element.next = current.next
                    current.next = new_element
                    break
                    
                elif position == 1:
                    new_element = self.head
                    self.head = new_element
                    break
                current = current.next
                x = x + 1
                
        
    def delete(self, value):
            """Delete the first node with a given value."""
            current = self.head
            #previous = current
            previous = None
            if self.head:
                while current.next and current.value != value:
                    previous = current
                    current = current.next
                                            
                if current.value == value:
                    if previous:
                        previous.next = current.next
                    else:
                        self.head = current.next

                            

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
#print(ll.head.next.next.value)
# Should also print 3
#print(ll.get_position(1).value)
#print(ll.get_position(2).value)
#print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
#print("----")
#print(ll.get_position(1).value)
#print(ll.get_position(2).value)
#print(ll.get_position(3).value)


# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
#print(ll.get_position(2).value)
#print(ll.get_position(3).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)