# Leap motion basicss
## Requirements
Python 3.8:
- pygame
- socketio
- subprocess (comes with python)

```
pip install pygame
pip install python-socketio
```

Node v12:
- express
- socket.io
- leapjs

```
cd node
npm install

[Leap Motion SDK](https://developer.leapmotion.com/sdk-leap-motion-controller/)
```

## Running
Run `python game.py` from the default dir.


# How it works
The leap motion controller is always hosted on a windows app from Ultraleap. When
supporting their (no longer updated) Javascript API, the app hosts a local server on
port 6437. The javascript library uses that in a `Leap.loop()` function.

To get the data to python, both the Nodejs and Python scripts are connected via
socketio. Node sends the relevant data in an object over the socket, where Python
interprets that and renders it on a `pygame` window.

## What data is shown?
The pygame window shows 3 main variables per hand. The most obvious of which being
the hand position in 3D space, shown left/right by the vertical line, up/down
by the horizontal line, and forward/backwards by the dot representing the hand growing
and shrinking.

Second is the hand rotation. I'm still not exactly sure what each axis represents, but
what is shown is 2 lines for the x and y axis recorded (couldn't find any consistent
physical rotation represented by the z axis). Holding the palm straight out in front
will center the y axis, and rotating your hand about your arm will modify the x axis data.

Last (for now) is the pinch strength. You can change this from pinch to grab strength on lines
`37` and `38` of `node/index.js`. Pinch strength is, for the most part, how close your index
and middle finger are to your thumb. Grab strength is, also for the most part, how close all
your fingers are to your palm *or* thumb. Either of these values are shown by the dot fading
from blue to yellow as the pinch/grip strength increases.