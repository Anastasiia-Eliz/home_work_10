from flask import Flask
from utils import get_candidates, list_of_candidates, get_candidate_id, get_candidate_skill

app = Flask(__name__)


@app.route("/")
def index_page():
    """Выводит страницу со списком кандидатов"""
    candidate_list = get_candidates("candidates.json")

    return list_of_candidates(candidate_list)


@app.route("/candidates/<int:candidate_id>")
def page_candidate(candidate_id):
    """Выводит страницу с 1 кандидатом по заданному id"""
    candidates_list = get_candidates("candidates.json")

    candidate = get_candidate_id(candidates_list, candidate_id)

    result = f'< img scr = "{candidate["picture"]}" >'

    return result + list_of_candidates([candidate])


@app.route("/skills/<skill>")
def skills(skill):
    """Выводит страницу с 1 или несколькими кандидатами по заданному навыку"""
    candidates_list = get_candidates("candidates.json")
    return list_of_candidates(get_candidate_skill(candidates_list, skill))


app.run()
