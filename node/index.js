const Leap = require('leapjs')
var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

var init = true
var count = 0;
app.get('/', (req, res) => {
  res.send();
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

http.listen(3000, () => {
  console.log('listening on *:3000');
});

var controller = Leap.loop({enableGestures:true}, function(frame){
  if (init) {
    if (frame.hands[0]){
    //    console.log(frame.hands[0].indexFinger)
    var previousFrame = controller.frame(1);
    pos = frame.hands[0].palmPosition
    update_pos(pos)
    //init = false
      }
  }
});

function update_pos(pos) {
  if (count < 2) {
    count++;
  }
  else if (count == 2) {
    console.log(pos)
    io.emit('position_update', pos)
    count = 0
  }
}