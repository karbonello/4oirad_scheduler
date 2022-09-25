import datetime

from orm.base import Base
from sqlalchemy import Column, DateTime, Integer, String


class Notification(Base):

    __tablename__ = "notification"

    id = Column(Integer, primary_key=True)
    bot_whatsapp_number = Column(String)
    user_wa_number = Column(String)
    access_token = Column(String)
    we_template_name = Column(String)
    template_vars = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
