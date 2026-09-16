import base64
import time
from pathlib import Path

from config.settings import settings
from helpers.logger import get_logger

log = get_logger("media")


def _ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def _timestamp():
    return time.strftime("%Y%m%d_%H%M%S")


def screenshot(driver, name="screenshot", directory=None):
    folder = Path(directory) if directory else settings.SCREENSHOT_DIR
    _ensure_dir(folder)
    path = folder / f"{name}_{_timestamp()}.png"
    driver.save_screenshot(str(path))
    log.info(f"screenshot saved {path}")
    return str(path)


def screenshot_bytes(driver):
    return driver.get_screenshot_as_png()


def element_screenshot(driver, element, name="element", directory=None):
    folder = Path(directory) if directory else settings.SCREENSHOT_DIR
    _ensure_dir(folder)
    path = folder / f"{name}_{_timestamp()}.png"
    element.screenshot(str(path))
    return str(path)


def start_recording(driver, fps=10, quality="medium", time_limit=600):
    driver.start_recording_screen(videoFps=fps, videoQuality=quality, timeLimit=time_limit)
    log.info("screen recording started")


def stop_recording(driver, name="video", directory=None):
    payload = driver.stop_recording_screen()
    folder = Path(directory) if directory else settings.ARTIFACT_DIR
    _ensure_dir(folder)
    path = folder / f"{name}_{_timestamp()}.mp4"
    with open(path, "wb") as handle:
        handle.write(base64.b64decode(payload))
    log.info(f"recording saved {path}")
    return str(path)


def push_file(driver, device_path, local_path):
    with open(local_path, "rb") as handle:
        payload = base64.b64encode(handle.read()).decode("utf-8")
    driver.push_file(device_path, payload)


def pull_file(driver, device_path, local_path):
    payload = driver.pull_file(device_path)
    _ensure_dir(Path(local_path).parent)
    with open(local_path, "wb") as handle:
        handle.write(base64.b64decode(payload))
    return local_path


def pull_folder(driver, device_path, local_zip):
    payload = driver.pull_folder(device_path)
    _ensure_dir(Path(local_zip).parent)
    with open(local_zip, "wb") as handle:
        handle.write(base64.b64decode(payload))
    return local_zip


def device_logs(driver, log_type="syslog"):
    return driver.get_log(log_type)


def save_device_logs(driver, log_type="syslog", name="device_log", directory=None):
    folder = Path(directory) if directory else settings.ARTIFACT_DIR
    _ensure_dir(folder)
    path = folder / f"{name}_{_timestamp()}.log"
    entries = driver.get_log(log_type)
    with open(path, "w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(f"{entry.get('timestamp')} {entry.get('message')}\n")
    return str(path)
