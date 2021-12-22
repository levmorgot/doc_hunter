from repositories.departments import DepartmentsRepository
from repositories.doctors import DoctorsRepository
from repositories.filials import FilialsRepository
from repositories.free_times import FreeTimesRepository


def get_filial_repository() -> FilialsRepository:
    return FilialsRepository()


def get_departments_repository() -> DepartmentsRepository:
    return DepartmentsRepository()


def get_doctors_repository() -> DoctorsRepository:
    return DoctorsRepository()


def get_free_times_repository() -> FreeTimesRepository:
    return FreeTimesRepository()
