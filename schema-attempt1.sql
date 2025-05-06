-- make sure sqlite enforces foreign key checks
PRAGMA foreign_keys = ON;
CREATE TABLE users (
  id            INTEGER   PRIMARY KEY,
-- ensure role is either student, admin or staff (data entry validation)
  role          VARCHAR   NOT NULL CHECK(role IN ('student','admin','staff')),
  student_email VARCHAR   NOT NULL UNIQUE,
-- upon creation of a user tuple, if created timestamp isn't specified, default to current time
  created_at    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  password_hashed TEXT NOT NULL;
);

CREATE TABLE pois (
  id             INTEGER PRIMARY KEY,
-- could use similar checks a done for role, but we are not yet final on categories
-- using tinyint to save on space (6 catagories, 0-5 is sufficient) 
  item_type      TINYINT,
  mazemap_id     INTEGER,
-- using triggers to only update when necessary 
-- i.e. when a new review is added for a specific type
  reviews_count  INTEGER NOT NULL DEFAULT 0,
  average_score  REAL    NOT NULL DEFAULT 0.0
);

CREATE TABLE reviews (
  id         INTEGER   PRIMARY KEY,
-- when a user or poi is deleted, delete all associated reviews
  user_id    INTEGER   NOT NULL REFERENCES users(id)   ON DELETE CASCADE,
  poi_id     INTEGER   NOT NULL REFERENCES pois(id)    ON DELETE CASCADE,
  title      VARCHAR,
  body       TEXT,
-- more tiny ints, score is 0-5. Sliders arbitrary but likely 0-99 or 0-19
  score      TINYINT   NOT NULL, 
  slider1    TINYINT,
  slider2    TINYINT,
  slider3    TINYINT,
  slider4    TINYINT,

-- checking status is one of the three specified statuses (data entry validation)
-- mainly assisting in ajax, saving progress and etc
-- not relevent currently but good to have
  status     VARCHAR   NOT NULL CHECK(status IN ('pending','approved','rejected')), 
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- using indexes to avoid potential slow downs
CREATE INDEX idx_reviews_user_id ON reviews(user_id);
CREATE INDEX idx_reviews_poi_id  ON reviews(poi_id);

-- after a new review is posted (aka after an INSERT operation), update review count and average scores
CREATE TRIGGER trg_reviews_after_insert
AFTER INSERT ON reviews
FOR EACH ROW
BEGIN
  UPDATE pois
     SET reviews_count = (SELECT COUNT(*) FROM reviews WHERE poi_id = NEW.poi_id),
         average_score = (SELECT AVG(score)  FROM reviews WHERE poi_id = NEW.poi_id)
   WHERE id = NEW.poi_id;
END;

-- similarly to above but recalc on deletion of a single review (aka after delete)
CREATE TRIGGER trg_reviews_after_delete
AFTER DELETE ON reviews
FOR EACH ROW
BEGIN
  UPDATE pois
     SET reviews_count = (SELECT COUNT(*) FROM reviews WHERE poi_id = OLD.poi_id),
         average_score = COALESCE((SELECT AVG(score) FROM reviews WHERE poi_id = OLD.poi_id),0)
   WHERE id = OLD.poi_id;
END;

-- if the poi_id changes, (changing the reference of a specific tuple) recalculate the count and avg scores
CREATE TRIGGER trg_reviews_after_update
AFTER UPDATE OF poi_id,score ON reviews
FOR EACH ROW
BEGIN
  -- old POI
  UPDATE pois
     SET reviews_count = (SELECT COUNT(*) FROM reviews WHERE poi_id = OLD.poi_id),
         average_score = COALESCE((SELECT AVG(score) FROM reviews WHERE poi_id = OLD.poi_id),0)
   WHERE id = OLD.poi_id;
  -- new POI
  UPDATE pois
     SET reviews_count = (SELECT COUNT(*) FROM reviews WHERE poi_id = NEW.poi_id),
         average_score = (SELECT AVG(score) FROM reviews WHERE poi_id = NEW.poi_id)
   WHERE id = NEW.poi_id;
END;
