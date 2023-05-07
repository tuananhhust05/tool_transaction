CREATE TABLE `ecom`.`transaction` (
  `id` INT NOT NULL,
  `creator_id` INT NOT NULL,
  `amount` INT NOT NULL,
  `fee` INT NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `created_by` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_by` INT NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

CREATE TABLE `ecom`.`plan` (
  `id` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `time_change` DATETIME NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

CREATE TABLE `ecom`.`result` (
  `id` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `time_change` DATETIME NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `time_current` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
