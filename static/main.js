const menuButton = document.querySelector("[data-menu-button]");
const menu = document.querySelector("[data-menu]");

menuButton?.addEventListener("click", () => {
  const isOpen = menu.classList.toggle("is-open");
  menuButton.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
});

menu?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => menu.classList.remove("is-open"));
});
