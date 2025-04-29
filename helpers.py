import os
from datetime import datetime

def capture_screenshot(page, name="error"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "reports/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    path = f"{screenshot_dir}/{name}_{timestamp}.png"
    page.screenshot(path=path)
    return path
