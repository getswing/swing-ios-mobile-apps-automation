from helpers.exceldata import find_rows

SHEET = "Player Details"


def load_player_details(tc_id):
    details = {}
    for row in find_rows(SHEET, "TC_ID", tc_id):
        player = str(row.get("PLAYER_NAME") or "")
        question = str(row.get("QUESTION") or "")
        if not player or not question:
            continue
        details.setdefault(player, []).append({
            "question": question,
            "answer_type": str(row.get("ANSWER_TYPE") or "option").lower(),
            "answer": str(row.get("ANSWER") or ""),
        })
    return details


def load_questions(tc_id, player):
    return load_player_details(tc_id).get(player, [])
