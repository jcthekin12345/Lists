people: list[str] = ['John', 'Mike', 'Dick', 'Rick', 'Swick', 'Mick']
print('Original:', people)

# Append
people.append('Jeremy')
print(people)

# Remove
people.remove('John')

# Pop
people.pop()
print(people)

people[0] = 'Blackman'
print(people)

people.insert(2, 'Brown')
print(people)
