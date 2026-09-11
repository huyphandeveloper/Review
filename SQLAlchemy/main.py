from database import engine, Base
from models import Member, Book, Author, Borrow

Base.metadata.create_all(bind= engine)