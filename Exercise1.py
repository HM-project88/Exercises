
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'Set' is wrong and 'set' is correct.
def id_to_fruit(fruit_id: int, fruits: set[str]) -> str:
    idx = 0
    for fruit in fruits:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")
# When we use string array with "{}" it should have address
# We have to change name1, name3, name4 to:
name1 = id_to_fruit(1, {"apple":0, "orange":1, "melon":2, "kiwi":3, "strawberry":4})
name3 = id_to_fruit(3, {"apple":0, "orange":1, "melon":2, "kiwi":3, "strawberry":4})
name4 = id_to_fruit(4, {"apple":0, "orange":1, "melon":2, "kiwi":3, "strawberry":4})
print(name1)
print(name3)
print(name4)
# Or we can change "{}" to "[]"
name1 = id_to_fruit(1, ["apple", "orange", "melon", "kiwi", "strawberry"])
name3 = id_to_fruit(3, ["apple", "orange", "melon", "kiwi", "strawberry"])
name4 = id_to_fruit(4, ["apple", "orange", "melon", "kiwi", "strawberry"])
print('%%%%%%%%%%%%%%%%%%%')
print(name1)
print(name3)
print(name4)

