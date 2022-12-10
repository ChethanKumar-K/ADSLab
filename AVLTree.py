import sys
class TreeNode(object):
    def __init__(self,key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree(object):
    def insertNode(self,root,key):

        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insertNode(root.left,key)
        else:
            root.right = self.insertNode(root.right,key)

        #   Updating the height of the nodes
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        #   Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        
        if balanceFactor > 1:
            #   left-left problem
            if key < root.left.key:
                return self.rightRotate(root)
            #   right-left problem
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            #   right-right problem
            if key > root.right.key:
                return self.leftRotate(root)
            #   left-right problem
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
    
    def delNode(self,root,key):
        if not root:
            return
        elif key < root.key:
            root.left = self.delNode(root.left,key)
        elif key > root.key:
            root.right = self.delNode(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValue(root.right)
            root.key = temp.key
            root.right = self.delNode(root.right,temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            #   left - left
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            #   right - left
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            #   right - right
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            #   left - right
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root

    #   Function for left rotation
    def leftRotate(self,root):
        temp = root.right
        temp2 = temp.left
        temp.left = root
        root.right = temp2
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        temp.height = 1 + max(self.getHeight(temp.left),self.getHeight(temp.right))
        return temp
    
    #   Function for right rotation
    def rightRotate(self,root):
        temp = root.left
        temp2= temp.right
        temp.right = root
        root.left = temp2
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        temp.height = 1 + max(self.getHeight(temp.left),self.getHeight(temp.right))
        return temp

    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self,root):
        if not root:
            return 
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValue(self,root):
        if root is None or root.left is None:
            return root
        return self.getMinValue(root.left)

    def inOrder(self,root):
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.key),end = " ")
        self.inOrder(root.right)
    
    def printHelper(self,currPtr,indent,last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R---")
                indent +=   "   "
            else:
                sys.stdout.write("L---")
                indent +=   "|  "
            print(currPtr.key)
            self.printHelper(currPtr.left,indent,False)
            self.printHelper(currPtr.right,indent,True)


myTree = AVLTree()
root = None
print("Choices \n1.Insert \n2.Delete \n3.Print Tree \n4.Print Inorder Traversal\n5.Exit")
choice = int(input("Enter your choice : "))
while(choice != 5):
    if choice == 1:
        elem = int(input("Enter the element to be inserted : "))
        root = myTree.insertNode(root,elem)
    elif choice == 4:
        print("The Inorder Traversal is ")
        myTree.inOrder(root)
        print()
    elif choice == 2:
        elem = int(input("Enter the element to delete : "))
        root =  myTree.delNode(root,elem)
        if root is None:
            print("Element is not the tree")
    elif choice == 3:
        myTree.printHelper(root,"",True)
    else:
        print("Please enter a valid choice")
    choice = int(input("Enter your choice : "))
    
    
#   OUTPUT
# Choices 
# 1.Insert 
# 2.Delete 
# 3.Print Tree 
# 4.Print Inorder Traversal
# 5.Exit
# Enter your choice : 1
# Enter the element to be inserted : 20
# Enter your choice : 1
# Enter the element to be inserted : 5
# Enter your choice : 1
# Enter the element to be inserted : 75
# Enter your choice : 1
# Enter the element to be inserted : 33
# Enter your choice : 1
# Enter the element to be inserted : 89
# Enter your choice : 3
# R---20      
#    L---5    
#    R---75   
#       L---33
#       R---89
# Enter your choice : 1
# Enter the element to be inserted : 90
# Enter your choice : 3
# R---75
#    L---20
#    |  L---5
#    |  R---33
#    R---89
#       R---90
# Enter your choice : 2
# Enter the element to delete : 5
# Enter your choice : 3
# R---75
#    L---20
#    |  R---33
#    R---89
#       R---90
# Enter your choice : 5
