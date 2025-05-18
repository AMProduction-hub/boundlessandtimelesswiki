window.addEventListener("DOMContentLoaded", () => {
    const blocks = document.querySelectorAll("blockquote");
  
    blocks.forEach((el) => {
      const text = el.textContent.trim();
      const match = text.match(/^\[!(\w+)\]/i);
      if (match) {
        const type = match[1].toLowerCase();
        el.classList.add("admonition", type);
  
        // Optional: remove [!type] from the first paragraph
        const firstChild = el.querySelector("p");
        if (firstChild) {
          firstChild.innerHTML = firstChild.innerHTML.replace(/\[!\w+\]\s*/, "");
        }
      }
    });
  });
  