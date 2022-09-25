#!/bin/bash
echo -e "alembic upgrade head && python fastapi_app.py" | bash
