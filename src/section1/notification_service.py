class NotificationService:
    def send(self, recipient_name, alert_text):
        print(f">> ALERT to {recipient_name}: {alert_text}")