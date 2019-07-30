document.addEventListener("DOMContentLoaded", (event) => {
  const images = ["hello1.jpeg", "hello2.jpeg", "hello3.jpeg", "hello4.jpeg", "hello5.jpeg", "hello6.jpeg"];
  const todaysImage = images[(new Date().getDate() % images.length)];
  const image = document.getElementById("profile");
  image.setAttribute("src", "assets/" + todaysImage);
});
