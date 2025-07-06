from http.client import responses

from requests import Response
import logging
from src.api.api_client import APIClient
from src.model.student import Student

logger = logging.getLogger("StudentService")


class StudentService:
    def __init__(self, api_client: APIClient):
        self.api = api_client

    def create_student(self, student_data: Student) -> Response:
        logger.info("Создание студента через API...")
        response = self.api.post(student_data.to_dict())
        logger.info(f"Студент успешно создан. Данные студента: {student_data}")
        return response

    def get_student(self, student_id: str) -> Response:
        logger.info(f"Получение студента с ID = {student_id}")
        response = self.api.get(student_id)
        logger.info("Данные успешно получены.")
        return response

    def update_student(self, student_id: str, new_data: Student):
        logger.info(f"Обновление данных студента ID = {student_id}")
        response = self.api.put(student_id, new_data.to_dict())
        logger.info(f"Данные студента успешно обновлены. Данные студента: {new_data}")
        return response

    def delete_student(self, student_id: str):
        logger.info(f"Удаление студента ID = {student_id}")
        response = self.api.delete(student_id)
        logger.info("Студент успешно удалён.")
        return response