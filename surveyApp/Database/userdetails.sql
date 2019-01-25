-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: bkbase
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `userdetails`
--

DROP TABLE IF EXISTS `userdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `userdetails` (
  `username` text,
  `email` text,
  `department` text,
  `company` text,
  `password` text,
  `isValid` text,
  `survey` varchar(40) DEFAULT NULL,
  `activateSurvey` varchar(10) DEFAULT NULL,
  `role` varchar(30) DEFAULT NULL,
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdetails`
--

LOCK TABLES `userdetails` WRITE;
/*!40000 ALTER TABLE `userdetails` DISABLE KEYS */;
INSERT INTO `userdetails` VALUES ('sachin1','1@gmail','Deco','surveyy1','default123','False','comp','False','Manager',1),('sachin10','10@gmail','Adv','surveyy1','default123','False','comp','False','Sr.Manager',2),('sachin11','11@gmail','Adv','surveyy1','default123','False','comp','False','Sr.Manager',3),('sachin12','12@gmail','Adv','surveyy1','default123','False','comp','False','Sr.Manager',4),('sachin13','13@gmail','Adv','surveyy1','default123','False','comp','False','Sr.Manager',5),('sachin14','14@gmail','Trade','surveyy1','default123','False','comp','False','Sr.Manager',6),('sachin15','15@gmail','Deco','surveyy1','default123','False','comp','False','Sr.Manager',7),('sachin16','16@gmail','CSG','surveyy1','default123','False','comp','False','Lead',8),('sachin17','17@gmail','CCB','surveyy1','default123','False','comp','False','Lead',9),('sachin18','18@gmail','CSG','surveyy1','default123','False','comp','False','Lead',10),('sachin19','19@gmail','CSG','surveyy1','default123','False','comp','False','Lead',11),('sachin2','2@gmail','Deco','surveyy1','default123','False','comp','False','Lead',12),('sachin20','20@gmail','CSG','surveyy1','default123','False','comp','False','Lead',13),('sachin21','21@gmail','CSG','surveyy1','default123','False','comp','False','Ex.Manager',14),('sachin22','22@gmail','CSG','surveyy1','default123','False','comp','False','Member',15),('sachin23','23@gmail','Deco','surveyy1','default123','False','comp','False','Member',16),('sachin24','24@gmail','Deco','surveyy1','default123','False','comp','False','Member',17),('sachin25','25@gmail','Trade','surveyy1','default123','False','comp','False','Member',18),('sachin26','26@gmail','Adv','surveyy1','default123','False','comp','False','Member',19),('sachin27','27@gmail','Trade','surveyy1','default123','False','comp','False','Member',20),('sachin28','28@gmail','Deco','surveyy1','default123','False','comp','False','Member',21),('sachin29','29@gmail','CCB','surveyy1','default123','False','comp','False','Member',22),('sachin3','3@gmail','Deco','surveyy1','default123','False','comp','False','Member',23),('sachin4','4@gmail','Deco','surveyy1','default123','False','comp','False','Sr.Manager',24),('sachin5','5@gmail','Deco','surveyy1','default123','False','comp','False','Ex.Manager',25),('sachin6','6@gmail','Deco','surveyy1','default123','False','comp','False','Lead',26),('sachin7','7@gmail','Deco','surveyy1','default123','False','comp','False','Member',27),('sachin8','8@gmail','Deco','surveyy1','default123','False','comp','False','Sr.Manager',28),('sachin9','9@gmail','Deco','surveyy1','default123','False','comp','False','Sr.Manager',29),('tendulkar1','1@gmail','Deco','surveyy56','default123','False','c688p','False','Manager',30),('tendulkar10','10@gmail','Adv','surveyy56','default123','False','c688p','False','Sr.Manager',31),('tendulkar11','11@gmail','Adv','surveyy56','default123','False','c688p','False','Sr.Manager',32),('tendulkar12','12@gmail','Adv','surveyy56','default123','False','c688p','False','Sr.Manager',33),('tendulkar13','13@gmail','Adv','surveyy56','default123','False','c688p','False','Sr.Manager',34),('tendulkar14','14@gmail','Trade','surveyy56','default123','False','c688p','False','Sr.Manager',35),('tendulkar15','15@gmail','Deco','surveyy56','default123','False','c688p','False','Sr.Manager',36),('tendulkar16','16@gmail','CSG','surveyy56','default123','False','c688p','False','Lead',37),('tendulkar17','17@gmail','CCB','surveyy56','default123','False','c688p','False','Lead',38),('tendulkar18','18@gmail','CSG','surveyy56','default123','False','c688p','False','Lead',39),('tendulkar19','19@gmail','CSG','surveyy56','default123','False','c688p','False','Lead',40),('tendulkar2','2@gmail','Deco','surveyy56','default123','False','c688p','False','Lead',41),('tendulkar20','20@gmail','CSG','surveyy56','default123','False','c688p','False','Lead',42),('tendulkar21','21@gmail','CSG','surveyy56','default123','False','c688p','False','Ex.Manager',43),('tendulkar22','22@gmail','CSG','surveyy56','default123','False','c688p','False','Member',44),('tendulkar23','23@gmail','Deco','surveyy56','default123','False','c688p','False','Member',45),('tendulkar24','24@gmail','Deco','surveyy56','default123','False','c688p','False','Member',46),('tendulkar25','25@gmail','Trade','surveyy56','default123','False','c688p','False','Member',47),('tendulkar26','26@gmail','Adv','surveyy56','default123','False','c688p','False','Member',48),('tendulkar27','27@gmail','Trade','surveyy56','default123','False','c688p','False','Member',49),('tendulkar28','28@gmail','Deco','surveyy56','default123','False','c688p','False','Member',50),('tendulkar29','29@gmail','CCB','surveyy56','default123','False','c688p','False','Member',51),('tendulkar3','3@gmail','Deco','surveyy56','default123','False','c688p','False','Member',52),('tendulkar4','4@gmail','Deco','surveyy56','default123','False','c688p','False','Sr.Manager',53),('tendulkar5','5@gmail','Deco','surveyy56','default123','False','c688p','False','Ex.Manager',54),('tendulkar6','6@gmail','Deco','surveyy56','default123','False','c688p','False','Lead',55),('tendulkar7','7@gmail','Deco','surveyy56','default123','False','c688p','False','Member',56),('tendulkar8','8@gmail','Deco','surveyy56','default123','False','c688p','False','Sr.Manager',57),('tendulkar9','9@gmail','Deco','surveyy56','default123','False','c688p','False','Sr.Manager',58);
/*!40000 ALTER TABLE `userdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-26  1:33:11
