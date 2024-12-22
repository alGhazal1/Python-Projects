converter= input('Paste the file link:')
try:
    with open(converter, 'r', encoding='utf-8', errors='ignore') as file:
        data = file.read()
    with open("G:\\Education\\plp\Python\\week4Assign\\testOutput.txt", "w", encoding='utf-8', errors='ignore') as file:
        file.write(data)
except FileNotFoundError:
    print('File Not Found. Check Again!')

    file.close()
