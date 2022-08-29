(function () {
  const elements = document.querySelectorAll("[data-trigger-nav]");
  const handler = () => {
    elements.forEach((element) => {
      const rect = element.getBoundingClientRect();
      const isInViewport =
        rect.top <= document.documentElement.clientHeight / 2 &&
        rect.bottom >= document.documentElement.clientHeight / 2;

      document
        .querySelectorAll(
          `nav a[href='#${element.getAttribute("data-trigger-nav")}']`
        )
        .forEach((element) => {
          element.classList.toggle("active", isInViewport);
        });
    });
  };
  document.addEventListener("scroll", handler);
  window.addEventListener("DOMContentLoaded", handler);
})();
