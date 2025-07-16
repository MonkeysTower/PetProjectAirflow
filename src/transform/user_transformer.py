from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def transform_user(raw_user):
    logger.info("Начинаем преобразование данных")

    transformed = {
        "first_name": raw_user["name"]["first"],
        "last_name": raw_user["name"]["last"],
        "email": raw_user["email"],
        "city": raw_user["location"]["city"],
        "country": raw_user["location"]["country"],
        "phone": raw_user["phone"]
    }

    logger.info("Данные успешно преобразованы")
    return transformed