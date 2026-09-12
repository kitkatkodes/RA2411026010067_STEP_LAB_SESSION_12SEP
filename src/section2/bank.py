class Bank:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def perform_operation(self, message):
        self.notification_service.send("System", message)