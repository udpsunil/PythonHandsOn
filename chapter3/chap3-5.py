# Changing Guest List

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