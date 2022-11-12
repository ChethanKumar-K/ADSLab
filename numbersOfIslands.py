class DSU:
    def __init__(self,n):
        self.n = n
        self.parent = [0]*n
        self.rank = [0]*n
        self.makeSet()
    
    def makeSet(self):
        #   initially all elements are in their own set
        for i in range(self.n):
            self.parent[i] = i
        
    #   Find the representative of the element , find function
    def find(self,x):
        if(self.parent[x] != x):
            # if x is not the representative of the set, then recursively call find on its parent
            # We also compress the path ie, we move the i th node directly under the root
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self,x,y):
        #   find the representative of the x and y 
        xRoot = self.find(x)
        yRoot = self.find(y)

        #   if elements are in the same set no need to unite
        if(xRoot == yRoot):
            return
        
        #   if rank of x is less than y then move x under y
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot

        #   if rank of y is less than x then move y under x
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot

        #   if both x and y have the same rank, move y under x and increment the rank of x
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] = self.rank[xRoot] + 1

#   returns the number of islands in a[][]
def countIslands(a):
    n = len(a)
    m = len(a[0])
    #   creating individual sets for each element 
    dus = DSU(n*m)

    # The following loop checks for its neighbours and unites indexes with both are 1
    for j in range(n):
        for k in range(m):

            #if the cell is 0,do nothing
            if a[j][k] == 0:
                continue

            #Else check for its 8 neighbours
            #   checking for the down element
            if j+1 < n and a[j+1][k]== 1:
                dus.union( j*(m)+k , (j + 1)* (m) + k)
            
            #   checking for the above element
            if j-1 >= 0 and a[j-1][k] == 1:
                dus.union( j*(m)+k , (j-1)*(m)+ k)

            #   checking for the right element
            if k+1 < m and a[j][k+1] == 1:
                dus.union(j*(m)+k , j*(m)+k+1)
            
            #   checking for the left element
            if k-1 >= 0 and a[j][k-1] == 1:
                dus.union(j*m +k , j * (m) +k -1)
            
            #   checking for the rightdown diagonal element
            if j+1 < n and k+1 < m and a[j+1][k+1] == 1:
                dus.union(j*(m)+k, (j+1)*(m)+k+1)

            #   checking for the rightabove diagonal element
            if j + 1 < n and k - 1 >= 0 and a[j+1][k-1] == 1:
                dus.union(j * (m) + k , (j+1)*(m) + k - 1)

            #    checking for the leftbelow diagonal element
            if j - 1 >= 0 and k + 1 < m and a[j-1][k+1] == 1:
                dus.union(j * m + k, (j-1)*m + k+1)
            
            #   checking for the leftabove diagonal element
            if j - 1 >= 0 and k - 1 >= 0 and a[j-1][k-1] == 1:
                dus.union(j * m + k , (j- 1)* m + k -1)
            
    #   Array to notedown the frequency of each element
    c = [0] * (n*m)
    numberOfIslands = 0
    for j in range(n):
        for k in range(m):
            if a[j][k] == 1:
                x = dus.find(j * m + k)

                #   if frequency of the set is 0,increment the numberOfIslands
                if c[x] == 0:
                    numberOfIslands += 1
                    c[x] += 1
                else:
                    c[x] += 1
    
    return numberOfIslands

#   Main Program
a = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1]
]
print("The Number of islands is : ",countIslands(a))
