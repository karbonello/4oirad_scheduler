from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NotificationDTO(BaseModel):
    bot_whatsapp_number: str
    user_wa_number: str
    access_token: str
    we_template_name: str
    template_vars: str
