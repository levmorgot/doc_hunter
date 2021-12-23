from departments.repositories import DepartmentsRepository
from doctors.repositories import DoctorsRepository
from filials.repositories import FilialsRepository
from schedules.repositories import FreeTimesRepository


def get_filial_repository() -> FilialsRepository:
    return FilialsRepository()


def get_departments_repository() -> DepartmentsRepository:
    return DepartmentsRepository()


def get_doctors_repository() -> DoctorsRepository:
    return DoctorsRepository()


def get_free_times_repository() -> FreeTimesRepository:
    return FreeTimesRepository()
