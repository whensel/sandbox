from .calculator import add
from .models import User
from .db import session_scope


def read_users():
    with session_scope() as session:
        users = session.query(User).all()
        for user in users:
            print(user.__dict__)

def create_user():
    return User(
        first_name="Joe",
        last_name="Smith",
        email="joe.smith@mail.com",
        password="Password1"
    )

def add_user():
    with session_scope() as session:
        user = create_user()
        print(user)
        session.add(user)
        session.commit()


def run(args=None):
    add_user()
    read_users()

    #  added_numbers = add("2,3")
    #  print(f"Added numbers value is: {added_numbers}")
