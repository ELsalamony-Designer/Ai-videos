function generateVideo() {
  const prompt = document.getElementById('prompt').value;
  const image = document.getElementById('imageInput').files[0];
  const formData = new FormData();
  formData.append("prompt", prompt);
  if (image) {
    formData.append("image", image);
  }

  fetch("http://localhost:5000/generate", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    const video = document.createElement("video");
    video.src = data.video_url;
    video.controls = true;
    video.width = 400;

    const container = document.getElementById("videoResult");
    container.innerHTML = "";
    container.appendChild(video);
  });
}
