def showMenu():
 print("---- MENU -----")
 print("1 Add marks")
 print("2 Show marks")
 print("3 Percentile of one")
 print("4 Multiple percentiles")
 print("5 High Low")
 print("6 Sort")
 print("7 Exit")

def getMarks():
    mk=[]
    try:
        n = int(input("how many students "))
    except:
        print("no")
        return mk
    i=0
    while i<n:
        try:
            m=float(input("marks "+str(i+1)+" : "))
            if m<0:
               print(" no negative input")
            else:
               mk.append(m); i=i+1
        except:
            print("wrong")
    return mk


def showMarks(m):
   if len(m)==0:
       print("empty list ")
       return 
   print("marks -->")
   for i in range(0,len(m)):
      print(i+1, ":", m[i])

def getPercent(m, val):
    c=0
    ln = len(m)
    for s in m:
        if s < val:
            c += 1
    if ln==0:
        return 0
    p = (c/ln)*100
    return p

def multPerc(m):
   if len(m)==0:
        print("first enter marks ")
        return
   try:
      k=int(input("how many students"))
   except:
      print("wrong")
      return
   for j in range(k):
      try:
         v=float(input("marks: "))
         pp=getPercent(m,v)
         print("percentile is", round(pp,2))
      except:
         print("skipped one")



def hiLo(m):
    if len(m)==0:
        print("nothing yet")
        return
    hi = max(m)
    lowe = min(m)
    print("High =",hi)
    print("Low =", lowe)


def sortMarks(m):
    if len(m)==0:
        print("enter marks first")
        return
    
    print("1 ascending order")
    print("2 descending order")
    try:
       c=int(input("opt: "))
    except:
       print("no")
       return
    
    if c==1:
        sm=sorted(m)
        print("sorted:", sm)
    elif c==2:
        sm=sorted(m, reverse=True)
        print("sorted:", sm)
    else:
        print("wrong choice")


# main prog
def main():
   # intentionally weird spacing and var names
   mList=[]  
   
   while True:
        showMenu()
        try:
           ch = int(input("ch: "))
        except:
            print(" invalid")
            continue
        
        if ch==1:
           mList = getMarks()
        
        elif ch==2:
           showMarks(mList)
        
        elif ch==3:
           if len(mList)==0:
              print("enter marks")
           else:
              try:
                 xx=float(input("enter score: "))
                 pp = getPercent(mList,xx)
                 print("percentile:", round(pp,2))
              except:
                 print("wrong")
        
        elif ch==4:
           multPerc(mList)
        
        elif ch==5:
           hiLo(mList)
        
        elif ch==6:
           sortMarks(mList)
        
        elif ch==7:
           print("end")
           break
        
        else:
           print("wrong option")

main()