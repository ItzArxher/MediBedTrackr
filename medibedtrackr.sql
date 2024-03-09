-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 09, 2024 at 04:19 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medibedtrackr`
--
CREATE DATABASE IF NOT EXISTS `medibedtrackr` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `medibedtrackr`;

-- --------------------------------------------------------

--
-- Table structure for table `afdeling`
--

CREATE TABLE IF NOT EXISTS `afdeling` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `naam` varchar(50) NOT NULL,
  `etage` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `afdeling`
--

INSERT INTO `afdeling` (`id`, `naam`, `etage`) VALUES
(1, 'Spoedeisende Hulp', 21),
(2, 'Cardiologie', 19),
(3, 'Chirurgie', 19),
(4, 'Pediatrie', 14),
(5, 'Gynaecologie', 11),
(6, 'Neurologie', 12),
(7, 'Oncologie', 1),
(8, 'Orthopedie', 18),
(9, 'Oogheelkunde', 11),
(10, 'KNO (Keel, Neus, Oor)', 3),
(11, 'Interne Geneeskunde', 7),
(12, 'Psychiatrie', 25),
(13, 'Radiologie', 4),
(14, 'Urologie', 21),
(15, 'Dermatologie', 15),
(16, 'Maag-darm-leverziekten', 14),
(17, 'Revalidatiegeneeskunde', 23),
(18, 'Anesthesiologie', 23),
(19, 'Fysiotherapie', 22),
(20, 'Hematologie', 15),
(21, 'Nefrologie', 7),
(22, 'Pijnbestrijding', 15),
(23, 'Endocrinologie', 2),
(24, 'Gerontologie', 17),
(25, 'Oncologische Chirurgie', 1),
(26, 'Plastische Chirurgie', 7),
(27, 'Vrouwenziekten', 3),
(28, 'Kindergeneeskunde', 19);

-- --------------------------------------------------------

--
-- Table structure for table `bed`
--

CREATE TABLE IF NOT EXISTS `bed` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `afdeling_id` int(10) UNSIGNED NOT NULL,
  `is_beschikbaar` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  KEY `bed_afdeling_id_index` (`afdeling_id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bed`
--

INSERT INTO `bed` (`id`, `afdeling_id`, `is_beschikbaar`) VALUES
(1, 19, 0),
(2, 12, 0),
(3, 17, 1),
(4, 8, 1),
(5, 20, 1),
(6, 11, 1),
(7, 3, 1),
(9, 14, 1),
(10, 18, 1),
(11, 1, 1),
(12, 4, 1),
(13, 25, 1),
(14, 16, 1),
(15, 7, 1),
(16, 21, 1),
(18, 10, 1),
(19, 2, 1),
(20, 22, 1),
(22, 23, 1),
(23, 13, 1),
(24, 6, 1),
(25, 26, 1),
(26, 15, 1),
(27, 9, 1),
(28, 27, 1),
(29, 28, 1),
(30, 19, 1),
(35, 12, 1),
(36, 14, 1),
(37, 14, 1),
(38, 14, 1),
(39, 14, 1),
(40, 14, 1),
(41, 1, 1),
(42, 1, 1),
(43, 1, 1),
(44, 27, 1),
(45, 2, 0),
(46, 19, 1),
(47, 19, 1),
(50, 1, 1),
(55, 2, 1),
(60, 3, 1),
(61, 3, 1),
(62, 3, 1),
(63, 3, 1),
(68, 4, 1),
(69, 4, 1),
(70, 4, 1),
(71, 4, 1),
(72, 4, 1),
(73, 5, 1),
(74, 5, 1),
(75, 5, 1),
(76, 5, 1),
(77, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `opname`
--

CREATE TABLE IF NOT EXISTS `opname` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `bed_id` int(10) UNSIGNED NOT NULL,
  `patient_id` int(10) UNSIGNED NOT NULL,
  `opname_datumtijd` datetime NOT NULL DEFAULT current_timestamp(),
  `ontslag_datumtijd` datetime DEFAULT NULL,
  `status` enum('opgenomen','ontslagen','overgebracht') NOT NULL DEFAULT 'opgenomen',
  PRIMARY KEY (`id`),
  KEY `opname_bed_id_index` (`bed_id`),
  KEY `opname_patient_id_index` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `opname`
--

INSERT INTO `opname` (`id`, `bed_id`, `patient_id`, `opname_datumtijd`, `ontslag_datumtijd`, `status`) VALUES
(20, 10, 89, '2024-03-10 11:39:00', '2024-03-30 17:07:00', 'opgenomen'),
(22, 45, 94, '2024-03-08 12:07:00', NULL, 'opgenomen');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE IF NOT EXISTS `patient` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `voornaam` varchar(50) NOT NULL,
  `achternaam` varchar(50) NOT NULL,
  `telefoon_nr` varchar(50) NOT NULL,
  `id_nr` varchar(50) NOT NULL,
  `geboorte_datum` date NOT NULL,
  `geslacht` enum('man','vrouw','andere') NOT NULL,
  `is_opgenomen` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE KEY `patient_id_nr_unique` (`id_nr`)
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `voornaam`, `achternaam`, `telefoon_nr`, `id_nr`, `geboorte_datum`, `geslacht`, `is_opgenomen`) VALUES
(88, 'John', 'Doe', '+5978776541', 'JK572841', '1990-05-15', 'man', 0),
(89, 'Jane', 'Smith', '+5978776432', 'TS748903', '1985-09-28', 'vrouw', 1),
(90, 'Michael', 'Johnson', '+5978990876', 'PM631295', '1982-07-15', 'man', 0),
(91, 'Emily', 'Brown', '+5978563210', 'EB430982', '1993-12-03', 'man', 0),
(92, 'William', 'Taylor', '+5978774321', 'WT241780', '1978-04-22', 'man', 0),
(93, 'Olivia', 'Williams', '+5978770012', 'OW108796', '1980-11-07', 'man', 0),
(94, 'James', 'Anderson', '+5978774329', 'JA675321', '1975-03-18', 'man', 1),
(95, 'Emma', 'Jones', '+5978779901', 'EJ159487', '1995-08-30', 'man', 0),
(96, 'Daniel', 'Martinez', '+5978770890', 'DM895632', '1987-02-25', 'man', 0),
(97, 'Sophia', 'Garcia', '+5978775643', 'SG728965', '1989-06-09', 'man', 0),
(98, 'Benjamin', 'Rodriguez', '+5978779780', 'BR367895', '1983-10-14', 'man', 0),
(99, 'Isabella', 'Lopez', '+5978771234', 'IL482913', '1992-01-20', 'man', 0),
(100, 'Logan', 'Perez', '+5978774320', 'LP578321', '1986-07-04', 'man', 0),
(101, 'Mia', 'Gonzalez', '+5978778901', 'MG123456', '1997-04-05', 'man', 0),
(102, 'Alexander', 'Sanchez', '+5978772345', 'AS896540', '1981-09-17', 'man', 0),
(103, 'Charlotte', 'Ramirez', '+5978775678', 'CR345218', '1984-11-23', 'man', 0),
(104, 'Ethan', 'Torres', '+5978778909', 'ET659874', '1994-02-08', 'man', 0),
(105, 'Amelia', 'Flores', '+5978777890', 'AF456312', '1976-06-16', 'man', 0),
(106, 'Aiden', 'Rivera', '+5978776789', 'AR213456', '1988-12-10', 'man', 0),
(107, 'Harper', 'Gomez', '+5978773456', 'HG987231', '1980-03-29', 'man', 0),
(108, 'Michael', 'Gonzalez', '+5978774567', 'MG541230', '1991-05-31', 'man', 0),
(109, 'Evelyn', 'Diaz', '+5978777890', 'ED785649', '1982-08-27', 'man', 0),
(110, 'Jacob', 'Cruz', '+5978776543', 'JC624198', '1983-04-14', 'man', 0),
(111, 'Abigail', 'Martin', '+5978776789', 'AM293857', '1996-10-02', 'man', 0),
(112, 'Elijah', 'Hernandez', '+5978777654', 'EH732149', '1979-12-19', 'man', 0),
(113, 'Elizabeth', 'Nguyen', '+5978774567', 'EN918273', '1998-03-25', 'man', 0),
(114, 'Sofia', 'Kim', '+5978771234', 'SK498765', '1977-01-11', 'man', 0),
(115, 'Ella', 'Patel', '+5978778901', 'EP365214', '1985-06-07', 'man', 0),
(116, 'Matthew', 'Ali', '+5978773456', 'MA519243', '1988-09-03', 'man', 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bed`
--
ALTER TABLE `bed`
  ADD CONSTRAINT `bed_afdeling_id_foreign` FOREIGN KEY (`afdeling_id`) REFERENCES `afdeling` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `opname`
--
ALTER TABLE `opname`
  ADD CONSTRAINT `opname_ibfk_1` FOREIGN KEY (`bed_id`) REFERENCES `bed` (`id`),
  ADD CONSTRAINT `opname_patient_id_foreign` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
