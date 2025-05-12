from app import db, application  # import your Flask app and db
from app.models import UserModel, CategoryModel, SpotModel, ReviewModel
from datetime import date
import random

with application.app_context():
    # Optional: clear existing data
    ReviewModel.query.delete()
    SpotModel.query.delete()
    UserModel.query.delete()
    CategoryModel.query.delete()
    db.session.commit()

    # Insert categories
    category_data = [
        CategoryModel(name="study", total_likes=0),
        CategoryModel(name="grub", total_likes=0),
        CategoryModel(name="snap", total_likes=0),
        CategoryModel(name="fun", total_likes=0)
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

    # Insert spots (only for snap and fun)
    snap_fun_spots = []
    for category_id in [3, 4]:  # 3 = snap, 4 = fun
        for i in range(5):
            spot = SpotModel(
                spot_name=f"{'Snap' if category_id == 3 else 'Fun'} Spot {i + 1}",
                category_ID=category_id,
                locationx=random.uniform(115.8, 115.9),
                locationy=random.uniform(-31.9, -31.95),
                description=f"Great place for {'photos' if category_id == 3 else 'fun'}!",
                num_likes=random.randint(0, 50)
            )
            snap_fun_spots.append(spot)
    db.session.add_all(snap_fun_spots)
    db.session.commit()

    # Insert reviews
    all_users = UserModel.query.all()
    all_spots = SpotModel.query.all()
    reviews = []
    for spot in all_spots:
        for _ in range(3):
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
