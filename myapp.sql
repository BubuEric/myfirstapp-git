# Host: localhost  (Version 5.7.22-log)
# Date: 2018-09-07 19:39:41
# Generator: MySQL-Front 5.4  (Build 4.153) - http://www.mysqlfront.de/

/*!40101 SET NAMES utf8 */;

#
# Structure for table "admin"
#

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_admin_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "admin"
#

INSERT INTO `admin` VALUES (1,'eric','pbkdf2:sha256:50000$ZuWZc1mz$cc0dd22a9dc5d15cfe45c5537927ccffba5dbc40a99b001ea7463326d1b7cbf7','2018-09-04 18:50:32');

#
# Structure for table "blog"
#

DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `ix_blog_addtime` (`addtime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "blog"
#


#
# Structure for table "tag"
#

DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `num` bigint(20) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_tag_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

#
# Data for table "tag"
#

INSERT INTO `tag` VALUES (1,'电影资源',1,'2018-09-07 17:13:29'),(2,'电视剧资源',2,'2018-09-07 17:24:08'),(3,'影视周边',3,'2018-09-07 17:24:22'),(4,'阅读',4,'2018-09-07 17:24:49'),(5,'音乐',5,'2018-09-07 17:25:04'),(6,'学习园地',6,'2018-09-07 17:25:13'),(7,'模板素材',7,'2018-09-07 17:25:35'),(8,'软件工具',8,'2018-09-07 17:25:48'),(9,'福利小站',9,'2018-09-07 17:25:59');

#
# Structure for table "tagname"
#

DROP TABLE IF EXISTS `tagname`;
CREATE TABLE `tagname` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `tag_id` (`tag_id`),
  KEY `ix_tagname_addtime` (`addtime`),
  CONSTRAINT `tagname_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "tagname"
#


#
# Structure for table "tagurl"
#

DROP TABLE IF EXISTS `tagurl`;
CREATE TABLE `tagurl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `tagname_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `tagname_id` (`tagname_id`),
  KEY `ix_tagurl_addtime` (`addtime`),
  CONSTRAINT `tagurl_ibfk_1` FOREIGN KEY (`tagname_id`) REFERENCES `tagname` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "tagurl"
#

