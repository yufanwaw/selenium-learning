import logging
import sys
from pathlib import Path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

PROJECT_ROOT = Path(__file__).resolve().parents[3]
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
    logger.info("Starting Chrome browser")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver

    logger.info("Closing Chrome browser")
    driver.quit()
