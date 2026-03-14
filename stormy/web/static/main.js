const form = document.getElementById('form');
const input = document.getElementById('input');
const messages = document.getElementById('messages');

function addMessage(text, who = 'bot') {
  const div = document.createElement('div');
  div.className = `msg ${who}`;
  div.textContent = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener('submit', async e => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  input.value = '';

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    if (data.error) {
      addMessage('Error: ' + data.error);
    } else {
      addMessage(data.response);
    }
  } catch (err) {
    addMessage('Network error – is the server running?');
  }
});

// Optional: show status on load
fetch('/api/status')
  .then(r => r.json())
  .then(d => console.log('Stormy status:', d));
