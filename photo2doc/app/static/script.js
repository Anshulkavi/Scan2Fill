document.getElementById('uploadForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const formData = new FormData();
  formData.append('file', document.getElementById('formImage').files[0]);

  const res = await fetch('/upload', {
    method: 'POST',
    body: formData
  });

  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  window.open(url);
});
