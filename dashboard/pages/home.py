from dash import html, register_page, dcc, callback, Input, Output 
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import websockets
import json
import asyncio
from dash_extensions import WebSocket
from dash_extensions.enrich import html, dcc, Output, Input, DashProxy
from collections import deque 


register_page(
 __name__,
 name='Home',
 top_nav=True,
 path='/'
)

#Overall layout for the home page
def layout():
 layout = html.Div(style={'marginLeft': '20px', 'width' : '98%', 'marginBottom' : '15px'}, children=[

 html.Div(style={'marginTop': '20px', 'marginBottom' : '20px'},children=[
     
 html.Div(className="row",children=[
    html.Div( className="col", children=[
    html.H3('RAM Graph')
    ]),
    html.Div( className="col", children=[
    html.H3('CPU Graph')
    ]),
 ]), 

 html.Div(className="row",children=[
    html.Div( className="col",children=[
    dcc.Graph(id ="ram-graph", className="col"),
    ]),
    html.Div( className="col",children=[
    WebSocket(id="ws", url="ws://127.0.0.1:5000/random_data"),
    dcc.Graph(id ="cpu-graph", className="col"),
    dcc.Interval(id='graph-update4', interval=2000, n_intervals=0),
    ]),
 ]),


 ]),

 html.Br(),
 html.Br(),
 html.H2('Explainations'),
 html.Br(),
 html.Span('RAM Graph', style={'padding': '5px','fontSize':'25px', 'borderWidth':'1px', 'borderStyle':'solid'}),
 html.P('The RAM Graph shows the amount of RAM in use in MB out of 7GB of Total RAM.',
 style={'marginTop': '10px', 'fontSize': '20px'}),
 html.Br(),
 html.Span('CPU Graph', style={'padding': '5px','fontSize':'25px', 'borderWidth':'1px', 'borderStyle':'solid'}),
 html.P('The CPU Graph shows the average utilization percentage of the 6 CPU cores.',
 style={'marginTop': '10px', 'fontSize': '20px'}),

 ])
 return layout




######################################################################################################################################################################
async def get_data():
    print("setting uri")
    uri = "ws://127.0.0.1:5000/random_data"
    try:
        async with websockets.connect(uri) as websocket:
            print("websocket connected")
            while True:
                print("recving data")
                data = await websocket.recv()
                print("data recvd")
                return json.loads(data)
    except Exception as e:
        print("Exception:", e)

df1 = pd.DataFrame(columns=['time', 'value']) 
x1 = deque(maxlen = 60)
y1 = deque(maxlen = 60)

df2 = pd.DataFrame(columns=['time', 'value']) 
x2 = deque(maxlen = 60)
y2 = deque(maxlen = 60)

df3 = pd.DataFrame(columns=['time', 'value']) 
x3 = deque(maxlen = 60)
y3 = deque(maxlen = 60)

df4 = pd.DataFrame(columns=['time', 'value']) 
x4 = deque(maxlen = 60)
y4 = deque(maxlen = 60)

df5 = pd.DataFrame(columns=['time', 'value']) 
x5 = deque(maxlen = 60)
y5 = deque(maxlen = 60)

df6 = pd.DataFrame(columns=['time', 'value']) 
x6 = deque(maxlen = 60)
y6 = deque(maxlen = 60)

df7 = pd.DataFrame(columns=['time', 'value']) 
x7 = deque(maxlen = 60)
y7 = deque(maxlen = 60)

df8 = pd.DataFrame(columns=['time', 'value']) 
x8 = deque(maxlen = 60)
y8 = deque(maxlen = 60)

df9 = pd.DataFrame(columns=['time', 'value']) 
x9 = deque(maxlen = 60)
y9 = deque(maxlen = 60)
##########################################################################
df11 = pd.DataFrame(columns=['time', 'value']) 
x11 = deque(maxlen = 60)
y11 = deque(maxlen = 60)

df12 = pd.DataFrame(columns=['time', 'value']) 
x12 = deque(maxlen = 60)
y12 = deque(maxlen = 60)

df13 = pd.DataFrame(columns=['time', 'value']) 
x13 = deque(maxlen = 60)
y13 = deque(maxlen = 60)

df14 = pd.DataFrame(columns=['time', 'value']) 
x14 = deque(maxlen = 60)
y14 = deque(maxlen = 60)

df15 = pd.DataFrame(columns=['time', 'value']) 
x15 = deque(maxlen = 60)
y15 = deque(maxlen = 60)

df16 = pd.DataFrame(columns=['time', 'value']) 
x16 = deque(maxlen = 60)
y16 = deque(maxlen = 60)

df17 = pd.DataFrame(columns=['time', 'value']) 
x17 = deque(maxlen = 60)
y17 = deque(maxlen = 60)

df18 = pd.DataFrame(columns=['time', 'value']) 
x18 = deque(maxlen = 60)
y18 = deque(maxlen = 60)

df19 = pd.DataFrame(columns=['time', 'value']) 
x19 = deque(maxlen = 60)
y19 = deque(maxlen = 60)

