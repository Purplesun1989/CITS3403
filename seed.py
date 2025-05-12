from app import db, application
from app.models import UserModel, CategoryModel, SpotModel, ReviewModel
from datetime import date
import random

with application.app_context():
    # Clear all data
    db.session.query(ReviewModel).delete()
    db.session.query(SpotModel).delete()
    db.session.query(UserModel).delete()
    db.session.query(CategoryModel).delete()
    db.session.commit()

    # Define fixed categories (with specific IDs and neutral order)
    category_definitions = [
        (1, "study"),
        (2, "grub"),
        (3, "snap"),
        (4, "fun"),
        (5, "shop"),
        (6, "chill"),
    ]
    categories = [CategoryModel(category_ID=cid, name=name, total_likes=0) for cid, name in category_definitions]
    db.session.add_all(categories)
    db.session.commit()

    # Insert 5 users
    users = []
    for i in range(5):
        user = UserModel(
            username=f"user{i}",
            uwa_email=f"user{i}@student.uwa.edu.au",
            password_hash="hashed_pw",
            age=random.randint(18, 30),
            birthday=date(2000 + i % 5, 1 + i % 12, 1 + i % 28),
            gender=random.choice(["Male", "Female", "Other"]),
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    # Map category names to IDs
    category_map = {name: cid for cid, name in category_definitions}

    # Add 5 spots per category with neutral names
    all_spots = []
    spot_counter = 1
    for cat_name, cat_id in category_map.items():
        for _ in range(5):
            spot = SpotModel(
                spot_name=f"Spot {spot_counter}",
                category_ID=cat_id,
                locationx=random.uniform(115.8, 115.9),
                locationy=random.uniform(-31.9, -31.95),
                description="A great spot!",
                num_likes=random.randint(0, 50),
            )
            all_spots.append(spot)
            spot_counter += 1
    db.session.add_all(all_spots)
    db.session.commit()

    # Add 5 reviews per spot
    all_users = UserModel.query.all()
    spots = SpotModel.query.all()
    reviews = []
    for spot in spots:
        for _ in range(5):
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

    print("✅ Seeded database with neutral spot names, 30 spots, and 150 reviews!")


