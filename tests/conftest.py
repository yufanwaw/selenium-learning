import os
import logging
import sys
from pathlib import Path

import pytest
from selenium import webdriver

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "test_execution.log", mode="w"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    selenium_remote_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

    logger.info("Starting Chrome browser on Selenium Grid: %s", selenium_remote_url)
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=selenium_remote_url,
        options=options,
    )

    yield driver

    logger.info("Closing Chrome browser")
    driver.quit()
