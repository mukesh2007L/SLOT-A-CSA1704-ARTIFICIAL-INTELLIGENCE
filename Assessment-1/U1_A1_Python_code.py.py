from collections import deque
import heapq

def water_jug():
    print("\nWATER JUG PROBLEM")
    start=(0,0); goal=(2,0)
    queue=deque([(start,[start])]); visited=set()
    while queue:
        (jug4,jug3),path=queue.popleft()
        if (jug4,jug3)==goal:
            print("\nSolution Steps:")
            for s in path: print(s)
            return
        if (jug4,jug3) in visited: continue
        visited.add((jug4,jug3))
        states=[]
        states.append((4,jug3)); states.append((jug4,3))
        states.append((0,jug3)); states.append((jug4,0))
        t=min(jug4,3-jug3); states.append((jug4-t,jug3+t))
        t=min(jug3,4-jug4); states.append((jug4+t,jug3-t))
        for st in states:
            if st not in visited:
                queue.append((st,path+[st]))

def mars_rover():
    print("\nMARS ROVER AGENT")
    terrain=input("Enter terrain (rock/sand/plain): ")
    obstacle=input("Obstacle present? (yes/no): ")
    battery=int(input("Battery percentage: "))
    print("\nPercepts")
    print("Terrain:",terrain)
    print("Obstacle:",obstacle)
    print("Battery:",battery,"%")
    print("\nAction Taken")
    if battery<20:
        print("Recharge Battery")
    elif obstacle=="yes":
        print("Turn Left and Avoid Obstacle")
    elif terrain=="rock":
        print("Collect Rock Sample")
    elif terrain=="sand":
        print("Analyze Soil")
    else:
        print("Move Forward")
    print("\nPerformance: Mission executed successfully.")

def safe(board,row,col):
    for i in range(col):
        if board[i]==row or abs(board[i]-row)==abs(i-col):
            return False
    return True

def solve(board,col):
    if col==8: return True
    for row in range(8):
        if safe(board,row,col):
            board[col]=row
            if solve(board,col+1): return True
            board[col]=-1
    return False

def queens():
    print("\n8 QUEENS PROBLEM")
    board=[-1]*8
    if solve(board,0):
        print()
        for i in range(8):
            for j in range(8):
                print("Q" if board[j]==i else ".", end=" ")
            print()

def ola():
    print("\nOLA CAB BOOKING")
    source=input("Enter Source: ")
    destination=input("Enter Destination: ")
    print("1.Mini\n2.Micro\n3.Sedan\n4.Prime\n5.Shared")
    choice=int(input("Select Cab: "))
    distance=float(input("Enter Distance (km): "))
    cabs={1:("Mini",12),2:("Micro",10),3:("Sedan",18),4:("Prime",22),5:("Shared",8)}
    if choice not in cabs:
        print("Invalid Choice"); return
    cab,rate=cabs[choice]
    fare=distance*rate
    print("\nBooking Confirmed")
    print("Source:",source)
    print("Destination:",destination)
    print("Cab:",cab)
    print("Fare: Rs.",fare)

def ucs():
    print("\nUNIFORM COST SEARCH")
    graph={'S':[('A',1),('G',12)],'A':[('B',3),('C',1)],'B':[('D',3)],'C':[('D',1),('G',2)],'D':[('G',3)],'G':[]}
    pq=[(0,'S',['S'])]; visited=set()
    while pq:
        cost,node,path=heapq.heappop(pq)
        if node=='G':
            print("Least Cost Path:"," -> ".join(path))
            print("Total Cost =",cost); return
        if node in visited: continue
        visited.add(node)
        for n,w in graph[node]:
            if n not in visited:
                heapq.heappush(pq,(cost+w,n,path+[n]))

while True:
    print("\n===== AI ASSESSMENT MENU =====")
    print("1. Water Jug Problem")
    print("2. Mars Rover Agent")
    print("3. 8 Queens Problem")
    print("4. OLA Cab Agent")
    print("5. Uniform Cost Search")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1: water_jug()
    elif choice==2: mars_rover()
    elif choice==3: queens()
    elif choice==4: ola()
    elif choice==5: ucs()
    elif choice==6:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
