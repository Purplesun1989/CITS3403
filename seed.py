from app import db, application
from app.models import UserModel, CategoryModel, SpotModel, ReviewModel
from datetime import date
import random

with application.app_context():
    # Clear existing data
    ReviewModel.query.delete()
    SpotModel.query.delete()
    UserModel.query.delete()
    CategoryModel.query.delete()
    db.session.commit()

    # Insert categories
    category_data = [
        CategoryModel(name="Shop", total_likes=0),
        CategoryModel(name="grub", total_likes=0),
        CategoryModel(name="snap", total_likes=0),
        CategoryModel(name="fun", total_likes=0),
        CategoryModel(name="chill", total_likes=0),
        CategoryModel(name="study", total_likes=0),
    ]
    db.session.add_all(category_data)
    db.session.commit()

    # Insert users
    users = []
    for i in range(5):
        user = UserModel(
            username=f"user{i}",
            uwa_email=f"user{i}@student.uwa.edu.au",
            password_hash="hashed_pw",
            age=random.randint(18, 30),
            birthday=date(2000 + i % 5, 1 + i % 12, 1 + i % 28),
            gender=random.choice(["Male", "Female", "Other"])
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    # Map category names to their IDs
    categories = {cat.name.lower(): cat.category_ID for cat in CategoryModel.query.all()}

    # Insert spots for each category
    spots = []
    for category_name in ['snap', 'fun', 'grub', 'shop', 'chill', 'study']:
        for i in range(5):
            spot = SpotModel(
                spot_name=f"{category_name.capitalize()} Spot {i + 1}",
                category_ID=categories[category_name],
                locationx=random.uniform(115.8, 115.9),
                locationy=random.uniform(-31.9, -31.95),
                description=f"Nice place for {category_name}.",
                num_likes=random.randint(0, 50)
            )
            spots.append(spot)
    db.session.add_all(spots)
    db.session.commit()

    # Insert reviews
    all_users = UserModel.query.all()
    all_spots = SpotModel.query.all()
    reviews = []
    for spot in all_spots:
        for _ in range(3):  # at least 3 reviews per spot
            ranks = {
                "rank_cleanliness": random.randint(1, 5),
                "rank_atmosphere": random.randint(1, 5),
                "rank_comfort": random.randint(1, 5),
                "rank_accessibility": random.randint(1, 5),
                "rank_value": random.randint(1, 5),
                "rank_service_quality": random.randint(1, 5),
                "rank_noise_level": random.randint(1, 5),
                "rank_crowdedness": random.randint(1, 5),
            }
            overall = round(sum(ranks.values()) / len(ranks))
            user = random.choice(all_users)
            review = ReviewModel(
                spot_ID=spot.spot_ID,
                user_id=user.id,
                text="Nice spot!",
                rank_overall=overall,
                **ranks
            )
            reviews.append(review)
    db.session.add_all(reviews)
    db.session.commit()

    print("✅ Seeded database with categories, users, spots, and reviews!")

