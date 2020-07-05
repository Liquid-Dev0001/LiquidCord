import asyncio
from .eventRegisterer import EventRegisterer
from liquid_cord.eventListener import listen_for_events


class Client:
    def __init__(self, token):
        self.token = token
        self.events = EventRegisterer()

    def register_events(self, events: EventRegisterer):
        self.events = events

    def run(self):
        print("running bot...")
        asyncio.run(listen_for_events(self))
        print(1)
        while True: pass



