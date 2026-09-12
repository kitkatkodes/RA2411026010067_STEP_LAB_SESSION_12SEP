class NotificationService:
    def send(self, recipient, message):
        print(f"[EMAIL] To: {recipient} | {message}")