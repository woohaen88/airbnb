### Room

GET POST /room [v]
GET PUT DELETE /room/1 [v]
GET /room/1/amenity [v]
GET /room/1/review [v]
GET POST /room/1/booking
GET PUT DELETE /room/1/booking/2
GET POST /amenity [v]
GET PUT DELETE /amenity/1 [v]
GET POST /room/1/booking

### Experience

GET POST /experience
GET PUT /experience/1
GET /experience/1/perk
GET POST /experience/1/booking
GET PUT DELETE /experience/1/booking/2
GET POST /perk [v]
GET PUT DELETE /perk/1 [v]

### Media

GET POST /photo [v]
GET PUT DELETE /photo/1 []

GET POST /video
GET PUT DELETE /video/1

### Wishlists

GET POST /wishlist [v]
GET PUT DELETE /wishlist/1 [v]
PUT /wishlist/1/room/2 [v]
is_liked [v]
