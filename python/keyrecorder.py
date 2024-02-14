import keyboard

data = keyboard.record(until="esc")
print(data)

# Removing
for item in data:
    item.remove()
print(type(data))