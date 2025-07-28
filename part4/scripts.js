/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    const logoutBtn = document.getElementById('logout-button');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            document.cookie = 'token=; Max-Age=0; path=/';
            window.location.href = 'login.html';
        });
    }

    // Exemple pour loginLink et logoutButton dans checkAuthentication
    checkAuthentication();
  });

  // Login configuration

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

// Place by filter configuration

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
    if (!placesList) return;
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
            <button class="view-details-btn">View Details</button>
        `;

        placeCard.querySelector('.view-details-btn').addEventListener('click', () => {
         // Redirige vers place.html avec l'id en query param
        window.location.href = `place.html?id=${place.id}`;
        });

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

// Place details

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            displayPlaceDetails(data);
        } else {
            console.error('Failed to fetch place details:', response.status);
        }
    } catch (error) {
        console.error('Error fetching place details:', error);
    }
}

function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');
    placeDetails.innerHTML = ''; // clear

    const title = document.createElement('h2');
    title.textContent = place.title;

    const desc = document.createElement('p');
    desc.textContent = place.description;

    const price = document.createElement('p');
    price.textContent = `Price: $${place.price}`;

    const location = document.createElement('p');
    location.textContent = `Location: (${place.latitude}, ${place.longitude})`;

    // Optionally display amenities
    const amenities = document.createElement('ul');
    amenities.textContent = "Amenities:";
    (place.amenities || []).forEach(a => {
        const item = document.createElement('li');
        item.textContent = a;
        amenities.appendChild(item);
    });

    placeDetails.appendChild(title);
    placeDetails.appendChild(desc);
    placeDetails.appendChild(price);
    placeDetails.appendChild(location);
    placeDetails.appendChild(amenities);
}

document.addEventListener('DOMContentLoaded', () => {
    const placeId = getPlaceIdFromURL();

    if (placeId) {
        checkAuthForPlaceDetails(placeId);  // page place.html
    } else if (document.getElementById('places-list')) {
        checkAuthentication(); // page index.html
    }
});


function checkAuthForPlaceDetails(placeId) {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        if (addReviewSection) addReviewSection.style.display = 'none';
        fetchPlaceDetails(null, placeId);
    } else {
        if (addReviewSection) addReviewSection.style.display = 'block';
        fetchPlaceDetails(token, placeId);
    }
}

function checkAuthReview() {
    const token = getCookie('token');
    if (!token) {
        window.location.href = 'index.html';
    }
    return token;
}

async function submitReview(token, placeId, reviewText) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/reviews/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                place_id: placeId,
                text: reviewText
            })
        });

        if (response.ok) {
            alert('Review submitted successfully!');
            document.getElementById('review-form').reset();
        } else {
            const error = await response.json();
            alert('Failed to submit review: ' + (error.message || response.statusText));
        }
    } catch (error) {
        alert('Error submitting review: ' + error.message);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const token = checkAuthReview();
    const placeId = getPlaceIdFromURL();
    const reviewForm = document.getElementById('review-form');

    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const reviewTextarea = document.getElementById('review-text');
            if (!reviewTextarea) return;

            const reviewText = reviewTextarea.value;

            if (!reviewText) {
                alert('Please write a review before submitting.');
                return;
            }

            await submitReview(token, placeId, reviewText);
        });
    }
});
