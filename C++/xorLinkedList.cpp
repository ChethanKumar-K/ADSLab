
// efficient Doubly Linked List

// Importing libraries
#include <bits/stdc++.h>
#include <cinttypes>

using namespace std;

// Class 1
// Helper class(Node structure)
class Node {
	public : int data;
	// Xor of next node and previous node
	Node* xnode;
};

// Method 1
// It returns Xored value of the node addresses
Node* Xor(Node* x, Node* y)
{
	return reinterpret_cast<Node*>(
		reinterpret_cast<uintptr_t>(x)
		^ reinterpret_cast<uintptr_t>(y));
}

// Method 2
// Insert a node at the start of the Xored LinkedList and
// mark the newly inserted node as head
void insert(Node** head_ref, int data)
{
	// Allocate memory for new node
	Node* new_node = new Node();
	new_node -> data = data;

	// Since new node is inserted at the
	// start , xnode of new node will always be
	// Xor of current head and NULL
	new_node -> xnode = *head_ref;

	// If linkedlist is not empty, then xnode of
	// present head node will be Xor of new node
	// and node next to current head */
	if (*head_ref != NULL) {
		// *(head_ref)->xnode is Xor of (NULL and next).
		// If we Xor Null with next we get next
		(*head_ref)
			-> xnode = Xor(new_node, (*head_ref) -> xnode);
	}

	// Change head
	*head_ref = new_node;
}

// Method 3
// It simply prints contents of doubly linked
// list in forward direction
void printList(Node* head)
{
	Node* curr = head;
	Node* prev = NULL;
	Node* next;

	cout << "The nodes of Linked List are: \n";

	// Till condition holds true
	while (curr != NULL) {
		// print current node
		cout << curr -> data << " ";

		// get address of next node: curr->xnode is
		// next^prev, so curr->xnode^prev will be
		// next^prev^prev which is next
		next = Xor(prev, curr -> xnode);

		// update prev and curr for next iteration
		prev = curr;
		curr = next;
	}
	cout << "\n";
}

int deletion(Node ** head_ref){
    int value;
    Node *temp;
    if(*head_ref == NULL){
        cout << "The list is empty\n";
        return -1;
    }
    else if((*head_ref) -> xnode == NULL){
        value = (*head_ref)->data;
        *head_ref = NULL;    
        return value; 
    }
    else{
        value = (*head_ref)->data;
        temp = (*head_ref);
        *head_ref = (*head_ref) -> xnode;
        (*head_ref)->xnode = Xor(temp,(*head_ref)->xnode);
        return value;
    }
    
}

// Method 4
// main driver method
int main()
{
	Node* head = NULL;
	int choice ;
	int val;
	
	cout << "Choices \n 1.Insert \n 2.Delete \n 3.Print \n 4.Exit\n";
	cout << "Enter your choice : ";
	cin >> choice;
	while(choice != 4){
	    switch(choice){
	        case 1:
	            cout << "Enter the element to be inserted ";
	            cin >> val;
	            insert(&head,val);
	            break;
	       case 2:
	            val = deletion(&head);
	            cout << "The deleted element is "<<val<<"\n";
	            break;
	       case 3:
	            printList(head);
	            break;
	    }
	    cout << "Enter your choice : ";
	    cin >> choice;
	}
	// Printing the created list
	
	printList(head);

	return (0);
}
