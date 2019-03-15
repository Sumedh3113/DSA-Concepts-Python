lass Node:
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insert(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				# here we are directly using self.leftChild as we are in Node class
				# in Tree class we need to use self.root.leftChild
				self.leftChild = Node(data)
				#base condition for return
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True
				
	def find(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False
				
	def getHeight(self):
		if self.leftChild and self.rightChild:
			# here 1 will be added to leftChild in every call same with rightChild 
			# In the end will return max value from the two
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

	def preorder(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value))

	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print (str(self.value))
			if self.rightChild:
				self.rightChild.inorder()

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			#here by doing self.root = Node(data) we are making self.root object of Node class
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False
			
	def getHeight(self):
		if self.root:
			return self.root.getHeight()
		else:
			return -1
	
	def preorder(self):
		if self.root is not None:
			print("PreOrder")
			self.root.preorder()
		
	def postorder(self):
		if self.root is not None:
			print("PostOrder")
			self.root.postorder()
			
	def inorder(self):
		if self.root is not None:
			print("InOrder")
			self.root.inorder()

bst = Tree()
print(bst.insert(10))
#print(bst.insert(5))
bst.preorder()
print(bst.getHeight())
#bst.postorder()
#bst.inorder()
print(bst.remove(10))
bst.preorder()