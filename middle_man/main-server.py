import asyncio
import json
import pickle
import socket
from quart import Quart, websocket

#Created a quart app to be the structure of this program 
app = Quart(__name__)

# mini_socket = socket.socket()
# mini_socket.bind(('127.0.0.1', 8000))
# mini_socket.listen(1)
# conn, address = mini_socket.accept()


# create a soskcet object, bind it to the localhost and port 8000, listen for any messages and then accept it
# the print statements are for debugging purposes 
mini_socket = socket.socket()
try:
    mini_socket.bind(('127.0.0.1', 8000))
except Exception as e:
    print(e)
print("listening")
mini_socket.listen(1)
print("accepting")
conn, address = mini_socket.accept()
print("accepted")


#This function will be called from the main client program
#Created an async function that receives the data from the socket, pickles it back to a usable form and send it through a websocket
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

#Run app on port 5000 -- different ports prevents any port clashing errors?
if __name__ == "__main__":
    app.run(port=5000)
