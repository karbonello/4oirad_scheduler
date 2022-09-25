import datetime as dt
import time
from threading import Thread

import requests
import uvicorn
from fastapi import FastAPI

from oirad_scheduler.api.api_router import api_router
from oirad_scheduler.models import Notification
from oirad_scheduler.orm.engine import SessionLocal

app = FastAPI()
app.include_router(api_router)

utc_tz = dt.timezone.utc


def handler():
    while True:
        yesterday = dt.date.today() - dt.timedelta(days=1)
        today = dt.date.today() - dt.timedelta(days=1)
        t = dt.time(hour=5, minute=0)
        yesterday = (dt.datetime.combine(yesterday, t))
        today = (dt.datetime.combine(today, t))
        now = dt.datetime.utcnow()
        if now.hour == 5 and now.minute == 0:
            with SessionLocal.begin() as session:
                all_notifications = session.query(Notification).all()
                for notification in all_notifications:
                    if yesterday < notification.created_at < today:
                        url = 'https://go.botmaker.com/api/v1.0/intent/v2'
                        myobj = {
                            "chatPlatform": 'whatsapp',
                            "chatChannelNumber": notification.bot_whatsapp_number,
                            "platformContactId": notification.user_wa_number,
                            "ruleNameOrId": notification.we_template_name,
                            "params": notification.template_vars
                        }
                        x = requests.post(url, json=myobj)
        time.sleep(60)


@app.get("/health")
async def health_check():
    return {"Hello": "World"}

if __name__ == "__main__":
    thread = Thread(target=handler)
    thread.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
