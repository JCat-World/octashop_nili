# core/services/email_service.py
class EmailService:
    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        raise NotImplementedError
