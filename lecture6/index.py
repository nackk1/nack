animals = ["cat", "dog", "rabbit", "horse", "dog","parrot"]
first_dog_index = animals.index("dog")
print(f"The first accurrence  of 'dog' is at index: {first_dog_index}")

second_dog_index = animals.index("dog", first_dog_index+1)
print(f"The second accurrence  of 'dog' is at index: {second_dog_index}")