from fastapi import FastAPI
from routers import health_route, sys_info

app = FastAPI(
    title = "System Health Monitoring API",
    description = "API to monitor system health and retrieve system information",
    version = "1.0.0",
    docs_url = "/docs"
)

app.include_router(health_route.router)
app.include_router(sys_info.router)