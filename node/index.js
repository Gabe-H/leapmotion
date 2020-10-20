const Leap = require('leapjs')
var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.send();
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

http.listen(3000, () => {
  console.log('listening on *:3000');
});

Leap.loop({enableGestures:true}, function(frame){
  data = [
    {
      position: [0,0,0],
      side: null,
      grip: 0,
      valid: null,
      palmNormal: [0, 0, 0]
    },
    {
      position: [0,0,0],
      side: null,
      grip: 0,
      valid: null,
      palmNormal: [0, 0, 0]
    }
  ]
  for (i=0; i<frame.hands.length; i++) {
      data[i]['position'] = frame.hands[i].palmPosition
      data[i]['grip'] = frame.hands[i].grabStrength
      data[i]['side'] = frame.hands[i].type
      data[i]['palmNormal'] = frame.hands[i].palmNormal
  }
  update_pos(data)
});

function update_pos(data) {
  io.emit('position_update', data)
}