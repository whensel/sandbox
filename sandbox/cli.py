from .calculator import add
from .models import User
from .db import session_scope


def read_users():
    with session_scope() as session:
        users = session.query(User).all()
        for user in users:
            print(user.__dict__)


def run(args=None):
    read_users()

    #  added_numbers = add("2,3")
    #  print(f"Added numbers value is: {added_numbers}")
