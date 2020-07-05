class EventRegisterer:
    def __init__(self, **kwargs):
        self.message_send_event = kwargs.get("messageSendEvent", None)
        self.ready_event = kwargs.get("readyEvent", None)

