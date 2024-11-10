# D: Dependancy Inversion Principle
from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailService(NotificationService):
    def send(self, message):
        return f"Email sent with message: {message}"


class SMSService(NotificationService):
    def send(self, message):
        return f"SMS sent with message: {message}"


class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        return self.service.send(message)


# Using the classes with dependency injection
email_service = EmailService()
sms_service = SMSService()

manager = NotificationManager(email_service)
print(manager.notify("Hello via Email"))

manager = NotificationManager(sms_service)
print(manager.notify("Hello via SMS"))
