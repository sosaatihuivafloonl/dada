from fastapi import Depends, APIRouter, Request, FastAPI
from routes import userRoute
from models import userModel
from database.connection import engine
from fastapi.middleware.cors import CORSMiddleware


#config DB
userModel.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ['http://localhost:3000', 'http://127.0.0.1:3000',
           'https://localhost:3000', 'https://127.0.0.1:3000'] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# config routes
app.include_router(userRoute.userRouter)







