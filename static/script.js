// Yilni avtomatik yangilash
document.addEventListener("DOMContentLoaded", () => {
  const yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // Tungi/kun rejimi (light/dark theme)
  const root = document.documentElement;
  const themeToggle = document.getElementById("themeToggle");
  const savedTheme = localStorage.getItem("prof-theme");

  if (savedTheme === "dark") {
    root.setAttribute("data-theme", "dark");
    if (themeToggle) themeToggle.textContent = "☀️";
  }

  themeToggle?.addEventListener("click", () => {
    const isDark = root.getAttribute("data-theme") === "dark";
    if (isDark) {
      root.removeAttribute("data-theme");
      localStorage.setItem("prof-theme", "light");
      themeToggle.textContent = "🌙";
    } else {
      root.setAttribute("data-theme", "dark");
      localStorage.setItem("prof-theme", "dark");
      themeToggle.textContent = "☀️";
    }
  });

  // Mobil menyu
  const navToggle = document.getElementById("navToggle");
  const header = document.querySelector(".site-header");

  navToggle?.addEventListener("click", () => {
    header?.classList.toggle("nav-open");
  });

  // Nav elementiga bosilganda menyuni yopish (mobil)
  header?.querySelectorAll(".nav a").forEach((link) => {
    link.addEventListener("click", () => {
      header.classList.remove("nav-open");
    });
  });

  // Formni hozircha faqat console ga chiqarish (backend yo'q)
  const contactForm = document.querySelector(".contact-form");
  contactForm?.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(contactForm);
    console.log("Yangi xabar:", Object.fromEntries(formData.entries()));
    alert("Xabaringiz yuborildi (demo rejim).");
    contactForm.reset();
  });
});

