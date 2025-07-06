import pytest

from src.api.api_client import APIClient
from src.api.endpoints import Endpoint
from src.builders.student_builder import StudentBuilder
from src.api.student_service import StudentService

@pytest.fixture
def created_student():
    api = APIClient(Endpoint.URL.value)
    service = StudentService(api)
    builder = StudentBuilder()

    student_data = builder.build()
    response = service.create_student(student_data)

    yield student_data, response

    service.delete_student(response.json()["id"])




@pytest.fixture
def student_service():
    api = APIClient(Endpoint.URL.value)
    service = StudentService(api)
    return service

