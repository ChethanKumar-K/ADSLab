#include <iostream>
#include <bits/stdc++.h>
#include <cinttypes>

using namespace std;

class Node{
    public : int data;
    //  XOR of previous address and next address
    Node* xnode;
};

// Method 1 
// Returns the xor value of the node addresses
Node * Xor(Node* x, Node* y){
    return reinterpret_cast<Node*>(reinterpret_cast<uintptr_t>(x) ^
    reinterpret_cast<uintptr_t>(y));
}

//insert a node at the start of the list
void insert(Node** head_ref,int data){
    // allocate memory for the newnode
    Node * newnode = new Node();
    newnode->data = data;
    
    //  since newnode is inserted at the beginning 
    //  xnode value is xor of 0 and the head_ref
    newnode->xnode = *head_ref;
    
    //  if linked list is not empty, then xnode of 
    //  present head will be Xor of newnode
    //  and node next to current head
    
    if(*head_ref != NULL){
        (*head_ref)->xnode = Xor(newnode,(*head_ref)->xnode);
    }
    
    //  change head
    *head_ref = newnode;
}

//  method 3
//  print the list

void printList(Node *head){
    Node* curr = head;
    Node* prev = NULL;
    Node* next;
    
    cout << "The nodes of the list are : \n";
    
    //  Till the condition holds true
    while(curr != NULL){
        cout << curr->data << " ";
        
        //  get the address of the previous node and the xnode value of current node
        next = Xor(prev,curr->xnode);
        
        //  update prev and curr for next iteration
        prev = curr;
        curr = next;
    }
}

//  Driver Code
int main()
{
    Node *head = NULL;
    insert(&head,10);
    insert(&head,20);
    insert(&head,30);
    
    printList(head);
    return 0;
}
