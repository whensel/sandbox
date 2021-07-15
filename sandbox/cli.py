# from .calculator import add
from .models import User, Post
from .db import session_scope
from sqlalchemy import delete, update
from typing import Any


def read_users(session):
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


def remove_user(session, user_id):
    delete_user = delete(User).where(
        User.id == user_id
    )  # .execution_options(synchronize_session="fetch")
    session.execute(delete_user)
    session.commit()


def update_user(session, user_id, new_name):
    update_user_first_name = (
        update(User)
        .where(User.id == user_id)
        .values(first_name=new_name)
        .execution_options(synchronize_session="fetch")
    )
    session.execute(update_user_first_name)
    session.commit()


def add_user(session):
    user = create_user()
    session.add(user)
    session.commit()


def create_post(user: User):
    return Post(
        title="Some Random Thing Happened",
        summary="This random event was truly random",
        body="Blaw Blaw Blaw Blaw Blaw",
        is_deleted=False,
        user=user,
    )


def read_posts(session):
    posts = session.query(Post).all()
    for post in posts:
        print(post.__dict__)


def add_post(session, user):
    post = create_post(user)
    session.add(post)
    session.commit()


def update_post(session, post_id, new_title):
    update_post_title = (
        update(Post)
        .where(Post.id == post_id)
        .values(title=new_title)
        .execution_options(synchronize_session="fetch")
    )
    session.execute(update_post_title)
    session.commit()


def delete_post(session, post_id):
    delete_post = (
        delete(Post)
        .where(Post.id == post_id)
        .execution_options(synchronize_session="fetch")
    )
    session.execute(delete_post)
    session.commit()


def read_user(session: Any, user_id: int) -> User:
    user = session.query(User).get(user_id)
    return user


def run(args=None):
    with session_scope() as session:
        #  add_user()
        #  remove_user(2)
        #  update_user(1, "Bob")
        #  read_users()

        u = read_user(session, 1)
        print(u.__dict__)
        print(u.posts)

        # post = u.posts[2]
        # print(post.__dict__)

        # session.delete(post)

        # post = create_post(u)
        # print(post.__dict__)
        #  added_numbers = add("2,3")
    #  print(f"Added numbers value is: {added_numbers}")
