import asyncio
import json
import pickle
import socket
from quart import Quart, websocket

app = Quart(__name__)

mini_socket = socket.socket()
mini_socket.bind(('127.0.0.1', 8000))
mini_socket.listen(1)
conn, address = mini_socket.accept()

@app.websocket("/random_data")
async def random_data():
    while True:
        data = conn.recv(2048)
        data2 = pickle.loads(data)
        output1 = data2
       
        all_outputs = output1
        print(all_outputs)
        
        await websocket.send(json.dumps(all_outputs))
        await asyncio.sleep(5)

if __name__ == "__main__":
    app.run(port=5000)
