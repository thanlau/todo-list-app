from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import calendar

Base = declarative_base()

class Table(Base):

    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

class Todo:
    def __init__(self, db_name):
        self.engine = create_engine(f"sqlite:///{db_name}.db?check_same_thread=False")

    def save_database(self, add_task, add_deadline, session):
        new_row = Table(task=add_task, deadline=datetime.strptime(add_deadline,'%Y-%m-%d').date())
        session.add(new_row)
        session.commit()
        print('The task has been added!')

    def print_all(self,session):
        rows = session.query(Table).order_by(Table.deadline).all()
        # num = 1
        if not rows:
            print("Nothing to do")
        for row in rows:
            print(f"{row.id}. {row}. {row.deadline.day} {row.deadline.strftime('%b')}")
            # num += 1

    def print_today(self, session):
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        print(f"Today {today.day} {today.strftime('%b')}")
        if not rows:
                print("Nothing to do")
        print(rows)

    def print_week(self, session):
        today = datetime.today().date()
        idx_week = datetime.today().weekday()
        delta = 0
        while delta <= 6:
            print(calendar.day_name[idx_week], today.day, today.strftime('%b'))
            rows = session.query(Table).filter(Table.deadline == today).all()
            if not rows:
                print("Nothing to do")
            print(rows)
            print()
            today += timedelta(days=1)
            delta += 1
            idx_week = (idx_week+ 1)%7

    def print_miss(self, session):
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline < today.date()).all()
        print("Missed tasks:")
        if not rows:
                print("Nothing is missed!")
        for row in rows:
            print(f"{row}. {row.deadline.day} {row.deadline.strftime('%b')}")
        print()

    def delete(self, session, delete_choice):
        today = datetime.today()
        rows = session.query(Table).filter(Table.id == delete_choice).all()
        if not rows:
            print("Nothing to delete")
        for row in rows:
            session.delete(row)
            session.commit()
        print("The task has been deleted!")


    def main(self):
        Base.metadata.create_all(bind = self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        while True:
            print(f"""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")
            choice = input()
            if choice == '0':
                print('Bye!')
                exit()
            elif choice == '1':
                self.print_today(session)
            elif choice == '2':
                self.print_week(session)
            elif choice == '3':
                self.print_all(session)
            elif choice == '4':
                self.print_miss(session)
            elif choice == '5':
                print('Enter task')
                new_task = input()
                print("Enter deadline")
                new_deadline = input()
                self.save_database(new_task,new_deadline,session)
            elif choice == '6':
                self.print_all(session)
                print("Choose the number of the task you want to delete:")
                delete_choice = int(input())
                self.delete(session, delete_choice)
            else:
                print('Invaild Input')
                exit()
t = Todo('todo')
t.main()

# idx_week = datetime.today().weekday()
# today = datetime.today().date()
# while idx_week <= 6:
#     delta = 0
#     today += timedelta(days=1)
#     print(today.day, today.strftime('%b'),calendar.day_name[idx_week])
#     delta += 1
#     idx_week += 1
# print(datetime.strptime('2020-12-26','%Y-%m-%d').date())








