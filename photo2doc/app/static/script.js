// document.getElementById('uploadForm').addEventListener('submit', async function(e) {
//   e.preventDefault();

//   const formData = new FormData();
//   formData.append('file', document.getElementById('formImage').files[0]);

//   const res = await fetch('/upload', {
//     method: 'POST',
//     body: formData
//   });

//   const blob = await res.blob();
//   const url = URL.createObjectURL(blob);
//   window.open(url);
// });


document.getElementById('uploadForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const formData = new FormData();
  const fileInput = document.getElementById('formImage');
  if (!fileInput.files.length) return alert("Please select a file.");

  formData.append('file', fileInput.files[0]);

  const res = await fetch('/upload', {
    method: 'POST',
    body: formData
  });

  const data = await res.json();
  document.getElementById("resultText").textContent = data.extracted_text || `Error: ${data.error}`;
});
