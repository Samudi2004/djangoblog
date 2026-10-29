document.addEventListener("DOMContentLoaded", () => {

    const petalsContainer = document.getElementById("petals");

    if (!petalsContainer) {
        console.warn("Petals container not found.");
        return;
    }

    function createPetal() {

        const petal = document.createElement("span");
        petal.classList.add("petal");

        // Random position
        const left = Math.random() * window.innerWidth;

        // Random size (14px - 32px)
        const size = Math.random() * 18 + 14;

        // Random animation duration (8s - 14s)
        const duration = Math.random() * 6 + 8;

        // Random delay
        const delay = Math.random() * 2;

        // Random opacity
        const opacity = Math.random() * 0.5 + 0.5;

        // Random rotation
        const rotate = Math.random() * 360;

        petal.style.left = `${left}px`;
        petal.style.width = `${size}px`;
        petal.style.height = `${size}px`;
        petal.style.opacity = opacity;
        petal.style.animationDuration = `${duration}s`;
        petal.style.animationDelay = `${delay}s`;
        petal.style.transform = `rotate(${rotate}deg)`;

        petalsContainer.appendChild(petal);

        petal.addEventListener("animationend", () => {
            petal.remove();
        });

    }

    // Initial petals
    for (let i = 0; i < 30; i++) {
        setTimeout(createPetal, i * 180);
    }

    // Keep creating petals
    setInterval(createPetal, 350);

});