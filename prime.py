strt=int(input("Enter a starting point:"))
end=int(input("Enter a ending point:"))
print("These are the prime numbers with in  {} to {} ".format(strt,end)) 
for num in range(strt,end+1):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
    if flag==0:
        print(num)
