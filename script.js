function toggleFields() {
  const mode = document.getElementById('mode').value;
  const shiftField = document.getElementById('shift');
  shiftField.style.display = (mode === 'caesar') ? 'block' : 'none';
}

function submitForm() {
  const mode = document.getElementById('mode').value;
  const message = document.getElementById('message').value.trim();
  const shift = document.getElementById('shift').value;
  const output = document.getElementById('output');

  if (!message) {
    output.innerText = "Please enter a message.";
    return;
  }

  const payload = {
    mode: mode,
    message: message
  };

  if (mode === 'caesar') {
    if (!shift || isNaN(shift)) {
      output.innerText = "Please enter a valid shift value for Caesar cipher.";
      return;
    }
    payload.shift = parseInt(shift);
  }

  fetch('/encrypt', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
    .then(res => res.json())
    .then(data => {
      if (data.status === 'success') {
        if (data.mode === 'fernet') {
          output.innerText = `🔐 Fernet Encryption\n\nEncrypted Message:\n${data.encrypted}\n\nAPI Key:\n${data.key}`;
        } else {
          output.innerText = `🔑 Caesar Cipher\n\nOriginal Message: ${data.original}\nEncrypted Message: ${data.encrypted}\nDecrypted Message: ${data.decrypted}\nShift: ${data.shift}`;
        }
      } else {
        output.innerText = "Error: " + data.message;
      }
    })
    .catch(err => {
      output.innerText = "Error communicating with server.";
      console.error(err);
    });
}
