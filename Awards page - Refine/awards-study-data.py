from exts import db;
from models import reviewstModel;


# Add data
review_25_1 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Super quiet and peaceful — ideal for solo study sessions.",
    rank_cleanliness=9,
    rank_atmosphere=10,
    rank_comfort=8,
    rank_accessibility=8,
    rank_value=9,
    rank_service_quality=0,  # Not applicable
    rank_noise_level=1,
    rank_crowdedness=2,
    rank_overall=9
)

review_25_2 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Great natural light and comfy chairs. Gets a bit busy mid-afternoon.",
    rank_cleanliness=8,
    rank_atmosphere=9,
    rank_comfort=9,
    rank_accessibility=8,
    rank_value=9,
    rank_service_quality=0,
    rank_noise_level=3,
    rank_crowdedness=5,
    rank_overall=8
)

review_25_3 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Power outlets at every table! Perfect for long laptop sessions.",
    rank_cleanliness=8,
    rank_atmosphere=8,
    rank_comfort=7,
    rank_accessibility=9,
    rank_value=8,
    rank_service_quality=0,
    rank_noise_level=2,
    rank_crowdedness=3,
    rank_overall=8
)

review_25_4 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Nice and cool even on hot days. Great airflow and lighting.",
    rank_cleanliness=9,
    rank_atmosphere=9,
    rank_comfort=8,
    rank_accessibility=7,
    rank_value=8,
    rank_service_quality=0,
    rank_noise_level=2,
    rank_crowdedness=3,
    rank_overall=9
)

review_25_5 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Wi-Fi is fast and reliable. One of my top picks to revise in peace.",
    rank_cleanliness=8,
    rank_atmosphere=9,
    rank_comfort=9,
    rank_accessibility=8,
    rank_value=9,
    rank_service_quality=0,
    rank_noise_level=2,
    rank_crowdedness=4,
    rank_overall=9
)

review_25_6 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="The perfect mix of silence and occasional background hum. Zero distractions.",
    rank_cleanliness=9,
    rank_atmosphere=10,
    rank_comfort=8,
    rank_accessibility=9,
    rank_value=9,
    rank_service_quality=0,
    rank_noise_level=1,
    rank_crowdedness=2,
    rank_overall=10
)

review_25_7 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Tables are slightly small for group study, but great for individuals.",
    rank_cleanliness=7,
    rank_atmosphere=8,
    rank_comfort=7,
    rank_accessibility=8,
    rank_value=7,
    rank_service_quality=0,
    rank_noise_level=2,
    rank_crowdedness=3,
    rank_overall=7
)

review_25_8 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="Lighting is adjustable and soft — helps me focus longer.",
    rank_cleanliness=8,
    rank_atmosphere=9,
    rank_comfort=8,
    rank_accessibility=9,
    rank_value=8,
    rank_service_quality=0,
    rank_noise_level=2,
    rank_crowdedness=3,
    rank_overall=9
)

review_25_9 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="A little far from main campus, but worth it for the quiet.",
    rank_cleanliness=8,
    rank_atmosphere=9,
    rank_comfort=7,
    rank_accessibility=6,
    rank_value=8,
    rank_service_quality=0,
    rank_noise_level=2,
    rank_crowdedness=2,
    rank_overall=8
)

review_25_10 = reviewstModel(
    spot_ID=25,
    user_id=1,
    text="No interruptions and very respectful vibe. Would recommend for cramming days.",
    rank_cleanliness=9,
    rank_atmosphere=10,
    rank_comfort=9,
    rank_accessibility=9,
    rank_value=9,
    rank_service_quality=0,
    rank_noise_level=1,
    rank_crowdedness=1,
    rank_overall=10
)

db.session.add(review_25_1, review_25_2, review_25_3, review_25_4,
               review_25_5, review_25_6, review_25_7, review_25_8,
               review_25_9, review_25_10)
db.session.commit()

print("Award added!")

