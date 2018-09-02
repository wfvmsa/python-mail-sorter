create database email;
use email;

CREATE TABLE IF NOT EXISTS devops (
    id INT AUTO_INCREMENT,
    datamail VARCHAR(255),
    origem VARCHAR(255),
    assunto VARCHAR(255),
    PRIMARY KEY (id)
)  ENGINE=INNODB;