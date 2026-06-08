from fastapi import FastAPI
from routers import log_route, health_route, aws_route

app = FastAPI(
    title = "Simple Devops-style API",
    description = "This is a simple API to demonstrate FastAPI capabilities in DevOps context.",
    version = "1.0.0",
    docs_url="/docs",
)

app.include_router(log_route.router)
app.include_router(health_route.router)
app.include_router(aws_route.router, prefix="/aws")