from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
	return"""Q. What is linux?
A. A Linux is an open-source OS (operating system) widely used in servers and cloud environment.
Q. Can you elaborate ps aux data?
A. ps aux shows all the running proccesses in the system
 👉Sample Output 

   USER  PID  %CPU  %MEM  VSZ     RSS    TTY    STAT  START  TIME  COMMAND   
   root  1234  0.1  1.2   50000   12000   ?     S    10:00   0:01  nginx
   user  5678  5.0  2.5   150000  50000  pts/0  R+   10:05   0:10  app.py 

- USER: Who started the proccess 
 root => system
 user => you 
- PID: (proccess ID) Most important. Unique number for each proccess 
Example:5678.
oyu use this to kill proccess and Track proccess 
- %CPU: How much CPU it is using 
high => heavy process 
low => normal 
- %MEM: Memory usage 
 helps find Memory leaks and heavy apps 
- COMMAND: (Very Important) what is actually running 
Example: nginx => web-server 
         python-app => your app
- VSZ: (Virtual memory Size) Total virtual memory proccess has access to (in KB)
it is used in DevOps to see how much memory a proccess could potentially consume.
-RSS- Resident Set Size: Actual physical RAM the proccess is using (in KB)
it is used in DevOps to find memory-heavy apps and to debug memory leaks. 
-TTY- Terminal Type: Terminal attached to the proccess 
? => no termianl (background proccess) 
pts/0 => Terminal session 
it is used in DevOps to see if proccess is started by user or background job. 
-STAT- Proccess state: Current status of proccess 
STAT  MEANING 
R     Running 
S     Sleeping (waiting)
D     Uninterruptible sleep (usally I/O)
Z     Zombie (dead, not cleaned)
T     Stopped (manual or trace)
+     In foreground proeccess group 
DevOps Tip: 
R => actively runnign CPU
S => normal background sleep 
Z => problem (zombie proccess neeeds cleanup)
Q. What is kubernetes ?
A. kubernetes is a container orchestration tool used to manage, scale and update the applications"""

app.run(host="0.0.0.0", port=5000)
 
