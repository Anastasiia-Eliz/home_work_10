import json

def get_candidates(path):
    """Получает список кандидатов из json-файла"""
    with open(path, "r", encoding="utf-8") as candidates:
        return json.load(candidates)


def list_of_candidates(candidates_list):
    """Выводит список кандидатов по 3 признакам: имя, позиция, навыки"""
    result = ""
    for candidate in candidates_list:
        name = f'Имя кандидата - {candidate["name"]}\n'
        position = f'Позиция кандидата - {candidate["position"]}\n'
        skills = f'Навыки кандидата - {candidate["skills"]}\n\n'
        result += "<pre>"+name+position+skills+"<pre>"

    return result

def get_candidate_id(candidates_list, candidate_id):
    """Выводит кандидата с определенным id"""
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidate_skill(candidates_list, candidate_skill):
    """Выводит кандидатов с определенными навыками"""
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate["skills"].lower().split(", ")

        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result
