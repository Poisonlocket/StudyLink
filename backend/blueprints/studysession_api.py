from datetime import datetime, timedelta

from flask import Flask, Blueprint, Response, jsonify

from backend.types.studysession import StudySession


test_sessions = [
    StudySession(
        name="Math Study Group",
        start_time=datetime.now(),
        end_time=datetime.now() + timedelta(hours=2),
        students=["Alice", "Bob", "Charlie"],
        topics=["Algebra", "Calculus"],
        place="Room 101"
    ),
    StudySession(
        name="History Study Session",
        start_time=datetime.now() + timedelta(days=1),
        end_time=datetime.now() + timedelta(days=1, hours=3),
        students=["Diana", "Ethan"],
        topics=["Medieval History", "World War II"],
        place="Library"
    ),
    StudySession(
        name="Physics Study Night",
        start_time=datetime.now() + timedelta(days=2),
        end_time=datetime.now() + timedelta(days=2, hours=4),
        students=["Alice", "Frank", "Grace"],
        topics=["Quantum Mechanics", "Electromagnetism"],
        place="Physics Lab"
    ),
    StudySession(
        name="Chemistry Study Group",
        start_time=datetime.now() + timedelta(days=3),
        end_time=datetime.now() + timedelta(days=3, hours=2),
        students=["Bob", "Charlie", "Helen"],
        topics=["Organic Chemistry", "Inorganic Chemistry"],
        place="Room 202"
    ),
    StudySession(
        name="English Literature Study",
        start_time=datetime.now() + timedelta(days=4),
        end_time=datetime.now() + timedelta(days=4, hours=3),
        students=["Diana", "Grace", "Ivy"],
        topics=["Shakespeare", "Modern Literature"],
        place="Room 303"
    ),
]

#
for study_session in test_sessions:
    study_session.insert()


studysession_api = Blueprint('simple_page', __name__)


@studysession_api.get("/studysession/all")
def get_all_studysessions() -> tuple[Response, int]:
    string_sessions = []
    for studysession in test_sessions:
        session = studysession.to_dict()
        string_sessions.append(session)
    return jsonify(string_sessions), 200


@studysession_api.get("/studysession/<id>")
def get_specific_studysession(id: str):
    for studysession in test_sessions:
        if studysession.id == id:
            return jsonify(studysession.to_dict()), 200

    # If no match is found, return a 404 error response
    return jsonify({"error": f"StudySession with id {id} not found"}), 404
