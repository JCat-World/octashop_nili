

class SendEmailToUser:
    def __init__(self, email_service):
        self.email_service = email_service

    def execute(self, to: str, subject: str, body: str):

        self.email_service.send_email(to, subject, body)
