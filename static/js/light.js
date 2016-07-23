var socket;
var room = "light";

socket = new io.Socket();
	socket.connect();
	socket.on('connect', function() {
		socket.subscribe(room);
	});
  socket.on('message', function(data) {
    switch (data.action) {
      case 'bcast':
        console.log(data.message)
        break;
      }
    });
