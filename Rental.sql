CREATE DATABASE IF NOT EXISTS `Rental`;

USE `Rental`;

CREATE TABLE `Renter` (
    `Renter_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` CHAR(25) NOT NULL,
    `Surname` CHAR(25) NOT NULL,
    `Personal_id_num` CHAR(25) NOT NULL,
    `Phone_num` CHAR(15) NOT NULL
);

CREATE TABLE `Rented_tool` (
    `Tool_id` INT,
    `Tool_name` CHAR(25) NOT NULL,
    `Rent_id` INT,
    `Category_id` INT,
    `Instrument_loss_cost` INT NOT NULL,
    FOREIGN KEY (Tool_id) REFERENCES Tool_storage(Tool_id),
    FOREIGN KEY (Rent_id) REFERENCES Rent(Rent_id),
    FOREIGN KEY (Category_id) REFERENCES Categories(Category_id), 
    FOREIGN KEY (Tool_id) REFERENCES Tool_storage(Tool_id)
);

CREATE TABLE `Categories` (
    `Category_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    `Category` CHAR(25) NOT NULL
);

CREATE TABLE `Rent` (
    `Rent_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Renter_id` INT,
    `Rent_cost` INT NOT NULL,
    FOREIGN KEY (Renter_id) REFERENCES Renter(Renter_id)
);
CREATE TABLE `Tool_storage` (
    `Tool_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Amount_stored` INT NOT NULL
);
