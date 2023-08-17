const { exec } = require('child_process');

const backend = exec('pip install -r requirements.txt && python3 ./backend/manage.py runserver 3000');
const frontend = exec('cd frontend && npm install && npm run dev');
const webSocket = exec('cd websocket && npm install && node server.js');

webSocket.stdout.on('data', (data) => {
  console.log(`Websocket server output: ${data}`);
});

webSocket.stderr.on('data', (data) => {
  console.log(`Websocket server error: ${data}`);
});

backend.stdout.on('data', (data) => {
  console.log(`Backend server output: ${data}`);
});

backend.stderr.on('data', (data) => {
  console.log(`Backend server error: ${data}`);
});

frontend.stdout.on('data', (data) => {
  console.log(`Vue server output: ${data}`);
});

frontend.stderr.on('data', (data) => {
  console.error(`Vue server error: ${data}`);
});
