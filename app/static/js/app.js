const qs = (sel, scope = document) => scope.querySelector(sel);
const qsa = (sel, scope = document) => [...scope.querySelectorAll(sel)];

document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = qs('#theme-toggle');
  const mobileBtn = qs('#mobile-menu-btn');
  const navLinks = qs('#nav-links');
  const currentPage = location.pathname.split('/').pop() || 'index.html';

  if (themeToggle) {
    themeToggle.addEventListener('click', (e) => {
      e.preventDefault();
      const currentTheme = document.documentElement.getAttribute('data-theme');
      document.documentElement.setAttribute('data-theme', currentTheme === 'dark' ? 'light' : 'dark');
      themeToggle.innerHTML = currentTheme === 'dark'
        ? '<i class="fa-solid fa-moon"></i>'
        : '<i class="fa-solid fa-sun"></i>';
    });
  }

  if (mobileBtn && navLinks) {
    mobileBtn.addEventListener('click', () => navLinks.classList.toggle('active'));
    qsa('a', navLinks).forEach((link) => {
      link.addEventListener('click', () => navLinks.classList.remove('active'));
    });
  }

  qsa('.nav-links a').forEach((link) => {
    const href = link.getAttribute('href');
    if (href === currentPage) link.classList.add('active');
    if (currentPage === 'blog-detail.html' && href === 'blog.html') link.classList.add('active');
    if (currentPage === 'mahsulot-detail.html' && href === 'mahsulotlar.html') link.classList.add('active');
    if ((currentPage === 'savatcha.html' || currentPage === 'checkout.html') && href === 'mahsulotlar.html') link.classList.add('active');
  });
});
