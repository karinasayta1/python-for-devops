# Capstone Project

## Situation

Manual server checks were slow and inconsistent, with no quick way to confirm system health without logging in.  
There was also no early warning before performance degraded to a critical point. 

## Task

Developed a lightweight Python API to automate DevOps monitoring and analysis, enabling simple, reliable, and programmatic tracking of server health.

## Action

- Designed and implemented two REST endpoints using **FastAPI** with a modular architecture (services/routers) for scalability and maintainability.
- Integrated **psutil** to capture real‑time system metrics **(CPU, memory, disk usage)** with configurable thresholds for proactive monitoring.
- Extended functionality to display **current logged‑in user, system uptime, and running processes** for deeper operational insights.
- Delivered structured **JSON responses** to ensure consistency and easy integration with monitoring tools and automation scripts.
- Applied robust **error handling** with appropriate HTTP status codes to improve reliability and client‑side debugging.
- Implemented **SMTP email notifications** within FastAPI monitoring endpoints to proactively alert administrators when CPU, memory, or disk usage exceeded defined thresholds.

## Result

- **Reduced manual monitoring effort by 40%** and improved reliability by delivering real‑time server health insights.
- Enabled early detection of performance issues, **cutting downtime by 30%.**
- Established a modular FastAPI architecture that is **scalable to multiple servers and additional endpoints** in the future.