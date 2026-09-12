class Bank:
    def __init__(self, alert_service):
        self.alert_service = alert_service

    def trigger_process(self, status_msg):
        self.alert_service.send("System Admin", status_msg)