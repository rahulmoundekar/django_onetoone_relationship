# django_onetoone_relationship
django_onetoone_relationship Database table Queries

        DROP TABLE IF EXISTS `djangoapp`.`person`;
        CREATE TABLE  `djangoapp`.`person` (
          `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
          `name` varchar(45) NOT NULL,
          `mobile` varchar(45) NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

        DROP TABLE IF EXISTS `djangoapp`.`license`;
        CREATE TABLE  `djangoapp`.`license` (
          `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
          `license_number` varchar(45) NOT NULL,
          `issue_date` datetime NOT NULL,
          `expiry_date` datetime NOT NULL,
          `person_id` int(10) unsigned NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
