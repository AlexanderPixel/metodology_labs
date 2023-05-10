from algorithm import solve
from re import search

def main(filename):
    content = validator(filename)
    if content:
        a, b, c = [float(i) for i in content.split()]
        if a:
            return solve(a, b, c)
        else:
            print('a cannot be 0')
            return main(filename)

    else:
        return None
       
def validator(filename):
    pattern = r'^(-?\d+(\.\d+)?\s){2}-?\d+(\.\d+)?\n$'
    try:
        with open(filename, 'r') as file:
            line = file.read()
    except:
        print(f'File {filename} does not exist')
        return None
    matching = search(pattern, line)
    if matching:
        return matching.group()[:-2]
    else:
        print('Invalid file format')
        return None 