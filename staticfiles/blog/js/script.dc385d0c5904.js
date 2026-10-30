document.addEventListener("DOMContentLoaded", () => {

    const hero = document.querySelector(".hero");

    if (!hero) {
        return; // pages without a hero get no petals
    }

    // Container lives inside the hero, so petals are clipped to the banner
    const petalsContainer = document.createElement("div");
    petalsContainer.className = "hero-petals";
    hero.prepend(petalsContainer);

    function createPetal() {

        const petal = document.createElement("span");
        petal.classList.add("hero-petal");

        const left = Math.random() * hero.offsetWidth;
        const size = Math.random() * 12 + 12;          // 12px - 24px
        const duration = Math.random() * 6 + 8;        // 8s - 14s
        const delay = Math.random() * 2;
        const opacity = Math.random() * 0.4 + 0.5;

        petal.style.left = `${left}px`;
        petal.style.width = `${size}px`;
        petal.style.height = `${size}px`;
        petal.style.opacity = opacity;
        petal.style.animationDuration = `${duration}s`;
        petal.style.animationDelay = `${delay}s`;
        petal.style.setProperty("--fall", `${hero.offsetHeight + 40}px`);

        petalsContainer.appendChild(petal);

        petal.addEventListener("animationend", () => {
            petal.remove();
        });
    }

    // Initial petals (was 30)
    for (let i = 0; i < 8; i++) {
        setTimeout(createPetal, i * 400);
    }

    // Keep creating petals (was every 350ms)
    setInterval(createPetal, 1200);

});