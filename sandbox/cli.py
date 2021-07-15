# from .calculator import add
from .models import User, Post
from .db import session_scope
from sqlalchemy import delete, update


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
        password="Password1",
    )


def remove_user(user_id):
    with session_scope() as session:
        delete_user = (
            delete(User)
            .where(User.id == user_id)
            .execution_options(synchronize_session="fetch")
        )
        session.execute(delete_user)
        session.commit()


def update_user(user_id, new_name):
    with session_scope() as session:
        update_user_first_name = (
            update(User)
            .where(User.id == user_id)
            .values(first_name=new_name)
            .execution_options(synchronize_session="fetch")
        )
        session.execute(update_user_first_name)
        session.commit()


def add_user():
    with session_scope() as session:
        user = create_user()
        session.add(user)
        session.commit()


def create_post():
    return Post(
        title="Some Random Thing Happened",
        summary="This random event was truly random",
        body="Blaw Blaw Blaw Blaw Blaw",
        is_deleted=False,
    )


def read_posts():
    with session_scope() as session:
        posts = session.query(Post).all()
        for post in posts:
            print(post.__dict__)


def add_post():
    with session_scope() as session:
        post = create_post()
        session.add(post)
        session.commit()


def update_post(post_id, new_title):
    with session_scope() as session:
        update_post_title = (
            update(Post)
            .where(Post.id == post_id)
            .values(title=new_title)
            .execution_options(synchronize_session="fetch")
        )
        session.execute(update_post_title)
        session.commit()


def delete_post(post_id):
    with session_scope() as session:
        delete_post = (
            delete(Post)
            .where(Post.id == post_id)
            .execution_options(synchronize_session="fetch")
        )
        session.execute(delete_post)
        session.commit()


def run(args=None):
    # add_user()
    remove_user(2)
    read_users()

    #  added_numbers = add("2,3")
    #  print(f"Added numbers value is: {added_numbers}")
