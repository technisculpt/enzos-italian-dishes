// Photo lightbox (with swipe on phones) and the print button.
(function () {
  const dialog = document.querySelector(".lightbox");
  const photos = Array.from(document.querySelectorAll("img[data-lightbox]"));
  if (dialog && photos.length && typeof dialog.showModal === "function") {
    const big = dialog.querySelector("img");
    const caption = dialog.querySelector("figcaption");
    let index = 0;

    const show = (i) => {
      index = (i + photos.length) % photos.length;
      const img = photos[index];
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      const fig = img.closest("figure");
      const cap = fig && fig.querySelector("figcaption");
      caption.textContent = cap ? cap.textContent : img.alt;
    };

    photos.forEach((img, i) => {
      img.tabIndex = 0;
      img.setAttribute("role", "button");
      const open = () => { show(i); dialog.showModal(); };
      img.addEventListener("click", open);
      img.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); }
      });
    });

    dialog.querySelector(".lb-close").addEventListener("click", () => dialog.close());
    dialog.querySelector(".lb-prev").addEventListener("click", () => show(index - 1));
    dialog.querySelector(".lb-next").addEventListener("click", () => show(index + 1));
    dialog.addEventListener("click", (e) => { if (e.target === dialog) dialog.close(); });
    dialog.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") show(index - 1);
      if (e.key === "ArrowRight") show(index + 1);
    });

    let startX = null;
    dialog.addEventListener("touchstart", (e) => { startX = e.touches[0].clientX; }, { passive: true });
    dialog.addEventListener("touchend", (e) => {
      if (startX === null) return;
      const dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 50) show(index + (dx < 0 ? 1 : -1));
      startX = null;
    });
  }

  document.querySelectorAll("[data-print]").forEach((b) => b.addEventListener("click", () => window.print()));
})();
