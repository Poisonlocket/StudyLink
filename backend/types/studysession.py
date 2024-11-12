from datetime import datetime
import uuid

class StudySession:
    def __init__(self, name: str, start_time: datetime, end_time: datetime, students: list, topics: list, place: str ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self._students = students
        self.topics = topics
        self.place = place

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, new_id: uuid.uuid4()):
        new_id = str(new_id)
        self.id = new_id
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name: str):
        self.name = name

    @property
    def start_time(self):
        return self.start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        self.start_time = start_time

    @property
    def end_time(self):
        return self.end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        self.end_time = end_time

    @property
    def students(self):
        return self._students

    # TODO: make student type for type hinting
    @students.setter
    def students(self, students: list):
        self._students = students

    @property
    def topics(self):
        return self.topics
    
    @topics.setter
    def topics(self, topics: list):
        self.topics = topics
    

    @property
    def place(self):
        return self.place
    
    @place.setter
    def place(self, place: str):
        self.place = place

    def size(self):
        return len(self._students)