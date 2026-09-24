from helpers.exceldata import find_rows

SHEET = "Event Packages"


def load_package(tc_id):
    packages = []
    for row in find_rows(SHEET, "TC_ID", tc_id):
        packages.append({
            "package_name": str(row.get("PACKAGE_NAME") or ""),
            "package_qty": int(row.get("PACKAGE_QTY") or 1),
            "package_capacity": int(row.get("PACKAGE_CAPACITY") or 1),
            "package_slots": str(row.get("PACKAGE_SLOTS") or ""),
            "amount_package": str(row.get("AMOUT_PACKAGE") or row.get("AMOUNT_PACKAGE") or ""),
        })
    return packages
