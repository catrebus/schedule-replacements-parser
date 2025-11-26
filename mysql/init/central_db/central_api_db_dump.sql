-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: central_api_database
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `college_group`
--

DROP TABLE IF EXISTS `college_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college_group` (
  `id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college_group`
--

LOCK TABLES `college_group` WRITE;
/*!40000 ALTER TABLE `college_group` DISABLE KEYS */;
INSERT INTO `college_group` VALUES ('301-ИС-23');
/*!40000 ALTER TABLE `college_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pdf_download_url`
--

DROP TABLE IF EXISTS `pdf_download_url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pdf_download_url` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pdf_download_url`
--

LOCK TABLES `pdf_download_url` WRITE;
/*!40000 ALTER TABLE `pdf_download_url` DISABLE KEYS */;
/*!40000 ALTER TABLE `pdf_download_url` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `replacement`
--

DROP TABLE IF EXISTS `replacement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `replacement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `group` varchar(10) NOT NULL,
  `teacher_before` varchar(45) DEFAULT NULL,
  `pair_number_before` int DEFAULT NULL,
  `discipline_before` varchar(255) DEFAULT NULL,
  `class_before` varchar(45) DEFAULT NULL,
  `teacher_now` varchar(45) DEFAULT NULL,
  `pair_number_now` int DEFAULT NULL,
  `discipline_now` varchar(255) DEFAULT NULL,
  `class_now` varchar(45) DEFAULT NULL,
  `url_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `url_id_replacement_idx` (`url_id`),
  KEY `group_id_replacement_idx` (`group`),
  CONSTRAINT `group_id_replacement` FOREIGN KEY (`group`) REFERENCES `college_group` (`id`),
  CONSTRAINT `url_id_replacement` FOREIGN KEY (`url_id`) REFERENCES `pdf_download_url` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `replacement`
--

LOCK TABLES `replacement` WRITE;
/*!40000 ALTER TABLE `replacement` DISABLE KEYS */;
/*!40000 ALTER TABLE `replacement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `replacement_type`
--

DROP TABLE IF EXISTS `replacement_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `replacement_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `replacement_id` int NOT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `replacement_id_replacement_type_idx` (`replacement_id`),
  KEY `type_id_replacement_type_idx` (`type`),
  CONSTRAINT `replacement_id_replacement_type` FOREIGN KEY (`replacement_id`) REFERENCES `replacement` (`id`),
  CONSTRAINT `type_id_replacement_type` FOREIGN KEY (`type`) REFERENCES `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `replacement_type`
--

LOCK TABLES `replacement_type` WRITE;
/*!40000 ALTER TABLE `replacement_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `replacement_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES ('добавление занятия'),('замена дисциплины'),('замена кабинета'),('замена преподавателя'),('отмена занятия'),('перенос занятия');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-23 21:33:17
