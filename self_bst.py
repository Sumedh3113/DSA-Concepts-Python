class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root:
            return self.insert_new(self.root, new_val)
            
            
                
    def insert_new(self, start, new_val):
        if start.value > new_val:
            if start.left:
                self.insert_new(start.left, new_val)
            else:
                # if we do not put else here then this line always get 
                # executed after if but we want it to execute after if becomes false
                # also if we return self.insert_new(start.left, new_val) 
                #it would not become a prb but here we need else we cant just return any value
                start.left =  Node(new_val)
        else:
            if start.right:
                self.insert_new(start.right, new_val)
            else:
                start.right =  Node(new_val)     
        
    def search(self, find_val):
        if self.root:
            return self.search_new(self.root, find_val)
    
    def search_new(self,start, find_val):
        if start.value == find_val:
            return True
        else:
            if start.value > find_val:
			
			    self.search_new(start.left,find_val)
            else:
                if start.right:
                    self.search_new(start.right, find_val)
        # here we can directly write return false without else as our if is returning the value
        # which is not the case with insert_new() if condition
        return False
            
    
    def print_tree(self):
        # here [:-1] is used to slice last appended character "-"
        return self.preorder_print(self.root, "")[:-1]
    
    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())
# Check search
# Should be True
print(tree.search(2))
# Should be False
print(tree.search(1))