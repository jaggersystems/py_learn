lucky_numbers = [11, 67, 3, 76, 3, 6, 2, 6]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

# friends.extend(lucky_numbers)
# friends.append("Creed")
# friends.insert(1,"Kelly")
# friends.remove("Jim")
# friends.clear() ## clears all values from list
# friends.pop()  ## removes last element from list
# print(friends.index("Oscar"))  ## check for element in list
print(friends.count("Jim")) ## count occurances

friends.sort() ## sort alphabetical
print(friends)

friends2 = friends.copy()

print(friends2)
