from app import db
from app.models import SpotModel, ReviewModel
import random

db.drop_all()
db.create_all()

# Define category IDs
categories = {
    1: "Study",
    2: "Grub",
    3: "Snap",
    4: "Fun",
    5: "Shop",
    6: "Chill"
}

# Rating fields to fill in reviews
rating_fields = [
    'rank_overall', 'rank_comfort', 'rank_noise_level',
    'rank_service_quality', 'rank_value', 'rank_crowdedness',
    'rank_atmosphere', 'rank_accessibility', 'rank_cleanliness'
]

def create_random_review(spot_id):
    review_data = {
        'spot_ID': spot_id,
        'review_text': 'This is a test review.',
    }
    for field in rating_fields:
        review_data[field] = round(random.uniform(3.0, 5.0), 1)  # Ratings between 3.0 and 5.0
    return ReviewModel(**review_data)

for cat_id, cat_name in categories.items():
    for i in range(1, 6):  # 5 spots per category
        spot = SpotModel(
            spot_name=f"{cat_name} Spot {i}",
            category_ID=cat_id
        )
        db.session.add(spot)
        db.session.flush()  # to get spot.spot_ID before commit

        # Add 3 reviews for each spot
        for _ in range(3):
            review = create_random_review(spot.spot_ID)
            db.session.add(review)

db.session.commit()
print("Database seeded successfully with all categories.")
