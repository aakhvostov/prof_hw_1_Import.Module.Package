from datetime import datetime
from application.salary import calculate_salary as calc
from application.db.people import get_employees as emp


def main():
    print('I am from main')
    calc()
    emp()
    print(datetime.now())


if __name__ == '__main__':
    main()
