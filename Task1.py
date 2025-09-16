c=0
try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        for x in file:
           c=c+1
           print(f"Line{c}: ",x.strip())
    file.close()
except FileNotFoundError:
    print('Error: The file "sample.txt" was not found.')
