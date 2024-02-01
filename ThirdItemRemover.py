# Exercise to print and delete the third number from a list of numbers

lt = [1, 3, 7, 5, 7, 8, 9]

while True:
    print(f"List: {lt}")
    if len(lt) <= 2:
        print(f"Item removed: {lt[-1]}")
        lt.pop()
    elif len(lt) > 2:
        print(lt[2])
        del lt[2]
    if len(lt) == 0:
        print("Done")
        break
