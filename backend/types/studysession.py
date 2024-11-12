from datetime import datetime
from backend.database.database import insert
import uuid


class StudySession:
    def __init__(self, name: str, start_time: datetime, end_time: datetime, students: list, topics: list, place: str ):
        self._id = str(uuid.uuid4())
        self._name = name
        self._start_time = start_time
        self._end_time = end_time
        self._students = students
        self._topics = topics
        self._place = place

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id: uuid.UUID):
        self._id = str(new_id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        self._end_time = end_time

    @property
    def students(self):
        return self._students

    # TODO: make student type for type hinting
    @students.setter
    def students(self, students: list):
        self._students = students

    @property
    def topics(self):
        return self._topics
    
    @topics.setter
    def topics(self, topics: list):
        self._topics = topics


    @property
    def place(self):
        return self._place
    
    @place.setter
    def place(self, place: str):
        self._place = place

    def size(self):
        return len(self._students)

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "start_time": self._start_time.isoformat(),
            "end_time": self._end_time.isoformat(),
            "students": self._students,
            "topics": self._topics,
            "place": self._place
        }

    def insert(self):
        attendee_list = self.students
        attendees = ", ".join(attendee_list)
        subject_list = self.topics
        subjects = ", ".join(subject_list)
        insert(self._id,
               self._name,
               self._start_time,
               self._end_time,
               attendees,
               subjects,
               self._place)
