from repositories.departments import DepartmentsRepository
from repositories.doctors import DoctorsRepository
from repositories.filials import FilialsRepository


def get_filial_repository() -> FilialsRepository:
    return FilialsRepository()


def get_departments_repository() -> DepartmentsRepository:
    return DepartmentsRepository()


def get_doctors_repository() -> DoctorsRepository:
    return DoctorsRepository()