@callback(
 Output("ram-graph", "figure"),
 Output("cpu-graph", "figure"),
 [Input("graph-update4", "n_intervals")],
)
def update_graph4(n):
    data = get_data()
    all_data = asyncio.run(data) 
    ram_data = all_data[0]
    cpu_data = all_data[1]
    
    print(cpu_data)

    global df1
    df1 = pd.concat([df1, pd.DataFrame([ram_data[0]])], ignore_index=True)
    global df2
    df2 = pd.concat([df2, pd.DataFrame([ram_data[1]])], ignore_index=True)
    global df3
    df3 = pd.concat([df3, pd.DataFrame([ram_data[2]])], ignore_index=True)
    global df4
    df4 = pd.concat([df4, pd.DataFrame([ram_data[3]])], ignore_index=True)
    global df5
    df5 = pd.concat([df5, pd.DataFrame([ram_data[4]])], ignore_index=True)
    global df6
    df6 = pd.concat([df6, pd.DataFrame([ram_data[5]])], ignore_index=True)
    global df7
    df7 = pd.concat([df7, pd.DataFrame([ram_data[6]])], ignore_index=True)
    global df8
    df8 = pd.concat([df8, pd.DataFrame([ram_data[7]])], ignore_index=True)
    global df9
    df9 = pd.concat([df9, pd.DataFrame([ram_data[8]])], ignore_index=True)
  
    ############################################################################
    global df11
    df11 = pd.concat([df11, pd.DataFrame([cpu_data[0]])], ignore_index=True)
    global df12
    df12 = pd.concat([df12, pd.DataFrame([cpu_data[1]])], ignore_index=True)
    global df13
    df13 = pd.concat([df13, pd.DataFrame([cpu_data[2]])], ignore_index=True)
    global df14
    df14 = pd.concat([df14, pd.DataFrame([cpu_data[3]])], ignore_index=True)
    global df15
    df15 = pd.concat([df15, pd.DataFrame([cpu_data[4]])], ignore_index=True)
    global df16
    df16 = pd.concat([df16, pd.DataFrame([cpu_data[5]])], ignore_index=True)
    global df17
    df17 = pd.concat([df17, pd.DataFrame([cpu_data[6]])], ignore_index=True)
    global df18
    df18 = pd.concat([df18, pd.DataFrame([cpu_data[7]])], ignore_index=True)
    global df19
    df19 = pd.concat([df19, pd.DataFrame([cpu_data[8]])], ignore_index=True)

  
    a1 = df1['time'].iloc[-1]
    b1 = df1['value'].iloc[-1]
    x1.append(a1)
    y1.append((b1))

    a2 = df2['time'].iloc[-1]
    b2 = df2['value'].iloc[-1]
    x2.append(a2)
    y2.append((b2))

    a3 = df3['time'].iloc[-1]
    b3 = df3['value'].iloc[-1]
    x3.append(a3)
    y3.append((b3))

    a4 = df4['time'].iloc[-1]
    b4 = df4['value'].iloc[-1]
    x4.append(a4)
    y4.append((b4))

    a5 = df5['time'].iloc[-1]
    b5 = df5['value'].iloc[-1]
    x5.append(a5)
    y5.append((b5))

    a6 = df6['time'].iloc[-1]
    b6 = df6['value'].iloc[-1]
    x6.append(a6)
    y6.append((b6))

    a7 = df7['time'].iloc[-1]
    b7 = df7['value'].iloc[-1]
    x7.append(a7)
    y7.append((b7))

    a8 = df8['time'].iloc[-1]
    b8 = df8['value'].iloc[-1]
    x8.append(a8)
    y8.append((b8))

    a9 = df9['time'].iloc[-1]
    b9 = df9['value'].iloc[-1]
    x9.append(a9)
    y9.append((b9))

    #############################################################33
    a11 = df11['time'].iloc[-1]
    b11 = df11['value'].iloc[-1]
    x11.append(a11)
    y11.append((b11))

    a12 = df12['time'].iloc[-1]
    b12 = df12['value'].iloc[-1]
    x12.append(a12)
    y12.append((b12))

    a13 = df13['time'].iloc[-1]
    b13 = df13['value'].iloc[-1]
    x13.append(a13)
    y13.append((b13))

    a14 = df14['time'].iloc[-1]
    b14 = df14['value'].iloc[-1]
    x14.append(a14)
    y14.append((b14))

    a15 = df15['time'].iloc[-1]
    b15 = df15['value'].iloc[-1]
    x15.append(a15)
    y15.append((b15))

    a16 = df16['time'].iloc[-1]
    b16 = df16['value'].iloc[-1]
    x16.append(a16)
    y16.append((b16))

    a17 = df17['time'].iloc[-1]
    b17 = df17['value'].iloc[-1]
    x17.append(a17)
    y17.append((b17))

    a18 = df18['time'].iloc[-1]
    b18 = df18['value'].iloc[-1]
    x18.append(a18)
    y18.append((b18))

    a19 = df19['time'].iloc[-1]
    b19 = df19['value'].iloc[-1]
    x19.append(a19)
    y19.append((b19))



    trace1 = go.Scatter (
        x = list(x1),
        y = list(y1),
        mode="lines",
        name="titan 1",
        line={"color": "rgb(253, 50, 22)", "width" : 2},
    )
    trace11 = go.Scatter (
        x = list(x11),
        y = list(y11),
        mode="lines",
        name="titan 1",
        line={"color": "rgb(253, 50, 22)", "width" : 2},
    )
    fig1 = go.Figure(
        data = [trace1],
        layout = go.Layout()
    )
    fig1.update_layout(title="RAM Usage", yaxis_range=[0, 7500], xaxis_title="Timestamp",
                       yaxis_title="Usage in MB")
   

    fig2 = go.Figure(  
        data = [trace11]
    )
    fig2.update_layout(title="CPU Utilization", xaxis_title="Timestamp", yaxis_title="Average Utilization Percentage")

    print(y11)
    
    return fig1,fig2





