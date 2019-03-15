	"""Copy this code inside the binarysearch.py file"""
	def remove(self, data):
		# empty tree
		if self.root is None:
			return False
			
		# data is in root node	
		elif self.root.value == data:
			# if root has no children
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			# if root has only left child
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			# if root has only right child
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			# if root has both the child	
			elif self.root.leftChild and self.root.rightChild:
				# making two separate variables so that we can assign 
				# delNodeparent.left or delNodeparent.right to delNode.left or delNode.right 
				delNodeParent = self.root
				#why is it assigning root.rightChild in the begining 
				# because by taking leftest child from right child will maintain the BST property 
				# i.e leftChild < root < rightChild
				delNode = self.root.rightChild
				
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild
				# assigned value of leftest child to root node
				self.root.value = delNode.value
				
				# here we are rearranging the tree as per BST properties 
				# also we travelled till the leftest child of right tree it can not have 
				# left child as per above while loop but it can have right child thats what we are checking here				
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild
				else:
					# if it was the last node just set it to none
					# this condition is checking only two child possiblity or 
					# if root.right.left has two child case
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None
						
			return True
		
		parent = None
		node = self.root
		
		# find node to remove
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild
		
		# case 1: data not found
		if node is None or node.value != data:
			return False
			
		# case 2: remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		# case 3: remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		# case 4: remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		# case 5: remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None
