from pathlib import Path

import yaml

from helpers.logger import get_logger

log = get_logger("testdata")
DATA_DIR = Path(__file__).resolve().parent.parent / "fixtures" / "data"


def _read(tc_id):
    direct = DATA_DIR / f"{tc_id}.yaml"
    if direct.exists():
        return yaml.safe_load(direct.read_text(encoding="utf-8")) or {}
    for path in sorted(DATA_DIR.glob("*.yaml")):
        payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if tc_id in payload:
            return payload[tc_id] or {}
    raise FileNotFoundError(f"no test data for {tc_id} in {DATA_DIR}")


class CaseData:
    def __init__(self):
        self._payload = {}
        self.TC_ID = None

    def load(self, tc_id):
        for key in list(self._payload):
            if hasattr(self, key.upper()):
                delattr(self, key.upper())
        self._payload = _read(tc_id)
        self.TC_ID = tc_id
        for key, value in self._payload.items():
            setattr(self, key.upper(), value)
        log.info(f"loaded test data {tc_id}")
        return self

    def get(self, key, default=None):
        return self._payload.get(key, self._payload.get(key.lower(), default))

    def as_dict(self):
        return dict(self._payload)

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)
        raise AttributeError(f"{name} not in test data {self._payload.get('tc_id', '')}, keys: {sorted(self._payload)}")


D = CaseData()


def load_add_ons(tc_id):
    return _read(tc_id).get("add_ons", [])
