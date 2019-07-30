document.addEventListener("DOMContentLoaded", (event) => {
  const images = ["hello1.jpeg", "hello2.jpeg", "hello3.jpeg", "hello4.jpeg", "hello5.jpeg", "hello6.jpeg"];
  const todaysImage = images[(new Date().getDate() % images.length)];
  const image = document.getElementById("profile");
  image.setAttribute("src", "assets/" + todaysImage);
});

if (["0", "unspecified"].includes(navigator.doNotTrack)) {
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-64774283-2', 'auto');
  ga('send', 'pageview');
}
