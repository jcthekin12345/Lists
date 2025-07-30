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

# Change
people[0] = 'Blackman'
print(people)

# Insert
people.insert(2, 'Brown')
print(people)

# Clear
people.clear()
print(people)
