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

# Association table for many-to-many relationship
"""
student = Table(
    'class_students', Base.metadata,
    Column('class_id', Integer, ForeignKey('classes.id'), primary_key=True),
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True)
)
"""
# Define the Classes table
"""
class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    students = relationship('Student', secondary=class_students, back_populates='classes')

    def __repr__(self):
        return f"<Class(name={self.name})>"
"""
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

if __name__ == "__main__":
    test_data()
    query_date()
