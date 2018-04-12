CREATE TYPE unit AS ENUM ('Imperial', 'Metric');
CREATE TYPE not AS ENUM ('Text', 'Email', 'Web');

CREATE TABLE IF NOT EXISTS food ( 
    name VARCHAR(100),
    density DOUBLE(10,5),
    caloricDensity DOUBLE(10, 5),
    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS drink (
    name VARCHAR(100),
    density DOUBLE(10,5),
    caloriesPerOZ DOUBLE(10, 5),
    PRIMARY KEY (name)
)

CREATE TABLE IF NOT EXISTS exercise (
    name VARCHAR(100),
    caloriesOverTime INTEGER,
    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS userInformation (
    username VARCHAR(25),
    weight INTEGER,
    height INTEGER,
    gender VARCHAR(25),
    units unit,
    notificationType not,
    phoneNumber VARCHAR(10),
    email VARCHAR(50),
    PRIMARY KEY (username)
);

INSERT INTO food VALUES (Pizza, 1.07, 270);
INSERT INTO food VALUES (Apple, 0.2401, 52);
INSERT INTO food VALUES (Carrot, 0.54, 41.38);
INSERT INTO food VALUES (Twinkie, 0.32, 349);
INSERT INTO food VALUES (Chicken Soup, 1.07, 36);
INSERT INTO food VALUES (White Bread, 0.2, 267);
INSERT INTO food VALUES (Chicken Breast, 0.59, 88);
INSERT INTO food VALUES (Chicken Thigh, 0.59, 88);
INSERT INTO food VALUES (Beef Steak, 1.053, 267);
INSERT INTO food VALUES (Lamb Steak, 1.00, 235);
INSERT INTO food VALUES (Pork Chop, 1.03, 167);
INSERT INTO food VALUES (Salmon Filet, 0.919, 206);
INSERT INTO food VALUES (Baked Potatoes, 0.63, 93);
INSERT INTO food VALUES (Mashed Potatoes, 0.97, 103);
INSERT INTO food VALUES (Spinach, 0.63, 23);
INSERT INTO food VALUES (Lactose Free Ice Cream: Vanilla, 1.096, 211);
INSERT INTO food VALUES (Ice Cream: Vanilla, 1.096, 165);
INSERT INTO food VALUES (Cream Cheese, 1.01, 357);
INSERT INTO food VALUES (Parmesan Cheese, 0.63, 415);
INSERT INTO food VALUES (Egg, 1.00, 143);
INSERT INTO food VALUES (Deviled Egg, 1.00, 160);
INSERT INTO food VALUES (Brocoli, 0.777, 34);
INSERT INTO food VALUES (Lettuce, 0.3, 14);
INSERT INTO food VALUES (Hot Dog, 0.9, 247);
INSERT INTO food VALUES (Avocado, 0.63, 160);
INSERT INTO food VALUES (Pasta, 0.64, 158);
INSERT INTO food VALUES (Choclate Chip Cookie, 0.65, 458);
INSERT INTO food VALUES (Clam Chowder, 1.07, 84);
INSERT INTO food VALUES (Apple Pie, 1.11, 253);

INSERT INTO drink VALUES (Diet Coke, 1.045, 0);
INSERT INTO drink VALUES (Classic Coke, 1.11, 11.83);
INSERT INTO drink VALUES (Water, 1, 0);
INSERT INTO drink VALUES (Lactose Free Milk: Skim, 1.023, 11.25);
INSERT INTO drink VALUES (Apple Juice, 1.05, 14);
INSERT INTO drink VALUES (Orange Juice, 1.25, 14);
INSERT INTO drink VALUES (Wine, 0.98, 24);
INSERT INTO drink VALUES (Margaritas, 0.94, 56.6);
INSERT INTO drink VALUES (Beer, 1.060, 13);
INSERT INTO drink VALUES (Vodka, 0.79, 64);
INSERT INTO drink VALUES (Milk: skim, 1.035, 11.25);
INSERT INTO drink VALUES (Coffee, 1, 0.25);
INSERT INTO drink VALUES (Green Tea, 1, 0.25);
INSERT INTO drink VALUES (Powerade, 1.03, 6.25);

INSERT INTO exercise VALUES (Running, 400);
INSERT INTO exercise VALUES (Swimming, 413);
INSERT INTO exercise VALUES (Hiking, 430);
INSERT INTO exercise VALUES (Walking, 298);
INSERT INTO exercise VALUES (Lifting Weights, 224);
INSERT INTO exercise VALUES (Biking, 450);
INSERT INTO exercise VALUES (Rollerblading, 913);
INSERT INTO exercise VALUES (Skiing: Downhill, 272);
INSERT INTO exercise VALUES (Skiing: Cross Country, 1054);
INSERT INTO exercise VALUES (Yoga, 120);
INSERT INTO exercise VALUES (Pushups, 576);
INSERT INTO exercise VALUES (Crunches, 180);


