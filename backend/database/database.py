import uuid
from datetime import datetime

from sqlalchemy import create_engine, Column, String,DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

username = "root"
password = "My015*Ql!"
host = "localhost"
port = "3306"
db = "StudyLink"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db}")

# Define the base class for models
Base = declarative_base()

# Define the Students table
class Studysession(Base):
    __tablename__: str = 'students'

    uuid: str = Column(String(36), primary_key=True, unique=True)
    name:str = Column(String(50), nullable=False)
    start_time:datetime = Column(DateTime, nullable=False)
    end_time:datetime = Column(DateTime, nullable=False)
    students:list = Column(String(255), nullable=False) #TODO: is a list of students needs modifying
    topics:list[str] = Column(String(255), nullable=False)
    place:str = Column(String(255), nullable=False)


# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def test_data():
    uuid1 = str(uuid.uuid4())
    uuid2 = str(uuid.uuid4())
    stdy_session1 = Studysession(uuid=uuid1, name="some random session",
                                 start_time=datetime(2023, 6, 21, 17, 8, 11),
                                 end_time=datetime(2022, 7, 31, 3, 50, 1),
                                 students="Klara, Achmed, Michael, Mohamed, Lorenzo, Obama",
                                 topics="math, german, english, quantum physics",
                                 place="Nigeria")

    stdy_session2 = Studysession(uuid=uuid2, name="some faggot is part taking in this",
                                 start_time=datetime(2023, 6, 21, 17, 8, 11),
                                 end_time=datetime(2022, 7, 31, 3, 50, 1),
                                 students="xi shing ping, Victor, Putin, Stalin, Mussolini",
                                 topics="history, geography, geometry",
                                 place="Niger")

    session.add(stdy_session1)
    session.add(stdy_session2)
    session.commit()

def query_date():
    query = session.query(Studysession).all()
    for dataset in query:
        print(f"{dataset.uuid}, {dataset.name}, {dataset.start_time}, {dataset.end_time}, {dataset.students}, {dataset.topics}, {dataset.place}")

def insert(uuid, name, start_time, end_time, students, topics, place):
    session.add(Studysession(uuid=uuid, name=name, start_time=start_time, end_time=end_time, students=students, topics=topics, place=place))
    session.commit()

def delete(uuid):
    session.delete(session.query(Studysession).filter_by(uuid=uuid).first())
    session.commit()

def update(uuid, **kwargs):
    change:dict = {}
    for key, value in kwargs.items():
        change[key] = value
    session.query(Studysession).filter_by(uuid=uuid).update(change)
    session.commit()

if __name__ == "__main__":
    test_data()
    uuid = str(uuid.uuid4())
    insert(uuid, "lessgooo",
           datetime(2023, 6, 21, 17, 8, 11),
           datetime(2022, 7, 31, 3, 50, 1),
           "asdf, wert, yxcv ,dfgh, rtzu",
           "math, being gay, some shit, fff",
           "no where")
    # delete("ec85498a-a50a-4cfd-838f-4ebc7246a687")
    update("ffbcaabd-ad19-4747-af92-e2922857e4a3", name="min schwanz isch gross")
    query_date()
