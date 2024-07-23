-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS properties;
DROP SEQUENCE IF EXISTS properties_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS properties_id_seq;
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    property VARCHAR(255),
    description VARCHAR,
    location VARCHAR,
    cost INTEGER,
    user_id INTEGER,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INT,
    user_id INT,
    start_date DATE,
    end_date DATE,
    status VARCHAR,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
    UNIQUE (property_id, start_date, end_date)  -- Ensure no overlapping bookings for the same location
);

-- Then we add the FUNCTIONS and TRIGGERS to our database --

-- This creates the database function to check for our overlapping booking --
CREATE OR REPLACE FUNCTION prevent_overlapping_bookings()
RETURNS TRIGGER AS $$
BEGIN
    -- Check for overlapping bookings
    IF EXISTS (
        SELECT 1
        FROM Bookings
        WHERE property_id = NEW.property_id
            AND NEW.start_date < end_date
            AND NEW.end_date > start_date
        LIMIT 1 -- Early exit if any match is found
    ) THEN
        -- Raise an exception if an overlapping booking is found
        RAISE EXCEPTION 'Booking conflict detected for location %', NEW.property_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- This creates a TRIGGER for our database that activates before we INSERT or UPDATE our Bookings table
CREATE TRIGGER check_booking_conflict
BEFORE INSERT ON Bookings
FOR EACH ROW
EXECUTE FUNCTION prevent_overlapping_bookings();


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, password) VALUES ('charlie_roberts23@hotmail.co.uk', 'Password!23');
INSERT INTO users (name, password) VALUES ('taconlin@hotmail.co.uk', 'Password!24');
INSERT INTO users (name, password) VALUES ('joshuadosanjh@gmail.com', 'Qwerty?09');
INSERT INTO users (name, password) VALUES ('charlieroberts201@hotmail.co.uk', 'passWord?12');

INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property1', 'This place is nice', 'test1', '999', '1');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property2', 'This place is okay', 'test2', '888', '1');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property3', 'This place is amazing', 'test3', '777', '2');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property4', 'This place is cool', 'test4', '666', '2');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property5', 'This place is wicked', 'test5', '555', '3');
INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property6', 'This place is rubbish', 'test6', '444', '3');

INSERT INTO bookings (property_id, user_id, start_date, end_date, status) VALUES (1,2,'2025-01-01', '2025-01-08', 'PENDING');
INSERT INTO bookings (property_id, user_id, start_date, end_date, status) VALUES (2,3,'2025-01-01','2025-01-08', 'PENDING');
INSERT INTO bookings (property_id, user_id, start_date, end_date, status) VALUES (3,1,'2025-02-01','2025-02-08', 'PENDING');
INSERT INTO bookings (property_id, user_id, start_date, end_date, status) VALUES (4,4,'2025-02-01','2025-02-08', 'PENDING');
