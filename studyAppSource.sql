-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: studyApp
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `studyApp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `studyApp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `studyApp`;

--
-- Table structure for table `csv_logs`
--

DROP TABLE IF EXISTS `csv_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `csv_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `courseName` varchar(500) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `weekstoDraw` varchar(500) DEFAULT NULL,
  `drawPrize` varchar(500) DEFAULT NULL,
  `minAns` varchar(500) DEFAULT NULL,
  `minCorrect` varchar(500) DEFAULT NULL,
  `minAverage` varchar(500) DEFAULT NULL,
  `minSets` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `csv_logs`
--

LOCK TABLES `csv_logs` WRITE;
/*!40000 ALTER TABLE `csv_logs` DISABLE KEYS */;
INSERT INTO `csv_logs` VALUES (1,'tester@email.com',NULL,'humber_course',NULL,NULL,NULL,NULL,NULL,NULL),(2,'16string',NULL,'humber_new',NULL,NULL,NULL,NULL,NULL,NULL),(3,'tester@email.com',NULL,'Module1_final[195]',NULL,NULL,NULL,NULL,NULL,NULL),(4,'tester@email.com',NULL,'humber_test',NULL,NULL,NULL,NULL,NULL,NULL),(5,'tester@email.com',NULL,'test_course',NULL,NULL,NULL,NULL,NULL,NULL),(6,'tester@email.com',NULL,'temp_csv',NULL,NULL,NULL,NULL,NULL,NULL),(9,'wong.curtis@hotmail.com','2021-07-13 04:42:57','test_set','1','Shoutout Prize','8','8','75','none'),(16,'wong.curtis@hotmail.com','2021-07-21 06:33:17','humber_demo','3','Mention','15','15','75','3'),(18,'wong.curtis@hotmail.com','2021-07-31 19:09:12','testDataSML','none','none','none','none','none','none');
/*!40000 ALTER TABLE `csv_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `username`
--

DROP TABLE IF EXISTS `username`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `username` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `username`
--

LOCK TABLES `username` WRITE;
/*!40000 ALTER TABLE `username` DISABLE KEYS */;
INSERT INTO `username` VALUES (1,'qatest@email.com','qatester'),(2,'curtiswong06@gmail.com','Curtis GMAIL'),(3,'wong.curtis@hotmail.com','Curtis');
/*!40000 ALTER TABLE `username` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `teacher` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `courseName` varchar(500) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `incorrectCount` int NOT NULL,
  `correctCount` int NOT NULL,
  `answerCount` int NOT NULL,
  `setCount` int NOT NULL,
  `userAverage` int NOT NULL,
  `totalTime` int NOT NULL,
  `eligible` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'email@email.com','null','2021-06-09 05:56:46','humber_123',1,2,3,4,5,6,'false'),(7,'curtiswong06@gmail.com','null',NULL,'test_set',9,20,29,2,69,1,'NULL'),(8,'curtiswong06@gmail.com','null',NULL,'test_set',3,7,10,0,70,13,'NULL'),(9,'curtiswong06@gmail.com','null',NULL,'test_set',1,6,7,0,86,5,'NULL'),(10,'curtiswong06@gmail.com','null',NULL,'test_set',0,21,21,2,100,6,'NULL'),(11,'curtiswong06@gmail.com','null',NULL,'test_set',2,9,11,1,82,25,'NULL'),(14,'curtiswong06@gmail.com','wong.curtis@hotmail.com','2021-07-23 14:09:56','humber_demo',5,23,28,4,82,2,'true'),(20,'curtis@test.com','wong.curtis@hotmail.com','2021-07-25 23:12:22','humber_demo',5,16,21,4,76,15,'true'),(21,'curtis@testmail.com','wong.curtis@hotmail.com','2021-07-25 22:32:54','humber_demo',12,2,14,2,14,12,'false'),(23,'curtiswong06@gmail.com','wong.curtis@hotmail.com','2021-07-31 23:09:12','testDataSML',1,6,7,0,86,25,'false'),(24,'curtiswong06@gmail.com','wong.curtis@hotmail.com','2021-08-01 02:32:06','testDataSML',6,28,34,1,82,1,'false'),(25,'curtiswong06@gmail.com','41d8cd98f00b204e9800998ecf8427e','2021-08-01 23:17:10','humber_demo',0,3,3,0,100,5,'false'),(26,'curtiswong06@gmail.com','wong.curtis@hotmail.com','2021-08-01 01:17:42','test_set',0,20,20,1,100,5,'false');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-02 17:50:52
