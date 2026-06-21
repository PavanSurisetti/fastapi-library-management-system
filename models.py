#this file contains all the models that we use in the LIBRARY MANAGEMENT SYSTEM
#to inherit from the base class
from database import Base
#for column creation with integer,string as datatypes and foreign key 
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
#----1.Book Table-----
class Book(Base):
    __tablename__='book'
    id=Column(Integer,primary_key=True)#this is the id of the book which is unique
    title=Column(String,nullable=False)#this is the name of the book which cannot be  null
    author=Column(String,nullable=False)#this is the author of the book which cannot be null
    total_copies=Column(Integer,nullable=False)#this is  the total copies of a book which cannot be null
    available_copies=Column(Integer,nullable=False)#this is the available copies of a book
#----2.Members Table------
class Member(Base):
    __tablename__='member'
    id=Column(Integer,primary_key=True)#this is the member id which is unique
    name=Column(String,nullable=False)#this is the name of the member which cannot be null
    email=Column(String,unique=True,nullable=False)#this is  the email of the member which is unique and cannot be null
#-----3.Borrow Table------
class Borrow(Base):
    __tablename__='borrow'
    id=Column(Integer,primary_key=True)#this is the borrow id which is unqiue for a transaction
    member_id=Column(Integer,ForeignKey('member.id'))#this is the member id which refers to the id in the member table
    book_id=Column(Integer,ForeignKey('book.id'))#this is the book id which refers to the id in book table
    borrow_date=Column(DateTime,nullable=False)#this is the borrow date of the book and cannot be null
    return_date=Column(DateTime,nullable=True)#return date of the book ,initially it is null after returning the book it will update here