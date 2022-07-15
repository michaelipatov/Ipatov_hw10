import json
from pathlib import Path


def load_candidates():
    """Получает абсолютный путь к файлу candidates.json
       и возвращает список словарей candidates_list"""
    home = Path.home()
    path = Path(home, 'PycharmProjects', 'Ipatov_hw10', 'candidates.json')
    with open(path, encoding="utf-8") as file:
        candidates_list = json.load(file)
        return candidates_list


candidates_list = load_candidates()


def get_all():
    """Возвращает список all_list со всеми кандидатами"""
    all_list = []
    for candidates_dict in candidates_list:
        all_list.append(f"Имя кандидата - {candidates_dict['name']}\n")
        all_list.append(f"Позиция кандидата - {candidates_dict['position']}\n")
        all_list.append(f"Навыки через запятую - {candidates_dict['skills']}\n")
        all_list.append("\n")
    all_list = "".join(all_list)
    return all_list


def get_by_pk(pk):
    """Возвращает кандидата по его pk"""
    by_pk_list = []
    url_image = None
    for candidates_dict in candidates_list:
        if candidates_dict['pk'] == pk:
            url_image = candidates_dict['picture']
            by_pk_list.append(f"Имя кандидата - {candidates_dict['name']}\n")
            by_pk_list.append(f"Позиция кандидата - {candidates_dict['position']}\n")
            by_pk_list.append(f"Навыки через запятую - {candidates_dict['skills']}\n")
    by_pk_list = "".join(by_pk_list)
    return by_pk_list, url_image


def get_by_skill(skill_name):
    """Возвращает кандидатов по их скилам"""
    by_skill_list = []
    for candidates_dict in candidates_list:
        candidates_skills = candidates_dict['skills'].lower().split(", ")
        if skill_name in candidates_skills:
            by_skill_list.append(f"Имя кандидата - {candidates_dict['name']}\n")
            by_skill_list.append(f"Позиция кандидата - {candidates_dict['position']}\n")
            by_skill_list.append(f"Навыки через запятую - {candidates_dict['skills']}\n")
            by_skill_list.append(f"\n")
    by_skill_list = "".join(by_skill_list)
    return by_skill_list
