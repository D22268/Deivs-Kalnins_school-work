
CREATE DATABASE IF NOT EXISTS `rental`;

USE `rental`;

select * FROM Renter;
/*
CREATE TABLE IF NOT EXISTS `Renter` (
    `Renter_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` CHAR(25) NOT NULL,
    `Surname` CHAR(25) NOT NULL,
    `Personal_id_num` CHAR(25) NOT NULL,
    `Phone_num` CHAR(15) NOT NULL
);
CREATE TABLE IF NOT EXISTS `Categories` (
    `Category_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    `Category` CHAR(25) NOT NULL
);

CREATE TABLE IF NOT EXISTS `Rent` (
    `Rent_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Renter_id` INT UNSIGNED,
    `Rent_cost` INT NOT NULL,
    FOREIGN KEY (Renter_id) REFERENCES Renter(Renter_id)
);

CREATE TABLE IF NOT EXISTS `Tool_storage` (
    `Tool_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Amount_stored` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Rented_tool` (
    `Tool_id` INT UNSIGNED,
    `Tool_name` CHAR(25) NOT NULL,
    `Rent_id` INT UNSIGNED,
    `Category_id` INT UNSIGNED,
    `Instrument_loss_cost` INT NOT NULL,
    FOREIGN KEY (Tool_id) REFERENCES Tool_storage(Tool_id),
    FOREIGN KEY (Rent_id) REFERENCES Rent(Rent_id),
    FOREIGN KEY (Category_id) REFERENCES Categories(Category_id) 
);*/