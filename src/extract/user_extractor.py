import requests
import time
from src.utils.logger import setup_logger
from src.config.settings import API_URL, HEADERS, DELAY, RETRIES

logger = setup_logger(__name__)


def extract_user():
    logger.info("Начинаем извлекать данные из randomuser.me")

    for attempt in range(RETRIES):
        try:
            response = requests.get(API_URL, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
                user = data["results"][0]
                logger.info("Данные успешно извлечены")
                return user
            else:
                logger.warning({"status_code": response.status_code,"message": response.text, "action": "retrying"})
                time.sleep(DELAY)
        except Exception as e:
            logger.error({"error": str(e), "attempt": attempt + 1})
            time.sleep(DELAY)

    raise Exception("Не удалось получить данные после нескольких попыток")