from flask import Flask, Blueprint, Response

Ssessions = ["a", "b", "c"]

studysession_api = Blueprint('simple_page', __name__)


@studysession_api.get("/studysession/all")
def get_all_studysessions():
    for studysession in Ssessions:
        return Response(Ssessions, 200)
