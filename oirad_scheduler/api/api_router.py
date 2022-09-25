import datetime

from fastapi import APIRouter, Depends
from requests import Session
from sqlalchemy.orm import sessionmaker

from oirad_scheduler.api.dto import NotificationDTO
from oirad_scheduler.orm.engine import engine, SessionLocal
from oirad_scheduler.orm.utils import get_session_web

from oirad_scheduler.models import Notification

api_router = APIRouter()

Session = sessionmaker(engine)


def is_database_online(session: Session = Depends(get_session_web)) -> bool:
    return bool(session)


@api_router.post(
    '/api/add_notification', status_code=200
)
async def set_notification(
    notification_data: NotificationDTO
) -> None:
    with SessionLocal.begin() as session:
        notification = Notification(
            bot_whatsapp_number=notification_data.bot_whatsapp_number,
            user_wa_number=notification_data.user_wa_number,
            access_token=notification_data.access_token,
            we_template_name=notification_data.we_template_name,
            template_vars=notification_data.template_vars,
            created_at=datetime.datetime.utcnow(),
        )
        session.add(notification)
        session.commit()
    return None
