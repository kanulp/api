from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_all_users(db: Session):
    return db.query(models.User)


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.UserInfo(username=user.username, password=fake_hashed_password, fullname=user.fullname)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user