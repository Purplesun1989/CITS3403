from exts import db;
from models import reviewstModel;

# Add data
review1 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Delicious food and quick service. Will definitely come back!",
    rank_cleanliness=8,
    rank_atmosphere=7,
    rank_comfort=7,
    rank_accessibility=9,
    rank_value=9,
    rank_service_quality=8,
    rank_noise_level=6,
    rank_crowdedness=5,
    rank_overall=8
)

review2 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Nice spot for a casual bite. Portions are generous.",
    rank_cleanliness=7,
    rank_atmosphere=8,
    rank_comfort=6,
    rank_accessibility=8,
    rank_value=9,
    rank_service_quality=7,
    rank_noise_level=5,
    rank_crowdedness=6,
    rank_overall=8
)

review3 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Clean and cozy space, great noodles and very flavorful broth.",
    rank_cleanliness=9,
    rank_atmosphere=8,
    rank_comfort=8,
    rank_accessibility=7,
    rank_value=8,
    rank_service_quality=9,
    rank_noise_level=4,
    rank_crowdedness=3,
    rank_overall=9
)

review4 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Efficient service and a good variety of vegetarian options.",
    rank_cleanliness=8,
    rank_atmosphere=7,
    rank_comfort=7,
    rank_accessibility=9,
    rank_value=8,
    rank_service_quality=8,
    rank_noise_level=5,
    rank_crowdedness=4,
    rank_overall=8
)

review5 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="The lunch special was a great deal and very tasty.",
    rank_cleanliness=7,
    rank_atmosphere=6,
    rank_comfort=6,
    rank_accessibility=8,
    rank_value=9,
    rank_service_quality=7,
    rank_noise_level=6,
    rank_crowdedness=5,
    rank_overall=8
)

review6 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Well-lit, airy dining area and polite staff. Highly recommend the dumplings!",
    rank_cleanliness=9,
    rank_atmosphere=9,
    rank_comfort=8,
    rank_accessibility=8,
    rank_value=8,
    rank_service_quality=9,
    rank_noise_level=4,
    rank_crowdedness=3,
    rank_overall=9
)

review7 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Affordable and quick, but the portion size was a bit small for the price.",
    rank_cleanliness=8,
    rank_atmosphere=7,
    rank_comfort=7,
    rank_accessibility=4,
    rank_value=2,
    rank_service_quality=7,
    rank_noise_level=6,
    rank_crowdedness=3,
    rank_overall=7)

review8 = reviewstModel(
    spot_ID=16,
    user_id=1,
    text="Great atmosphere and friendly staff.",
    rank_cleanliness=9,
    rank_atmosphere=8,
    rank_comfort=8,
    rank_accessibility=7,
    rank_value=8,
    rank_service_quality=9,
    rank_noise_level=5,
    rank_crowdedness=4,
    rank_overall=8
)
db.session.add(review1, review2, review3, review4, review5, review6, review7, review8)
db.session.commit()

review_17_1 = reviewstModel(
    spot_ID=17,
    user_id=1,
    text="A cozy spot with great coffee and light snacks. Perfect for a quiet break.",
    rank_cleanliness=8,
    rank_atmosphere=9,
    rank_comfort=8,
    rank_accessibility=8,
    rank_value=7,
    rank_service_quality=8,
    rank_noise_level=3,
    rank_crowdedness=2,
    rank_overall=8
)

review_17_2 = reviewstModel(
    spot_ID=17,
    user_id=1,
    text="The croissants were fresh and buttery. Staff were attentive.",
    rank_cleanliness=9,
    rank_atmosphere=8,
    rank_comfort=8,
    rank_accessibility=9,
    rank_value=8,
    rank_service_quality=9,
    rank_noise_level=4,
    rank_crowdedness=3,
    rank_overall=9
)

review_17_3 = reviewstModel(
    spot_ID=17,
    user_id=1,
    text="Lovely little café with a warm vibe. Not ideal if you're in a rush though.",
    rank_cleanliness=7,
    rank_atmosphere=9,
    rank_comfort=7,
    rank_accessibility=8,
    rank_value=7,
    rank_service_quality=6,
    rank_noise_level=4,
    rank_crowdedness=3,
    rank_overall=7
)

review_17_4 = reviewstModel(
    spot_ID=17,
    user_id=1,
    text="Comfortable seating and top-notch hot chocolate. Great hangout spot.",
    rank_cleanliness=8,
    rank_atmosphere=8,
    rank_comfort=9,
    rank_accessibility=8,
    rank_value=8,
    rank_service_quality=9,
    rank_noise_level=3,
    rank_crowdedness=2,
    rank_overall=9
)
db.session.add(review_17_1, review_17_2, review_17_3, review_17_4)
db.session.commit()

review_18_1 = reviewstModel(
    spot_ID=18,
    user_id=1,
    text="Plenty of options but can get noisy during peak hours.",
    rank_cleanliness=7,
    rank_atmosphere=6,
    rank_comfort=6,
    rank_accessibility=9,
    rank_value=8,
    rank_service_quality=7,
    rank_noise_level=7,
    rank_crowdedness=8,
    rank_overall=7
)

review_18_2 = reviewstModel(
    spot_ID=18,
    user_id=1,
    text="Tried the ramen and it was flavorful. Fast service even when busy.",
    rank_cleanliness=8,
    rank_atmosphere=7,
    rank_comfort=6,
    rank_accessibility=9,
    rank_value=9,
    rank_service_quality=8,
    rank_noise_level=6,
    rank_crowdedness=7,
    rank_overall=8
)

review_18_3 = reviewstModel(
    spot_ID=18,
    user_id=1,
    text="Good food variety, but the tables could be cleaner.",
    rank_cleanliness=6,
    rank_atmosphere=6,
    rank_comfort=5,
    rank_accessibility=8,
    rank_value=8,
    rank_service_quality=7,
    rank_noise_level=7,
    rank_crowdedness=7,
    rank_overall=7
)

review_18_4 = reviewstModel(
    spot_ID=18,
    user_id=1,
    text="Great value for the price. The burger joint there is a must-try.",
    rank_cleanliness=7,
    rank_atmosphere=6,
    rank_comfort=6,
    rank_accessibility=8,
    rank_value=9,
    rank_service_quality=8,
    rank_noise_level=6,
    rank_crowdedness=6,
    rank_overall=8
)
db.session.add(review_18_1, review_18_2, review_18_3, review_18_4)
db.session.commit()

