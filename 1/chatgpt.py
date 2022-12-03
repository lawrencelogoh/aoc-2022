with open('file.txt', 'r') as f:
    lines = f.readlines()
    arrays = []

    current_array = []

    for line in lines:
        if line.strip() == '':
            arrays.append(current_array)
            current_array = []
        else:
            current_array += [int(x) for x in line.split()]
    arrays.append(current_array)

    new_array = []
    for array in arrays:
        new_array.append(sum(array))


#part 1
print(max(new_array))

new_array.sort(reverse=True)
print(sum(new_array[:3]))
