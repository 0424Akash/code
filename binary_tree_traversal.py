# A class that represents an individual node in a Binary Tree 
class Node: 
	def __init__(self, val = 0 ,left = None, right = None): 
		self.left = left
		self.right = right
		self.val = val 


# inorder tree traversal 
def printInorder(root): 
	if root:  
		return printInorder(root.left) + [root.val] + printInorder(root.right)
	else:
		return []


# postorder tree traversal 
def printPostorder(root): 
	if root:  
		return printPostorder(root.left) + printPostorder(root.right) + [root.val]
	else:
		return []


# preorder tree traversal 
def printPreorder(root): 
	if root: 
		return [root.val] + printPreorder(root.left) + printPreorder(root.right)
	else:
		return []


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.right.left = Node(6)
print ("Preorder traversal of binary tree is")
print(printPreorder(root)) 

print ("\nInorder traversal of binary tree is")
print(printInorder(root))

print ("\nPostorder traversal of binary tree is")
print(printPostorder(root))
