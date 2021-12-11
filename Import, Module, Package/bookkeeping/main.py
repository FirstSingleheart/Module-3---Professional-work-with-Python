from datetime import datetime, date, time
import db.people as people
import application.salary as salary

if __name__ == '__main__':
    print(datetime.now())
    people.get_employees()
    salary.calculate_salary()
