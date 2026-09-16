from helpers.exceldata import find_rows

SHEET = "Add_ons"


def load_add_ons(tc_id):
    add_ons = []
    for row in find_rows(SHEET, "TC_ID", tc_id):
        name = row.get("ADD_ONS_NAME")
        if name in (None, ""):
            continue
        add_ons.append({
            "add_ons_name": str(name),
            "add_ons_qty": int(row.get("ADD_ONS_QTY") or 1),
        })
    return add_ons
