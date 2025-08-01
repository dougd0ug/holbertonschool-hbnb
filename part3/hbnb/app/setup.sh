#!/bin/bash

API_URL="http://127.0.0.1:5000/api/v1"

# === Utilisateur propriétaire ===
EMAIL="owner@example.com"
PASSWORD="helloworld"
FIRST_NAME="John"
LAST_NAME="Doe"
IS_ADMIN=true

# === Utilisateur reviewer ===
REVIEWER_EMAIL="reviewer@example.com"
REVIEWER_PASSWORD="pass1234"
REVIEWER_FIRST_NAME="Alice"
REVIEWER_LAST_NAME="Smith"

# === Utilisateur admin ===
ADMIN_EMAIL="admin@example.com"
ADMIN_PASSWORD="adminpass"

# Helper pour extraire les IDs
extract_id() {
  echo "$1" | grep -o '"id":[^,}]*' | cut -d':' -f2 | tr -d '" '
}

# === Création Owner ===
echo "🧑 Creating owner user..."
OWNER_RESPONSE=$(curl -s -X POST "$API_URL/users/" \
  -H "Content-Type: application/json" \
  -d "{\"first_name\":\"$FIRST_NAME\", \"last_name\":\"$LAST_NAME\", \"email\":\"$EMAIL\", \"password\":\"$PASSWORD\", \"is_admin\":\"$IS_ADMIN\"}")
USER_ID=$(extract_id "$OWNER_RESPONSE")
echo "✅ Owner ID: $USER_ID"

echo "🔐 Logging in as owner..."
AUTH_RESPONSE=$(curl -s -X POST "$API_URL/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$EMAIL\", \"password\":\"$PASSWORD\"}")
ACCESS_TOKEN=$(echo "$AUTH_RESPONSE" | grep -oP '"access_token"\s*:\s*"\K[^"]+')
echo "✅ Owner token retrieved"

# === Création Reviewer ===
echo "🧑 Creating reviewer user..."
REVIEWER_RESPONSE=$(curl -s -X POST "$API_URL/users/" \
  -H "Content-Type: application/json" \
  -d "{\"first_name\":\"$REVIEWER_FIRST_NAME\", \"last_name\":\"$REVIEWER_LAST_NAME\", \"email\":\"$REVIEWER_EMAIL\", \"password\":\"$REVIEWER_PASSWORD\"}")
REVIEWER_ID=$(extract_id "$REVIEWER_RESPONSE")
echo "✅ Reviewer ID: $REVIEWER_ID"

echo "🔐 Logging in as reviewer..."
REVIEWER_AUTH=$(curl -s -X POST "$API_URL/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$REVIEWER_EMAIL\", \"password\":\"$REVIEWER_PASSWORD\"}")
REVIEWER_TOKEN=$(echo "$REVIEWER_AUTH" | grep -oP '"access_token"\s*:\s*"\K[^"]+')
echo "✅ Reviewer token retrieved"

# === Création Admin ===
echo "👑 Creating admin user via /users/..."
ADMIN_RESPONSE=$(curl -s -X POST "$API_URL/users/" \
  -H "Content-Type: application/json" \
  -d "{\"first_name\": \"Admin\", \"last_name\": \"User\", \"email\": \"$ADMIN_EMAIL\", \"password\": \"$ADMIN_PASSWORD\"}")
ADMIN_ID=$(extract_id "$ADMIN_RESPONSE")
echo "✅ Admin created with ID: $ADMIN_ID"


# === Reconnexion pour obtenir un vrai token admin ===
echo "🔐 Re-logging in as admin to get updated token..."
ADMIN_AUTH_RESPONSE=$(curl -s -X POST "$API_URL/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$ADMIN_EMAIL\", \"password\":\"$ADMIN_PASSWORD\"}")
ADMIN_TOKEN=$(echo "$ADMIN_AUTH_RESPONSE" | grep -oP '"access_token"\s*:\s*"\K[^"]+')
echo "✅ Admin token retrieved: $ADMIN_TOKEN"

# === Lister tous les utilisateurs ===
echo "📋 Listing all users as admin..."
curl -s -X GET "$API_URL/admin/" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json"
echo ""

