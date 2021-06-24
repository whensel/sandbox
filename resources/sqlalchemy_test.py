from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column("id", primary_key=True)
    title = Column("title", String(255), nullable=False)
    summary = Column("summary", String(140), nullable=False)
    body = Column("body", Text, nullable=False)
    is_deleted = Column("is_deleted", Boolean, nullable=False)


connection_url = f"postgresql://sandbox_user:Fxber93wGaB2@postgres-db:5432/sandbox_test"

engine = create_engine(connection_url)

db = scoped_session(sessionmaker(bind=engine))

query_rows = db.execute("SELECT * FROM users").fetchall()
for register in query_rows:
    print(register)
