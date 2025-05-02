# minicluster-dashboard

## Summary
This project is a real-time dashboard that displays the RAM and CPU usage collected from a cluster of Jetson Orin Nanos. 
The project is split into two programs (each folder is a program):  home server, titan-server.  
This project was created on VSCode and it uses mainly python and its libraries. 


### Home Server
  - This is a Plotly Dash (DashProxy) application. It displays two graphs: RAM and CPU Usage graphs.
  - It is a multipage application and to run it -- type this command into the terminal: python3 main-server.py

 - File described:
   - main-server.py: Creates the dash app, sets up the composion, and runs it. 
   - navbar.py: creates a general format for the navigation bar that is displayed throughout the webpage
   - pages folder:
     - home.py: takes in data from the titan-server program through a websocket, creates the layout of the home page, includes the graphs, and the dataframes that store the data.

### Titan-server
 - This is a Quart application that uses parse function to parse through tegrastats collected from the demo and is sent through a websocket to the home server program
 - To run this program:
   1. Make sure the computer that is running the fluid simulation has the titan-server.py script
   2. Pull up the terminal and type in the command: tegrastats | python3 titan-server.py
      
 - File described:
   - titan-server.py: takes in the tegrastats from the titans and is parsed and send through a socket to the middle_man program. 
