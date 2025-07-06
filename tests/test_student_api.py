import pytest
import uuid

from src.model.student import Student
from src.validators.validator import ResponseValidator
from src.builders.student_update_builder import StudentUpdateBuilder

def test_create_student(created_student):
    '''
    Кейс:
    Шаг 1: Создание студента
    Шаг 2: Валидируем статус код
    Шаг 3: Проверяем поля созданного студента. (Для сравнения берем студента созданного билдером и сравниваем его с ответом POST-запроса)
    '''
    expected_data, response = created_student

    ResponseValidator.validate_status_code(response, 201)
    ResponseValidator.validate_json_field(response, expected_data)



def test_get_student(created_student, student_service):
    '''
    Кейс:
    Шаг 1: Создание студента
    Шаг 2: Получение студента по ИД (ИД берем из ответа предыдущего шага)
    Шаг 3: Валидируем статус код
    Шаг 4: Проверяем поля созданного студента. Сравниваем поля созданного студента с полями студента полученными по ИД
    '''
    expected_data, response = created_student
    student_id = response.json()['id']
    get_response = student_service.get_student(student_id)

    ResponseValidator.validate_status_code(get_response, 200)
    ResponseValidator.validate_json_field(get_response, expected_data)



def test_student_update(created_student, student_service):
    '''
    Кейс:
    Шаг 1: Создание студента
    Шаг 2: Сохраняем данные созданного студента
    Шаг 3: Вызываем UpdateBuilder (Класс получает на вход данные созданного студента, смотрит на его поля и создает новые уникальные данные для апдейта, )
    Шаг 4: Вызываем update_student(Он выполняет PUT-запрос), на вход передаем ИД и новые сгенерированные данные
    Шаг 5: Валидируем статус код
    Шаг 6: Проверяем поля обновленного студента (Сравниваем сгенерированные данные Билдером с данными полученными от PUT-запроса)
    '''

    _, created_response = created_student
    original_student_dict = created_response.json()

    #Удаляем 'id' из словаря, чтобы использовать только поля без id для обновления
    if 'id' in original_student_dict:
        del original_student_dict['id']

    original_student = Student(**original_student_dict)
    student_id = created_response.json()['id']

    updated_data = StudentUpdateBuilder(original_student).build()


    response = student_service.update_student(student_id, updated_data)

    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_json_field(response, updated_data)


