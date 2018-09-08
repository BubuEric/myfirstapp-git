# Host: localhost  (Version 5.7.22-log)
# Date: 2018-09-08 18:42:46
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
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

#
# Data for table "tagname"
#

INSERT INTO `tagname` VALUES (1,'最新电影','2018-09-08 15:03:41',1),(2,'在线电影','2018-09-08 15:04:06',1),(3,'网盘资源','2018-09-08 15:04:35',1),(4,'BT资源','2018-09-08 15:04:45',1),(5,'生肉资源','2018-09-08 15:04:53',1),(6,'欧美剧','2018-09-08 15:05:16',2),(7,'韩剧','2018-09-08 15:05:25',2),(8,'日剧','2018-09-08 15:05:29',2),(9,'国产剧','2018-09-08 15:05:34',2),(10,'动漫','2018-09-08 15:05:38',2),(11,'纪录片','2018-09-08 15:05:47',2),(12,'字幕组','2018-09-08 15:06:59',3),(13,'资讯','2018-09-08 15:07:07',3),(14,'影视大v','2018-09-08 15:07:16',3),(15,'影视工具','2018-09-08 15:07:24',3),(16,'网络小说','2018-09-08 15:07:53',4),(17,'电子书','2018-09-08 15:08:00',4),(18,'有声读物','2018-09-08 15:08:08',4),(19,'漫画','2018-09-08 15:08:14',4),(20,'杂志','2018-09-08 15:08:19',4),(21,'文字社区','2018-09-08 15:08:25',4),(22,'在线音乐','2018-09-08 15:08:44',5),(23,'高清MV','2018-09-08 15:08:54',5),(24,'音乐下载','2018-09-08 15:09:02',5),(25,'音乐社区','2018-09-08 15:09:08',5),(26,'知识文库','2018-09-08 15:09:23',6),(27,'在线课程','2018-09-08 15:09:30',6),(28,'考研','2018-09-08 15:09:37',6),(29,'学习英语','2018-09-08 15:09:43',6),(30,'高清图库','2018-09-08 15:09:53',7),(31,'图标','2018-09-08 15:10:00',7),(32,'字体','2018-09-08 15:10:06',7),(33,'音效','2018-09-08 15:10:16',7),(34,'简历模板','2018-09-08 15:10:25',7),(35,'PPT模板','2018-09-08 15:10:34',7),(36,'灵感创意','2018-09-08 15:10:41',7),(37,'软件应用','2018-09-08 15:10:57',8),(38,'在线工具','2018-09-08 15:11:05',8),(39,'图片工具','2018-09-08 15:11:12',8),(40,'GIF工具','2018-09-08 15:11:19',8),(41,'斗图工具','2018-09-08 15:11:33',8),(42,'PDF工具','2018-09-08 15:11:38',8),(43,'公共场合不宜','2018-09-08 15:11:57',9),(44,'内涵社区','2018-09-08 15:12:04',9),(45,'你懂得','2018-09-08 15:12:09',9);

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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

#
# Data for table "tagurl"
#

INSERT INTO `tagurl` VALUES (1,'老司机电影网','http://www.lsjdyw.net/','2018-09-08 16:14:48',1),(2,'电影首发站','http://www.dysfz.cc/','2018-09-08 16:15:12',1),(3,'骑士影院','http://www.74zu.com/','2018-09-08 16:24:06',2),(4,'去转盘','http://www.quzhuanpan.com/','2018-09-08 16:25:10',3),(5,'磁力猫','https://www.cilimao.me/','2018-09-08 16:25:33',4),(6,'rarbg','https://rarbg.is/torrents.php','2018-09-08 16:26:09',4),(7,'人人影视','http://www.zimuzu.io/','2018-09-08 16:27:04',6),(8,'韩饭网','http://www.hanfan.cc/hanju/','2018-09-08 16:28:11',7),(9,'追新番','http://zhuixinfan.com/main.php','2018-09-08 16:28:47',8),(10,'猪猪日部落','http://www.zzrbl.com/','2018-09-08 16:29:08',8),(11,'6V国剧','http://www.6vhao.tv/dlz/','2018-09-08 17:11:08',9),(12,'A站','http://www.acfun.cn/','2018-09-08 17:11:29',10),(13,'B站','https://www.bilibili.com/','2018-09-08 17:11:45',10),(14,'纪录片天地','http://www.jlpcn.net/','2018-09-08 17:12:06',11),(15,'知轩藏书','http://www.zxcs8.com/','2018-09-08 17:12:58',11),(16,'追书神器','http://www.zhuishushenqi.com/','2018-09-08 17:13:33',17);
