friends = ['Jim', 'Karen', 'Kevin']
len(friends)    # len() returns the length of the list
for friend in friends:
    print(friend)
    
for index in range(10):
    print(index)
    
for index in range(3, 10):
    print(index)
    
for index in range(len(friends)):
    print(friends[index])
    
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")