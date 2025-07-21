friends = ["Apple","Orange",456,"atul"]
print("rohan eating",friends[0])
friends[0] = "orange"
print(friends[0]) 
print(friends[1:3])
# a = "harry"
# print(a[1:3])
friends.append("1")
print(friends)

friend = [1,2,45,34,65,44,55,33]
friend.sort()
print(friend)
friend.reverse()
print(friend)
friends.insert(2,3333)
print(friends)
friends.pop(3)
print(friends)
friend.remove(34)
print(friend)