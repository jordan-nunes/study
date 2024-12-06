input_coordinates = input("Write the coordinates: ")
list_coordinates = list(input_coordinates)
list_row_letters = []
list_row_coordinates = []
list_column_letters = []
list_column_coordinates = []

letter_index = 0
for char in input_coordinates:
    if not list_coordinates[letter_index].isdigit():
        list_row_letters.append(list_coordinates[letter_index])
        letter_index += 1
    else:
        row_letters = ''.join(list_row_letters)
        break

for char in input_coordinates[letter_index:]:
    if list_coordinates[letter_index].isdigit():
        list_row_coordinates.append(list_coordinates[letter_index])
        letter_index += 1
    else:
        row_coordinates = ''.join(list_row_coordinates)
        num_row_coordinates = int(row_coordinates)
        break

if letter_index >= len(input_coordinates):
    row_coordinates = ''.join(list_row_coordinates)
    num_row_coordinates = int(row_coordinates)

for char in input_coordinates[letter_index:]:
    if not list_coordinates[letter_index].isdigit():
        list_column_letters.append(list_coordinates[letter_index])
        letter_index += 1
    else:
        column_letters = ''.join(list_column_letters)
        break

for char in input_coordinates[letter_index:]:
    if list_coordinates[letter_index].isdigit():
        list_column_coordinates.append(list_coordinates[letter_index])
        letter_index += 1
    else:
        column_coordinates = ''.join(list_column_coordinates)
        num_col_coordinates = int(column_coordinates)
        break

if letter_index >= len(input_coordinates) and len(list_column_letters) > 0:
    column_coordinates = ''.join(list_column_coordinates)
    num_col_coordinates = int(column_coordinates)

if len(list_column_coordinates) != 0:
    ax = ""
    while num_col_coordinates > 0:
        num_col_coordinates, remainder = divmod(num_col_coordinates, 26)
        ax = chr(64 + remainder) + ax

    print("{}{}".format(ax, row_coordinates))
else:
    rx = num_row_coordinates
    num_col = 0
    for x, char in enumerate(reversed(list_row_letters)):
        num_col += (ord(char.upper()) - ord('A') + 1) * (26 ** x)    

    print("R{}C{}".format(rx, num_col))