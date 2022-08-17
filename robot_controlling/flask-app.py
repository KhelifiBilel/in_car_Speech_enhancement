from flask import Flask
import time
import robot  #configuration of GPIOs(rapsberry pi) to control motors
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello'


@app.route('/forward')
def forward():
	print("Forward!")
	robot.fwd()	# Send the robot Forward
	time.sleep(2)
	return 'Alexabot moved forward!'


@app.route('/backward')
def backward():
	print("Backward!")
	robot.bwd()	# Send the robot Backward
	time.sleep(2)
	return 'Alexabot moved Backward!'


@app.route('/stop')
def stop():
	print("Stop!")
	robot.stop()
	time.sleep(1)
	return 'Stopped!'


@app.route('/right')
def right():
	print("Right!")
	robot.right()
	time.sleep(1)
	return 'Alexabot moved Right!'


@app.route('/left')
def left():
	print("Left!")
	robot.left()
	time.sleep(1)
	return 'Alexabot moved Left!'

@app.route('/blue')
def blue():
	print("Blue Light!")
	robot.blue()
	time.sleep(1)
	return 'Blue Light!'


@app.route('/green')
def green():
	print("Green Light!")
	robot.green()
	time.sleep(1)
	return 'Green Light!'


@app.route('/lightoff')
def light_off():
	print("Turning light off!")
	robot.light_off()
	time.sleep(1)
	return 'turning the light off!'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
