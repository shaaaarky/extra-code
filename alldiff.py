numbers = [1, 3, 6, 8, 6, 8]


def find_out_if_diff(l):
    individuals  = []
    non_individuals = []
    all_unique = True
    for item in l:
        if item not in individuals:
            individuals.append(item)
        elif item in individuals:
            all_unique = False
            non_individuals.append(item)
    if all_unique == True:
        print("There are no repeated numbers in the list")
    print(f"Individuals: {individuals} Repeated Numbers: {non_individuals}")

find_out_if_diff(l=numbers)
