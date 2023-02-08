# Function to display hashtable
def display_hash(hashTable):
	
	for i in range(len(hashTable)):
		print(i, end = " ")
		
		for j in hashTable[i]:
			print("-->", end = " ")
			print(j, end = " ")
			
		print()

# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(10)]

# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
	return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].append(value)

def delete(Hashtable,keyvalue,value):
  hash_key = Hashing(keyvalue)
  try :
    Hashtable[hash_key].remove(value)
  except:
    print(value + " Not present in dictionary")

#   Main 
print("***\t MENU \t***\n1.Insert\n2.Delete\n3.Display\n4.Exit")
choice = int(input("Enter your choice : "))
while choice != 4:
  if choice == 1:
    value = input("Enter the element to insert : ")
    hashkey = len(value) % 10
    insert(HashTable, hashkey , value)
  
  elif choice == 2:
    value = input("Enter element to delete : ")
    hashkey = len(value)
    delete(HashTable , hashkey ,value)

  elif choice == 3:
    display_hash(HashTable)
  
  else:
    print("Choose from the given choices only")
    print("***\t MENU \t***\n1.Insert\n2.Delete\n3.Display\n4.Exit")
  choice = int(input("Enter your choice : "))
