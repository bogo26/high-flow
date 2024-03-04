from channels.generic.websocket import AsyncWebsocketConsumer
import json
# from channels.consumer import SyncConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    print("ChatConsumer")
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('DATA : ', text_data_json)

        # Handle the received message (e.g., broadcast to other clients)
        await self.send(text_data=json.dumps({
            'message': message
        }))


# class MyConsumer(AsyncWebsocketConsumer):
#     groups = ["broadcast"]

#     async def connect(self):
#         # Called on connection.
#         # To accept the connection call:
#         await self.accept()
#         # Or accept the connection and specify a chosen subprotocol.
#         # A list of subprotocols specified by the connecting client
#         # will be available in self.scope['subprotocols']
#         await self.accept("subprotocol")
#         # To reject the connection, call:
#         await self.close()

#     async def receive(self, text_data=None, bytes_data=None):
#         # Called with either text_data or bytes_data for each frame
#         # You can call:
#         await self.send(text_data="Hello world!")
#         # Or, to send a binary frame:
#         await self.send(bytes_data="Hello world!")
#         # Want to force-close the connection? Call:
#         await self.close()
#         # Or add a custom WebSocket error code!
#         await self.close(code=4123)

#     async def disconnect(self, close_code):
#         # Called when the socket closes




# class EchoConsumer(SyncConsumer):

#     def websocket_connect(self, event):
#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })





# import json
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#     def disconnect(self, close_code):
#         pass
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         self.send(text_data=json.dumps({
#             'message': message
        # }))
# 