use tubehub;

-- Create users database
CREATE TABLE IF NOT EXISTS `users` (
    `userid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(64) NOT NULL UNIQUE,
    `password` varchar(64) NOT NULL,
    PRIMARY KEY (`userid`)
) engine=innodb;

-- Create video database
CREATE TABLE IF NOT EXISTS `video` (
    `video_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `title` varchar(64) NOT NULL,
    `username` varchar(64) NOT NULL,
    `description` varchar(500) NOT NULL,
    `hash` varchar(64) NOT NULL UNIQUE,
    `filetype` varchar(64) NOT NULL,
    PRIMARY KEY (`video_id`),
    FOREIGN KEY (`username`) REFERENCES users(`username`) ON UPDATE CASCADE
) engine=innodb;

-- Add test user for travis
INSERT INTO `users` (`username`, `password`) VALUES ("pytest", "testpassword")

