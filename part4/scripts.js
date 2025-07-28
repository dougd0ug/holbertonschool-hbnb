/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('logout-button').addEventListener('click', (e) => {
    e.preventDefault();
    document.cookie = 'token=; Max-Age=0; path=/';
    window.location.href = 'login.html';
    });
  });

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            // Your code to handle form submission
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            try {
                const response = await loginUser(email, password);
                console.log("ok");
                if (response.ok) {
                    const data = await response.json();
                    document.cookie = `token=${data.access_token}; path=/`;
                    window.location.href = 'index.html';
                } else {
                    alert('Login failed: ' + response.statusText);
                }
                } catch (error) {
                    alert("Connexion error.");
                }
        });
    }
});

async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });
    // Handle the response
    return response;
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }

    const logoutButton = document.getElementById('logout-button');

    if (!token) {
        loginLink.style.display = 'block';
        logoutButton.style.display = 'none';
    } else {
        loginLink.style.display = 'none';
        logoutButton.style.display = 'block';
        fetchPlaces(token);
}
}

function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [key, value] = cookie.trim().split('=');
        if (key === name) {
            return value;
        }
    }
    return null;
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch places');
        }

        const data = await response.json();
        console.log('Places fetched:', data);
        displayPlaces(data);
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = '';

    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.classList.add('place-card');
        placeCard.setAttribute('data-price', place.price); // For filtering

        placeCard.innerHTML = `
            <h3>${place.title}</h3>
            <p>${place.description}</p>
            <p><strong>Price:</strong> $${place.price}</p>
            <p><strong>Location:</strong> ${place.location || 'Unknown'}</p>
        `;

        placesList.appendChild(placeCard);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();

    document.getElementById('price-filter').addEventListener('change', (event) => {
        const selectedPrice = event.target.value;
        const places = document.querySelectorAll('.place-card');

        places.forEach(place => {
            const price = parseFloat(place.getAttribute('data-price'));

            if (selectedPrice === 'All' || price <= parseFloat(selectedPrice)) {
                place.style.display = 'block';
            } else {
                place.style.display = 'none';
            }
        });
    });
});
