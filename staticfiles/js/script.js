// ===========================================
// Japan & Sri Lanka Hero Slider
// ===========================================

document.addEventListener("DOMContentLoaded", function () {

    const hero = document.querySelector(".hero-banner");
    const title = document.querySelector(".hero-content h1");
    const subtitle = document.querySelector(".hero-content p");

    if (!hero || !title || !subtitle) return;

    const slides = [

        {
            image: "/static/blog/img/japan1.jpg",
            title: "Discover Japan",
            text: "Experience timeless temples, cherry blossoms and the beauty of Mount Fuji."
        },

        {
            image: "/static/blog/img/japan2.jpg",
            title: "Cherry Blossom Paradise",
            text: "Walk beneath pink sakura trees and enjoy unforgettable spring landscapes."
        },

        {
            image: "/static/blog/img/japan3.jpg",
            title: "Modern Japan",
            text: "Explore vibrant cities where innovation meets centuries of tradition."
        },

        {
            image: "/static/blog/img/japan4.jpg",
            title: "Japanese Culture",
            text: "Discover ancient shrines, peaceful gardens and authentic traditions."
        },

        {
            image: "/static/blog/img/japan5.jpg",
            title: "Adventure in Japan",
            text: "Travel through breathtaking mountains, lakes and hidden villages."
        },

        {
            image: "/static/blog/img/srilanka1.jpg",
            title: "Welcome to Sri Lanka",
            text: "Discover tropical beaches, lush forests and rich cultural heritage."
        },

        {
            image: "/static/blog/img/srilanka2.jpg",
            title: "Golden Beaches",
            text: "Relax beside crystal-clear oceans with endless sunshine and palm trees."
        },

        {
            image: "/static/blog/img/srilanka3.jpg",
            title: "Nature & Wildlife",
            text: "Meet elephants, leopards and colorful birds in beautiful national parks."
        },

        {
            image: "/static/blog/img/srilanka4.jpg",
            title: "Tea Country",
            text: "Journey through green tea plantations and cool mountain landscapes."
        },

        {
            image: "/static/blog/img/srilanka5.jpg",
            title: "Ancient Sri Lanka",
            text: "Explore Sigiriya, ancient kingdoms and UNESCO World Heritage sites."
        }

    ];

    let current = 0;

    function changeSlide() {

        hero.style.opacity = "0";

        setTimeout(function () {

            hero.style.backgroundImage = `url('${slides[current].image}')`;

            title.textContent = slides[current].title;

            subtitle.textContent = slides[current].text;

            hero.style.opacity = "1";

            current++;

            if (current >= slides.length) {
                current = 0;
            }

        }, 600);

    }

    hero.style.transition = "all 1s ease";

    changeSlide();

    setInterval(changeSlide, 5000);

});