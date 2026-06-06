const userEmail = "admin";
const userPassword = "1234";

function login() 
{
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let error = document.getElementById("error");

   
    if (email === userEmail && password === userPassword) {
        localStorage.setItem("loggedIn", "true");

        // Flask dashboard
        window.location.href = "/";
    } 
    else {
        error.innerText = "Invalid Username or Password!";
    }
}

function logout()
{
    localStorage.removeItem("loggedIn");

    // Flask login route
    window.location.href = "/login";
}


/* ✅ Protect Dashboard */

if (window.location.pathname === "/") {
    if (localStorage.getItem("loggedIn") !== "true") {
        window.location.href = "/login";
    }
}

function goStudents() {
    window.location.href = "/students";
}


/* ✅ Date & Time */

function updateDateTime() {
    const now = new Date();

    const options = { 
        weekday: 'short', 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    };

    let dateEl = document.getElementById("date");
    let timeEl = document.getElementById("time");

    if(dateEl && timeEl){
        dateEl.innerText = now.toLocaleDateString("en-US", options);
        timeEl.innerText = now.toLocaleTimeString();
    }
}

setInterval(updateDateTime, 1000);
updateDateTime();


/* ✅ Canvas animation safe */

const canvas = document.getElementById("smokeCanvas");

if (canvas) {

    const ctx = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particlesArray = [];
    let mouse = { x: null, y: null };

    window.addEventListener("mousemove", function(event) {
        mouse.x = event.x;
        mouse.y = event.y;

        for (let i = 0; i < 5; i++) {
            particlesArray.push(new Particle());
        }
    });

    class Particle {
        constructor() {
            this.x = mouse.x;
            this.y = mouse.y;
            this.size = Math.random() * 8 + 2;
            this.speedX = Math.random() * 2 - 1;
            this.speedY = Math.random() * 2 - 1;
            this.opacity = 1;
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            this.opacity -= 0.02;
        }

        draw() {
            ctx.fillStyle = "rgba(0, 255, 255," + this.opacity + ")";
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

}
