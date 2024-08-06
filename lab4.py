Q#3.....................................................
class node:
    def _init_(self,data):
        self.data=data
        self.next=None

class Stack:
    def _init_(self):
        self.head=None
        self.current=None

    def push(self,node):
        if self.head==None:
            self.head=node
            self.current=node
        else:
            self.current.next=node
            self.current=self.current.next

    def pop(self):
        if self.head==None:
            print("Queue is empty ")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
            
    def _str_(self):
        temp=self.head
        nodes=[]
        while(temp!=None):
            nodes.append(temp.data)
            temp=temp.next
        return "-> ".join(map(str,nodes))
    
s=Stack()
s.push(node(1))
s.push(node(2))
s.push(node(3))
s.push(node(4))
s.push(node(5))

print(s)
s.pop()

Q#2............................................................

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start=0
end=len(list1)-1

n=int(input("Enter number you want to search : "))
while(start<=end):
    mid=(start+end)//2
    print(mid)
    if list1[mid]==n:
        print(f"number found at index {mid}")
        break
    elif list1[mid]<n:
        start=mid+1
    else:
        end=mid-1

if start>end:
    print("Number not found ")

    Q#1...............................................................
    class node:
    def _init_(self,data):
        self.data=data
        self.next=None

class Stack:
    def _init_(self):
        self.head=None

    def push(self,node):
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def pop(self):
        if self.head==None:
            print("Stack is empty ")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
            
    def _str_(self):
        current=self.head
        nodes=[]
        while(current!=None):
            nodes.append(current.data)
            current=current.next
        return "-> ".join(map(str,nodes))
    
s=Stack()
s.push(node(1))
s.push(node(2))
s.push(node(3))
s.push(node(4))
s.push(node(5))

print(s)

s.pop()

print(s)
print(s)

