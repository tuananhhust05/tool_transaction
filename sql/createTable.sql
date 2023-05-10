CREATE TABLE `defaultdb`.`transaction` (
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

CREATE TABLE `defaultdb`.`plan` (
  `id` INT NOT NULL,
  `created_date` DATETIME NOT NULL,
  `time_change` DATETIME NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

CREATE TABLE `defaultdb`.`result` (
  `id` INT NOT NULL,
  `created_date` DATETIME NOT NULL,
  `time_change` DATETIME NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `time_current` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

SELECT * FROM defaultdb.settlement;CREATE TABLE "settlement" (
  "id" int NOT NULL AUTO_INCREMENT,
  "status" varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  "amount" double NOT NULL,
  "fee_settlement" double NOT NULL,
  "fee_refund" double NOT NULL,
  "received_amount" double NOT NULL,
  "settle_date" datetime(3) NOT NULL,
  "created_date" datetime(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  "creator_id" varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  "stripe_id" varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  "type" varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY ("id")
);
