create database MomadeCuisines;
use MomadeCuisines;
show tables;
CREATE TABLE Users (
    user_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL, -- Store hashed passwords
    role ENUM('customer','cook', 'admin') NOT NULL DEFAULT 'customer', -- Role: customer or admin
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL unique,
	otp VARCHAR(6) DEFAULT NULL,
    otp_expires_at TIMESTAMP NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Packages (
    package_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    package_type ENUM('Breakfast', 'Lunch', 'Dinner') NOT NULL,
    package_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    package_id BIGINT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_date DATE NOT NULL, -- The date the meal is to be delivered
    order_status ENUM('Pending', 'Confirmed', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (package_id) REFERENCES Packages(package_id)
);

CREATE TABLE Payments (
    payment_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    user_id BIGINT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('QR Code', 'Bank Account') NOT NULL,
    payment_status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
    zakpay_transaction_id VARCHAR(100), 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Contact_Messages (
    message_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT, -- Optional, if the user is logged in
    phone_number VARCHAR(15) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

select* from users;

