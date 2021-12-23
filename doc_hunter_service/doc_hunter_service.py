import fastapi
import uvicorn

from departments import endpoints as department_endpoints
from doctors import endpoints as doctor_endpoints
from filials import endpoints as filial_endpoints
from schedules import endpoints as schedule_endpoints

api = fastapi.FastAPI()


api.include_router(filial_endpoints.router, prefix="/filials", tags=["filials"])
api.include_router(department_endpoints.router, prefix="/departments", tags=["departments"])
api.include_router(doctor_endpoints.router, prefix="/doctors", tags=["doctors"])
api.include_router(schedule_endpoints.router, prefix="/schedule", tags=["schedule"])

if __name__ == "__main__":
    uvicorn.run("doc_hunter_service:api", port=8000, host="0.0.0.0", reload=True)
