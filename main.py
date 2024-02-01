from fastapi import FastAPI
from starlette import status
from starlette.responses import RedirectResponse

from users.router import router as users_router
from resume.router import router as resumes_router
from vacancy.router import router as vacancies_router
from service.router import router as service_router

app = FastAPI()

app.include_router(users_router)
app.include_router(resumes_router)
app.include_router(vacancies_router)
app.include_router(service_router)


@app.get("/")
async def default_redirect() -> RedirectResponse:
    return RedirectResponse(
        "/docs",
        status_code=status.HTTP_302_FOUND,
    )
