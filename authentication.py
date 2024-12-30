from fastapi import FastAPI , Depends, HTTPException , Form , status , Query
from sqlalchemy import  Column,String, ForeignKey, create_engine, FLOAT, Boolean, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.orm import Session, sessionmaker, joinedload, relationship
from sqlalchemy import func
from pydantic import BaseModel, Field
from  typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy import Column, Integer, String

from utils import *
app = FastAPI()


'''MySQL'''
DATABASE_URL = "mysql+pymysql://root:Password123@localhost/fastapi-authentication"
engine = create_engine(DATABASE_URL, connect_args={})
metadata = MetaData()

print('hi')
# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    mobile_number = Column(String(15))
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(1000), nullable=False)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

class RegisterUser(BaseModel):
    name:str
    mobile_number:Optional[str] = None
    email:str
    password:str

@app.post("/register/", response_model=dict)
def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered.")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, password=hashed_password,name=user.name,mobile_number=user.mobile_number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully!"}


class UserLogin(BaseModel):
    email:str
    password:str
@app.post("/login/",response_model=dict)
def login(user:UserLogin, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid Email.")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid Password.")
    token  = create_access_token({"email":db_user.email})
    return {"message":"Login Success!","access_token":token}
