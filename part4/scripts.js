// main function to check wich page to handle, and handle logout button if the user is connected or not

document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname;

    if (path.endsWith('index.html') || path === '/' || path.endsWith('/')) {
        handleIndexPage();
    } else if (path.endsWith('login.html')) {
        handleLoginPage();
    } else if (path.endsWith('place.html')) {
        handlePlaceDetailsPage();
    }

    const logoutBtn = document.getElementById('logout-button');
    const loginLink = document.getElementById('login-link');
    const token = getCookie('token');

    if (logoutBtn) {
        if (token) {
            logoutBtn.style.display = 'block';
        } else {
            logoutBtn.style.display = 'none';
        }

        logoutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            document.cookie = 'token=; Max-Age=0; path=/';
            window.location.href = 'login.html';
        });
    }

    if (loginLink) {
        if (token) {
            loginLink.style.display = 'none';
        } else {
            loginLink.style.display = 'block';
        }
    }
});

// function to get cookie of identification

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

// function to handle Login Page, check if the email and password submitted match an user, if yes, the user
// is redirected on home page. To login you have to put your email and password

function handleLoginPage() {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            try {
                const response = await loginUser(email, password);
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
}

// function to authentificate the user and use the method POST

async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    });
    return response;
}

// function to handle Index Page if the user is connected. It can fetch places and filter places by price

function handleIndexPage() {
    const token = getCookie('token');

    if (token) {
        fetchPlaces(token);
    }

    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', (event) => {
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
    }
}

// function to fetch places from database

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) throw new Error('Failed to fetch places');

        const data = await response.json();
        displayPlaces(data);
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

// function to display places in the front, and go to the details place if you click on the button

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = '';
    places.forEach(place => {
        const card = document.createElement('div');
        card.className = 'place-card';
        card.setAttribute('data-price', place.price);
        
        let amenitiesText = 'No amenities';
        if (Array.isArray(place.amenities) && place.amenities.length > 0) {
            const amenityNames = place.amenities.map(a => a.name);
            amenitiesText = amenityNames.join(', ');
        }

        card.innerHTML = `
            <h3>${place.title}</h3>
            
            <p><strong>Price:</strong> $${place.price}</p>
            
            <p><strong>Amenities:</strong> ${amenitiesText}</p>
            <button class="view-details-btn">View Details</button>
        `;

        card.querySelector('.view-details-btn').addEventListener('click', () => {
            window.location.href = `place.html?id=${place.id}`;
        });
        placesList.appendChild(card);
    });
}

// function to handle Place Details on the page of the place. You have te review form to post a review too

function handlePlaceDetailsPage() {
    const placeId = getPlaceIdFromURL();
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');

    if (!placeId) return;

    if (token) {
        if (addReviewSection) addReviewSection.style.display = 'block';
        fetchPlaceDetails(token, placeId);
    } else {
        if (addReviewSection) addReviewSection.style.display = 'none';
        fetchPlaceDetails(null, placeId);
    }

    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const reviewText = document.getElementById('review-text').value.trim();
            const ratingStr = document.getElementById('review-rating').value;
            const rating = parseInt(ratingStr);

            if (!reviewText) {
                alert('Please write a review before submitting.');
                return;
            }
            if (isNaN(rating) || rating < 1 || rating > 5) {
                alert('Please select a valid rating between 1 and 5.');
                return;
            }

            await submitReview(token, placeId, reviewText, rating);
        });
    }
}

// function to pick place ID from the URL

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

// function to fetch Place Details from the database, is the token is authorize

async function fetchPlaceDetails(token, placeId) {
  try {
    const headers = {
      'Content-Type': 'application/json'
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
      method: 'GET',
      headers: headers
    });

    if (!response.ok) {
      console.error('Failed to fetch place details:', response.status);
      return;
    }

    const data = await response.json();
    console.log('Place details:', data);
    displayPlaceDetails(data);
  } catch (error) {
    console.error('Error fetching place details:', error);
  }
}

// function to display PLace details on the Place page


function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');
    placeDetails.innerHTML = '';

    placeDetails.innerHTML = `
    <h2>${place.title}</h2>
    <p>${place.description}</p>
    <p>Price: $${place.price}</p>
    <p>Location: (${place.latitude}, ${place.longitude})</p>
    `;

    if (Array.isArray(place.amenities) && place.amenities.length > 0) {
        const amenityNames = place.amenities.map(a => a.name);
        const amenitiesText = amenityNames.join(', ');

        const amenitiesSection = document.createElement('p');
        amenitiesSection.innerHTML = `<strong>Amenities:</strong> ${amenitiesText}`;
        placeDetails.appendChild(amenitiesSection);
    }

    // reviews
    const reviewContainer = document.getElementById('review-container');
    if (reviewContainer) {
        reviewContainer.innerHTML = '';

        if (place.reviews && place.reviews.length > 0) {
            place.reviews.forEach(review => {
                const reviewDiv = document.createElement('div');
                reviewDiv.classList.add('review');

                reviewDiv.innerHTML = `
                    <p><strong>${review.username || review.user_id || 'Anonymous'}</strong></p>
                    <p>Rating: ${review.rating}</p>
                    <p>${review.text}</p>
                    <br>
                `;

                reviewContainer.appendChild(reviewDiv);
            });
        } else {
            const noReviews = document.createElement('p');
            noReviews.textContent = 'No reviews yet.';
            reviewContainer.appendChild(noReviews);
        }
    }
}

// function which handle the Review form on the place page and the add_review page

async function submitReview(token, placeId, reviewText, rating) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/reviews/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ place_id: placeId, text: reviewText, rating: rating })
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
