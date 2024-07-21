USE gymalytics-db;

CREATE TABLE exercises (
    id INT,
    name varchar(255),
    description varchar(1023),
    main_muscle_group varchar (255),
    bodyweight boolean,
    image_url varchar(1023),
    category enum('calisthenics','bodybuilding','powerlifting'),
    PRIMARY KEY (id)
);

CREATE TABLE sets (
    id INT,
    user_id INT,
    exercise_id INT,
    session_id INT,
    reps INT,
    rest_time_seconds INT,
    weight float,
);

CREATE TABLE sessions (
    id INT PRIMARY KEY AUTO INCREMENT,
    user_id varchar(255),
    date timestamp
);

CREATE TABLE users (
    id INT PRIMARY KEY AUTO INCREMENT,
    name varchar(255),
    encrypted_pw text,
    last_name varchar(255),
    age int,
    description varchar(1023) DEFAULT "",
    preferred_category enum('calisthenics','bodybuilding','powelifting'),
    weight float,
    level enum('beginner','intermediate','advanced')
    profile_picture_url varchar(1023)
);