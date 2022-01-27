from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'salary - {time*rate+bonus}')
    except ValueError:
        print('Err')
salary()

sys