import websockets
import asyncio
import json
import liquid_cord


async def listen_for_events(client):

    print("listening")
    websocket_auth = {
        'op': 2,
        'd': {
            'token': client.token,
            'properties': {},
        }
    }

    async with websockets.connect('wss://gateway.discord.gg/?v=6&encoding=json') as w:
        await w.send(json.dumps(websocket_auth))

        while True:
            recieved = await w.recv()
            recieved = json.loads(recieved)
            print(recieved)
            if recieved['t'] == 'MESSAGE_CREATE':
                print("message recieved")
                asyncio.get_event_loop().create_task(client.events.message_send_event(recieved["d"]))

