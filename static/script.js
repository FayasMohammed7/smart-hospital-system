async function sendOTP() {
  const phone = document.getElementById("phone").value;
  const res = await fetch("/send-otp", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone }),
  });
  const data = await res.json();
  document.getElementById("response").innerText = data.message;
}

async function verifyOTP() {
  const phone = document.getElementById("phone").value;
  const otp = document.getElementById("otp").value;
  const res = await fetch("/verify-otp", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone, otp }),
  });
  const data = await res.json();
  if (data.redirect) {
    window.location.href = data.redirect;
  } else {
    document.getElementById("response").innerText = data.message;
  }
}
