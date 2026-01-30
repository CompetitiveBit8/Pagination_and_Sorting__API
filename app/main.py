from fastapi import FastAPI, Request, Depends, Query
from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from pathlib import Path
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

#Database Setup
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

#Defining the Model
class posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    author = Column(String, index=True)



# Base_dir = Path(__file__).resolve().parent
# templates = Jinja2Templates(directory=Base_dir / "templates")


app = FastAPI(title="Pagination and Sorting__API")


@app.get("/")
async def read_root():
    return {"message": "Welcome to Pagination and Sorting API"}


@app.get("/readdDB")
async def read_db(db: Session = Depends(get_db), limit: int = Query(3, ge=3),
                  sort_by: str = Query("id"), page: int = Query(1, ge=1),
                  order: str = Query("asc")):
    

    query = db.query(posts)

    skip = (page -1) * limit

    if order == "asc":
        query = query.order_by(getattr(posts, sort_by).asc())
    elif order == "desc":
        query = query.order_by(getattr(posts, sort_by).desc())

    # pagination
    results = query.offset(skip).limit(limit).all()
    return results

