const { exec } = require('child_process');

const backend = exec('pip install -r requirements.txt && python ./backend/manage.py runserver 3000');
const frontend = exec('cd frontend && npm install && npm run dev');

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
