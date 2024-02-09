-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2024 at 01:45 PM
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

-- --------------------------------------------------------

--
-- Table structure for table `afdeling`
--

CREATE TABLE `afdeling` (
  `id` int(10) UNSIGNED NOT NULL,
  `naam` varchar(50) NOT NULL,
  `etage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `afdeling`
--

INSERT INTO `afdeling` (`id`, `naam`, `etage`) VALUES
(1, 'Spoedeisende Hulp', 25),
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
(28, 'Kindergeneeskunde', 19),
(29, 'Neonatologie', 12);

-- --------------------------------------------------------

--
-- Table structure for table `bed`
--

CREATE TABLE `bed` (
  `id` int(10) UNSIGNED NOT NULL,
  `afdeling_id` int(10) UNSIGNED NOT NULL,
  `is_beschikbaar` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bed`
--

INSERT INTO `bed` (`id`, `afdeling_id`, `is_beschikbaar`) VALUES
(1, 5, 1),
(2, 12, 1),
(3, 17, 1),
(4, 8, 1),
(5, 20, 1),
(6, 11, 1),
(7, 3, 1),
(8, 29, 1),
(9, 14, 1),
(10, 18, 1),
(11, 1, 1),
(12, 4, 1),
(13, 25, 1),
(14, 16, 1),
(15, 7, 1),
(16, 21, 1),
(17, 29, 1),
(18, 10, 1),
(19, 2, 1),
(20, 22, 1),
(21, 29, 1),
(22, 23, 1),
(23, 13, 1),
(24, 6, 1),
(25, 26, 1),
(26, 15, 1),
(27, 9, 1),
(28, 27, 1),
(29, 28, 1),
(30, 19, 1);

-- --------------------------------------------------------

--
-- Table structure for table `opname`
--

CREATE TABLE `opname` (
  `id` int(10) UNSIGNED NOT NULL,
  `bed_id` int(10) UNSIGNED NOT NULL,
  `patient_id` int(10) UNSIGNED NOT NULL,
  `opname_datumtijd` datetime NOT NULL DEFAULT current_timestamp(),
  `ontslag_datumtijd` datetime DEFAULT NULL,
  `status` enum('opgenomen','ontslagen','overgebracht') NOT NULL DEFAULT 'opgenomen'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(10) UNSIGNED NOT NULL,
  `voornaam` varchar(50) NOT NULL,
  `achternaam` varchar(50) NOT NULL,
  `telefoon_nr` varchar(50) NOT NULL,
  `id_nr` varchar(50) NOT NULL,
  `geboorte_datum` date NOT NULL,
  `geslacht` enum('man','vrouw','andere') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `voornaam`, `achternaam`, `telefoon_nr`, `id_nr`, `geboorte_datum`, `geslacht`) VALUES
(88, 'John', 'Doe', '+5978776543', 'JK572843', '1990-05-12', 'vrouw'),
(89, 'Jane', 'Smith', '+5978776432', 'TS748903', '1985-09-28', 'man'),
(90, 'Michael', 'Johnson', '+5978990876', 'PM631295', '1982-07-15', 'man'),
(91, 'Emily', 'Brown', '+5978563210', 'EB430982', '1993-12-03', 'man'),
(92, 'William', 'Taylor', '+5978774321', 'WT241780', '1978-04-22', 'man'),
(93, 'Olivia', 'Williams', '+5978770012', 'OW108796', '1980-11-07', 'man'),
(94, 'James', 'Anderson', '+5978774329', 'JA675321', '1975-03-18', 'man'),
(95, 'Emma', 'Jones', '+5978779901', 'EJ159487', '1995-08-30', 'man'),
(96, 'Daniel', 'Martinez', '+5978770890', 'DM895632', '1987-02-25', 'man'),
(97, 'Sophia', 'Garcia', '+5978775643', 'SG728965', '1989-06-09', 'man'),
(98, 'Benjamin', 'Rodriguez', '+5978779780', 'BR367895', '1983-10-14', 'man'),
(99, 'Isabella', 'Lopez', '+5978771234', 'IL482913', '1992-01-20', 'man'),
(100, 'Logan', 'Perez', '+5978774320', 'LP578321', '1986-07-04', 'man'),
(101, 'Mia', 'Gonzalez', '+5978778901', 'MG123456', '1997-04-05', 'man'),
(102, 'Alexander', 'Sanchez', '+5978772345', 'AS896540', '1981-09-17', 'man'),
(103, 'Charlotte', 'Ramirez', '+5978775678', 'CR345218', '1984-11-23', 'man'),
(104, 'Ethan', 'Torres', '+5978778909', 'ET659874', '1994-02-08', 'man'),
(105, 'Amelia', 'Flores', '+5978777890', 'AF456312', '1976-06-16', 'man'),
(106, 'Aiden', 'Rivera', '+5978776789', 'AR213456', '1988-12-10', 'man'),
(107, 'Harper', 'Gomez', '+5978773456', 'HG987231', '1980-03-29', 'man'),
(108, 'Michael', 'Gonzalez', '+5978774567', 'MG541230', '1991-05-31', 'man'),
(109, 'Evelyn', 'Diaz', '+5978777890', 'ED785649', '1982-08-27', 'man'),
(110, 'Jacob', 'Cruz', '+5978776543', 'JC624198', '1983-04-14', 'man'),
(111, 'Abigail', 'Martin', '+5978776789', 'AM293857', '1996-10-02', 'man'),
(112, 'Elijah', 'Hernandez', '+5978777654', 'EH732149', '1979-12-19', 'man'),
(113, 'Elizabeth', 'Nguyen', '+5978774567', 'EN918273', '1998-03-25', 'man'),
(114, 'Sofia', 'Kim', '+5978771234', 'SK498765', '1977-01-11', 'man'),
(115, 'Ella', 'Patel', '+5978778901', 'EP365214', '1985-06-07', 'man'),
(116, 'Matthew', 'Ali', '+5978773456', 'MA519243', '1988-09-03', 'man');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `afdeling`
--
ALTER TABLE `afdeling`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bed`
--
ALTER TABLE `bed`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bed_afdeling_id_index` (`afdeling_id`);

--
-- Indexes for table `opname`
--
ALTER TABLE `opname`
  ADD PRIMARY KEY (`id`),
  ADD KEY `opname_bed_id_index` (`bed_id`),
  ADD KEY `opname_patient_id_index` (`patient_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `patient_id_nr_unique` (`id_nr`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `afdeling`
--
ALTER TABLE `afdeling`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `bed`
--
ALTER TABLE `bed`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `opname`
--
ALTER TABLE `opname`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bed`
--
ALTER TABLE `bed`
  ADD CONSTRAINT `bed_afdeling_id_foreign` FOREIGN KEY (`afdeling_id`) REFERENCES `afdeling` (`id`);

--
-- Constraints for table `opname`
--
ALTER TABLE `opname`
  ADD CONSTRAINT `opname_id_foreign` FOREIGN KEY (`id`) REFERENCES `bed` (`id`),
  ADD CONSTRAINT `opname_patient_id_foreign` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
