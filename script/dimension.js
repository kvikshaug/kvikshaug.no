(function () {
  const image = document.querySelector("img.hello");
  if (image) {
    const threshold = 5;

    image.addEventListener("mousemove", (event) => {
      const { clientX, clientY, currentTarget } = event;
      const { clientWidth, clientHeight, offsetLeft, offsetTop } =
        currentTarget;
      const horizontal = (clientX - offsetLeft) / clientWidth;
      const vertical = (clientY - offsetTop) / clientHeight;

      const rotateX = (threshold / 2 - horizontal * threshold).toFixed(2);
      const rotateY = (vertical * threshold - threshold / 2).toFixed(2);
      if (image.style.transition) {
        image.style.transition = null;
      }
      image.style.transform = `perspective(${clientWidth}px) rotateX(${rotateY}deg) rotateY(${rotateX}deg) scale3d(1, 1, 1)`;
    });

    image.addEventListener("mouseleave", (event) => {
      image.style.transition = "0.1s ease-in-out transform";
      image.style.transform = `perspective(${event.currentTarget.clientWidth}px) rotateX(0deg) rotateY(0deg)`;
    });
  }
})();
