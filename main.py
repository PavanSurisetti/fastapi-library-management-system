#this file contains all the API endpoints for our API
#to create all the tables in the database
from database import Base,engine,SessionLocal
#importing the models
import models
#importing session
from  sqlalchemy.orm import Session
#fastapi application creation
from fastapi import FastAPI,Depends,HTTPException,Path#dependency function and http exception
#this is used for the data validation
from pydantic import BaseModel,Field
#datetime
from datetime import datetime
#first create all the tables
Base.metadata.create_all(engine)#it will create all the tables
#let's create app for fastapi
app=FastAPI()
#----------------book creation--------------------
class bookCreation(BaseModel):
    title:str
    author:str
    total_copies:int
    available_copies:int
#------------user registration--------------
class memberRegister(BaseModel):
    name:str
    email:str
#--------------Borrow Book---------
class borrowBook(BaseModel):
    member_id:int
    book_id:int
    borrow_date:datetime=Field(default_factory=datetime.utcnow)
#----------------Return Book-----------
class returnBook(BaseModel):
    borrow_id:int
    return_date:datetime=Field(default_factory=datetime.utcnow)
#-------dependency function----------
def get_db():
    db=SessionLocal()#it is used to interact with the DB locally
    try:
        yield db#it will give db to API
    finally:
        db.close()#close the db
#welcome page
@app.get('/',tags=['Welcome'])
def home():
    return 'Welcome to Library Management System'
#------1.create Book-----------------------
@app.post('/book',tags=['Book Creation'])
def book_creation(*,db:Session=Depends(get_db),add:bookCreation):
    book=models.Book(title=add.title,author=add.author,total_copies=add.total_copies,available_copies=add.available_copies)
    #adding book to the session
    db.add(book)
    #commiting to the database
    db.commit()
    db.refresh(book)
    return {
        'message':'book added successfully',
        'book':{
            'id':book.id,
            'title':book.title,
            'author':book.author,
            'total_copies':book.total_copies,
            'availabe_copies':book.available_copies
        }
    }
#2------------get all Books ------------------------
@app.get('/Books',tags=['Get all Books'])
def getAllBooks(db:Session=Depends(get_db)):
    books=db.query(models.Book).all()
    if not books:
        raise HTTPException(status_code=404,detail='No Books Found')
    return{
        'message':'all books fetched successfully',
        'books':books
    }
#------------3.Get available Books--------------
@app.get('/books/available',tags=['Available Books'])
def availableBooks(db:Session=Depends(get_db)):
    books=db.query(models.Book).filter(models.Book.available_copies>0).all()
    if not books:
        raise HTTPException(status_code=404,detail='No Available Books Found')
    return{
        'message':'all available books fetched successfully',
        'books':books
    }
#--------4.Register Member --------------
@app.post('/register',tags=['Register Member'])
def register(add:memberRegister,db:Session=Depends(get_db)):
    member=models.Member(name=add.name,email=add.email)
    #add member to session
    db.add(member)
    #commiting to the database
    db.commit()
    return{
        'message':'memeber created successfully',
        'memeber_details':{
            'member_id':member.id,
            'name':member.name,
            'email':member.email
        }
    }
#-----5.Get all members------------------
@app.get('/memeber',tags=['Get all Members'])
def get_Member(db:Session=Depends(get_db)):
    members=db.query(models.Member).all()
    if not members:
        raise HTTPException(status_code=404,detail='Members Not Found')
    return{
        'message':'Members fetched Successfully',
        'details':members
    }
#-------6.Borrow book-------------------
@app.post('/borrow',tags=['Borrow Book'])
def borrowBook(add:borrowBook,db:Session=Depends(get_db)):
    borrow_book=models.Borrow(member_id=add.member_id,book_id=add.book_id,borrow_date=add.borrow_date)
    member_check=db.query(models.Member).filter(models.Member.id==add.member_id).first()
    book_check=db.query(models.Book).filter(models.Book.id==add.book_id).first()
    if not member_check:
        raise HTTPException(status_code=404,detail='Member Not Found')
    if not book_check:
        raise HTTPException(status_code=404,detail='Book Not Found')
    if(book_check.available_copies>0):
        #add to session
        db.add(borrow_book)
        #commiting to the database
        book_check.available_copies-=1
        db.commit()
        db.refresh(borrow_book)
        return{
            'message':'Book Borrowed Sucessfully!',
            'Transaction':{
                'memeber_id':borrow_book.member_id,
                'book_id':borrow_book.book_id,
                'borrorw_date':borrow_book.borrow_date

            }
        }
    raise HTTPException(status_code=404,detail='Books Out of Stock')
#----------------7.Return Book------------------
@app.post('/return',tags=['Return a Book'])
def return_Book(add:returnBook,db:Session=Depends(get_db)):
    borrow_id_check=db.query(models.Borrow).filter(models.Borrow.id==add.borrow_id).first()
    if not borrow_id_check:
        raise HTTPException(status_code=404,detail='Borrow ID not Found')
    #increase the avilable copies
    book=db.query(models.Book).filter(models.Book.id==borrow_id_check.book_id).first()
    book.available_copies+=1
    borrow_id_check.return_date=add.return_date
    db.commit()
    return{
        'message':'Book Returned Successfully'
    }
#-------8.Member Borrow History------------------------
@app.get('/borrowhistory/{id}',tags=['Borrow History'])
def history(id:int=Path(description='Enter Member ID'),db:Session=Depends(get_db)):
    history=db.query(models.Borrow).filter(models.Borrow.member_id==id).all()
    if not history:
        raise HTTPException(status_code=404,detail='History Not Found')
    return{
        'message':'History Fetched Successfully',
        'History':history
    }