# === Modifier un utilisateur ===
echo "✏️ Updating reviewer user with admin rights..."
curl -s -X PUT "$API_URL/admin/users/$REVIEWER_ID" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"first_name\": \"AliceUpdated\",
    \"last_name\": \"Smith\",
    \"email\": \"$REVIEWER_EMAIL\",
    \"password\": \"$REVIEWER_PASSWORD\",
    \"is_admin\": false
  }"
echo ""

# === Supprimer un utilisateur ===
echo "🗑 Deleting reviewer user with admin rights..."
curl -s -X DELETE "$API_URL/admin/users/$REVIEWER_ID" \
  -H "Authorization: Bearer $ADMIN_TOKEN"
echo ""

# === Création d’un Amenity ===
echo "📶 Creating amenity..."
AMENITY_RESPONSE=$(curl -s -X POST "$API_URL/amenities/" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "WiFi"}')
AMENITY_ID=$(extract_id "$AMENITY_RESPONSE")
echo "✅ Amenity created: $AMENITY_ID"

# === Création d’un Place ===
echo "🏠 Creating place..."
PLACE_RESPONSE=$(curl -s -X POST "$API_URL/places/" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"My Beautiful Place\",
    \"description\": \"Nice view and great WiFi\",
    \"price\": 120,
    \"latitude\": 48.8566,
    \"longitude\": 2.3522,
    \"owner_id\": \"$USER_ID\",
    \"amenities\": [\"$AMENITY_ID\"]
  }")
PLACE_ID=$(echo "$PLACE_RESPONSE" | grep -oP '"id"\s*:\s*"\K[^"]+')
echo "✅ PLACE ID: $PLACE_ID"

# === Détails du lieu ===
echo "🔍 Getting place details..."
curl -s -X GET "$API_URL/places/$PLACE_ID" -H "Authorization: Bearer $ACCESS_TOKEN"
echo ""

# === Création Review ===
echo "📝 Creating review..."
REVIEW_CREATE_RESPONSE=$(curl -s -X POST "$API_URL/reviews/" \
  -H "Authorization: Bearer $REVIEWER_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"text\": \"Amazing place!\",
    \"rating\": 5,
    \"place_id\": \"$PLACE_ID\",
    \"user_id\": \"$REVIEWER_ID\"
  }")
REVIEW_ID=$(extract_id "$REVIEW_CREATE_RESPONSE")
echo "✅ Review created: $REVIEW_ID"
echo "Review response:"
echo "$REVIEW_CREATE_RESPONSE"

# === Mise à jour Review ===
echo "🔄 Updating review..."
REVIEW_UPDATE_RESPONSE=$(curl -s -X PUT "$API_URL/reviews/$REVIEW_ID" \
  -H "Authorization: Bearer $REVIEWER_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"text\": \"Updated review text\",
    \"rating\": 4
  }")
echo "Review update response:"
echo "$REVIEW_UPDATE_RESPONSE"

# === Suppression Review ===
echo "🗑 Deleting review..."
REVIEW_DELETE_RESPONSE=$(curl -s -X DELETE "$API_URL/reviews/$REVIEW_ID" \
  -H "Authorization: Bearer $REVIEWER_TOKEN")
echo "Review delete response:"
echo "$REVIEW_DELETE_RESPONSE"

# === Mise à jour Place ===
echo "🔁 Updating place..."
UPDATE_RESPONSE=$(curl -s -X PUT "$API_URL/places/$PLACE_ID" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"Updated Place Title\",
    \"description\": \"Encore plus beau\",
    \"price\": 200.0,
    \"latitude\": 48.8566,
    \"longitude\": 2.3522,
    \"owner_id\": \"$USER_ID\",
    \"amenities\": [\"$AMENITY_ID\"]
  }")
UPDATED_TITLE=$(echo "$UPDATE_RESPONSE" | grep -oP '"title"\s*:\s*"\K[^"]+')
if [ -z "$UPDATED_TITLE" ]; then
  echo "❌ Failed to update place"
  echo "$UPDATE_RESPONSE"
else
  echo "✅ Place updated: $UPDATED_TITLE"
fi
