# More Guests

guests = ['Goku', 'Gohan', 'Bulma', 'Picollo']

print("You are welcome to my party "+guests[0])
print("You are welcome to my party "+guests[1])
print("You are welcome to my party "+guests[2])
print("You are welcome to my party "+guests[3])

print(guests[3] + " could not make it to the party.")

guests.remove('Picollo')
guests.append('Vegita')

print("You are welcome to my party "+guests[0])
print("You are welcome to my party "+guests[1])
print("You are welcome to my party "+guests[2])
print("You are welcome to my party "+guests[3])

print("I have found a much bigger dinner table to accomodate for 3 more people")

guests.insert(0, "Krillin")
guests.insert(len(guests)//2, "Tien")
guests.append("Purr")

print("You are welcome to my party "+guests[0])
print("You are welcome to my party "+guests[1])
print("You are welcome to my party "+guests[2])
print("You are welcome to my party "+guests[3])
print("You are welcome to my party "+guests[4])
print("You are welcome to my party "+guests[5])
print("You are welcome to my party "+guests[6])
