from algorithm import solve

def entry (coeff):
    response = input(f'{coeff} = ')
    try:
        number = float(response)
    except:
        print(f'Error. Expected a valid real number, got {response} instead')
        return entry(coeff)
    return number

def main():
    a, b, c = entry('a'), entry('b'), entry('c')
    if a:
        return solve(a, b, c)
    else:
        print('a cannot be 0')
        return main()