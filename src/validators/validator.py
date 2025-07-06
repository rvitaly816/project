from requests import Response

import logging

from src.model.student import Student

logger = logging.getLogger("Validator")

class ResponseValidator:
    @staticmethod
    def validate_status_code(response, expected_code: int):
        actual_code = response.status_code
        if actual_code != expected_code:
            logger.error(f"Ожидался статус {expected_code}, но получен {actual_code}")
        assert response.status_code == expected_code

    @staticmethod
    def validate_json_field(response: Response, expected: Student):
        response_json = response.json()
        for key, value in expected.to_dict().items():
            if key not in response_json:
                logger.error(f"Поле '{key}' отсутствует в ответе")
                assert False
            if response_json[key] != value:
                logger.error(f"Несовпадение поля '{key}': ожидалось '{value}', получено '{response_json[key]}'")
                assert False
        logger.info("Все поля успешно проверены.")