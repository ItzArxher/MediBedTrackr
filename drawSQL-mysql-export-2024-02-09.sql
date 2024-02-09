CREATE TABLE `afdeling`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `naam` VARCHAR(50) NOT NULL,
    `etage` INT NOT NULL
);
CREATE TABLE `bed`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `afdeling_id` INT UNSIGNED NOT NULL,
    `is_beschikbaar` TINYINT(1) NOT NULL
);
ALTER TABLE
    `bed` ADD INDEX `bed_afdeling_id_index`(`afdeling_id`);
CREATE TABLE `patient`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `voornaam` VARCHAR(50) NOT NULL,
    `achternaam` VARCHAR(50) NOT NULL,
    `telefoon_nr` VARCHAR(50) NOT NULL,
    `id_nr` BIGINT UNSIGNED NOT NULL,
    `geboorte_datum` DATE NOT NULL,
    `geslacht` ENUM('') NOT NULL
);
ALTER TABLE
    `patient` ADD UNIQUE `patient_id_nr_unique`(`id_nr`);
CREATE TABLE `opname`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `bed_id` INT UNSIGNED NOT NULL,
    `patient_id` INT UNSIGNED NOT NULL,
    `opname_datumtijd` DATETIME NOT NULL,
    `ontslag_datumtijd` DATETIME NULL,
    `status` ENUM('') NOT NULL
);
ALTER TABLE
    `opname` ADD INDEX `opname_bed_id_index`(`bed_id`);
ALTER TABLE
    `opname` ADD INDEX `opname_patient_id_index`(`patient_id`);
ALTER TABLE
    `opname` ADD CONSTRAINT `opname_id_foreign` FOREIGN KEY(`id`) REFERENCES `bed`(`id`);
ALTER TABLE
    `bed` ADD CONSTRAINT `bed_afdeling_id_foreign` FOREIGN KEY(`afdeling_id`) REFERENCES `afdeling`(`id`);
ALTER TABLE
    `opname` ADD CONSTRAINT `opname_patient_id_foreign` FOREIGN KEY(`patient_id`) REFERENCES `patient`(`id`);