from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session
from fastapi import Depends
from database.connection import get_db
from models.userModel import User




# instance
userRouter = APIRouter()


@userRouter.get("/test")
async def get_test():
    return "message: hello!"

# Функция для создания пользователя
@userRouter.post("/user")
def create_user(target_username: str, db: Session = Depends(get_db)):
    user = User(product_id='2321321321',target_username=target_username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Пример использования
# @userRouter.post("/users")
# def create_user_route(target_username: str, db: Session = Depends(get_db)):
#     new_user = create_user(target_username, db)
#     return {"message": f"Создан пользователь с именем: {new_user.target_username}"}



