-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pastelaria_db
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `tb_recebimento`
--

DROP TABLE IF EXISTS `tb_recebimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_recebimento` (
  `id_recebimento` int NOT NULL AUTO_INCREMENT,
  `data_hora` datetime NOT NULL,
  `tipo` tinyint NOT NULL,
  `valor_acrescimo` decimal(11,2) DEFAULT NULL,
  `valor_desconto` decimal(11,2) DEFAULT NULL,
  `valor_total` decimal(11,2) NOT NULL,
  `funcionario_id` int NOT NULL,
  PRIMARY KEY (`id_recebimento`),
  KEY `fk_recebimento_funcionario_idx` (`funcionario_id`),
  CONSTRAINT `fk_recebimento_funcionario` FOREIGN KEY (`funcionario_id`) REFERENCES `tb_funcionario` (`id_funcionario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_recebimento`
--

LOCK TABLES `tb_recebimento` WRITE;
/*!40000 ALTER TABLE `tb_recebimento` DISABLE KEYS */;
INSERT INTO `tb_recebimento` VALUES (1,'2020-11-30 19:44:11',1,0.00,1.00,10.00,3),(2,'2020-11-30 19:50:17',2,0.00,0.00,11.00,3),(3,'2020-11-30 20:00:44',2,0.00,0.00,11.00,3);
/*!40000 ALTER TABLE `tb_recebimento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-30 20:20:46
