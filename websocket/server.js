const WebSocket = require('ws');  // Import the 'ws' library

// Create WebSocket servers on localhost:4000 for 'pick' and 'timer' consumers
const wss = new WebSocket.Server({ port: 4000 });

wss.on('connection', socket => {
    socket.on('message', message => {
        wss.clients.forEach(client => {
            if (client.readyState === WebSocket.OPEN) {
              client.send(message);
            }
          });
    });
});
