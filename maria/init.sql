use tubehub;

CREATE TABLE IF NOT EXISTS `users` (
    `userid` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(64) NOT NULL,
    `password` varchar(64) NOT NULL,
    `birthdate` date NOT NULL,
    `email` varchar(64) NOT NULL,
    `sessionid` varchar(64) NOT NULL,
    PRIMARY KEY (`userid`)
) engine=innodb;

CREATE TABLE IF NOT EXISTS `video` (
    `video_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` varchar(64) NOT NULL,
    `userid` int(10) UNSIGNED NOT NULL,
    `description` varchar(64) NOT NULL,
    `location` varchar(64) NOT NULL,
    `filetype` varchar(64) NOT NULL,
    `url` varchar(64) NOT NULL,
    PRIMARY KEY (`video_id`),
    FOREIGN KEY (userid) REFERENCES users(userid) ON UPDATE CASCADE
) engine=innodb;
