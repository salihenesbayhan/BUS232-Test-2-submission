# function for taking input having list empty as list as a parameter
def inp(l):
    # take input until the user enters 0 
    while True:
        n=int(input("Please enter the number of shares: "))
        l.append(n)
        if n==0:
            break
# function for total shares
# using sum
def shares(lst):
    s=sum(lst)
    return s
# function for majority vote needed with sum of shares
# as parameter
def need(s):
    # majority of share is half of total shares +1
    need=(s//2)+1
    return need
# function for counting number of shareholders needed
def shareholders(l,need):
    # declaring value of count and add to 0
    # count will store number of shareholders
    # add will store sum of list elements
    count,add=0,0
    # iterating through list
    for i in l:
        # adding list elements to add
        add+=i
        # then count number of elements added
        count+=1
        # if sum of shares equals or exceeds the needed share
        # then break
        if add>=need:
            break
    # return count which contains needed number of shareholders.
    return count
# sorting function
def sorting(lst):
    lst.sort(reverse=True)

# Driver Code
l=[]  # empty list or array
# calling input function
inp(l)
# storing total shares after calling shares function
totalshares=shares(l)
# store majority shares
majority=need(totalshares)
print("Thank you, there is a total of",totalshares,"shares represented here.")
print("\nShares needed for majority vote is",majority)
# calling sorting functiion for sorting the array
sorting(l)
print("\nYou need the support of top",shareholders(l,majority),"shareholders for this number of votes.")