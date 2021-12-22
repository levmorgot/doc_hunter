import fastapi
# import uvicorn

from endpoits import departments, doctors, free_times, filials

api = fastapi.FastAPI()


api.include_router(filials.router, prefix="/filials", tags=["filials"])
api.include_router(departments.router, prefix="/departments", tags=["departments"])
api.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
api.include_router(free_times.router, prefix="/free-times", tags=["free-times"])
#
# if __name__ == "__main__":
#     uvicorn.run("cache-async-few-threads-microservice:api", port=8000, host="0.0.0.0", reload=True)