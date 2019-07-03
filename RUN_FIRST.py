

with open("C#file/C#.txt", 'r') as file:
    new_file = open("C#file/EditC#.txt", 'w', newline='')
    value = 0
    for row in file:
        print(row)
        if "//" not in row:
            new_file.writelines(row)
    new_file.close()

print("So, you can now officially read that file ;)")