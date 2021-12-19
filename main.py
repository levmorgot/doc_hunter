import fastapi
import uvicorn

from endpoits import filials, departments, doctors

api = fastapi.FastAPI()


api.include_router(filials.router, prefix="/filials", tags=["filials"])
api.include_router(departments.router, prefix="/departments", tags=["departments"])
api.include_router(doctors.router, prefix="/doctors", tags=["doctors"])


if __name__ == "__main__":
    uvicorn.run("main:api", port=8000, host="0.0.0.0", reload=True)
