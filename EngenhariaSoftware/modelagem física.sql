-- MySQL Workbench Synchronization
-- Generated: 2020-11-06 23:57
-- Model: Pastelaria do Zé
-- Version: 1.2
-- Project: Projeto Integrador - Grupo 06
-- Author: Eliza Muniz de Souza

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `pastelaria_db` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_cliente` (
  `id_cliente` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `telefone` CHAR(11) NOT NULL,
  `compra_fiado` TINYINT(4) NOT NULL,
  `dia_fiado` INT(11) NULL DEFAULT NULL,
  `senha` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_produto` (
  `id_produto` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `descricao` VARCHAR(200) NULL DEFAULT NULL,
  `foto` MEDIUMBLOB NULL DEFAULT NULL,
  `valor_unitario` DECIMAL(11,2) NOT NULL,
  PRIMARY KEY (`id_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_empresa` (
  `taxa_juro_diario` DECIMAL(11,2) NULL DEFAULT NULL,
  `multa_atraso` DECIMAL(11,2) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_comanda` (
  `id_comanda` INT(11) NOT NULL AUTO_INCREMENT,
  `numero_comanda` VARCHAR(100) NOT NULL,
  `data_hora` DATETIME NOT NULL,
  `status_comanda` TINYINT(4) NULL DEFAULT NULL,
  `status_pagamento` TINYINT(4) NULL DEFAULT NULL,
  `funcionario_id` INT(11) NOT NULL,
  `cliente_id` INT(11),
  PRIMARY KEY (`id_comanda`),
  INDEX `funcionario_id_idx` (`funcionario_id` ASC),
  INDEX `cliente_id_idx` (`cliente_id` ASC),
  CONSTRAINT `fk_comanda_funcionario`
    FOREIGN KEY (`funcionario_id`)
    REFERENCES `pastelaria_db`.`tb_funcionario` (`id_funcionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comanda_cliente`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `pastelaria_db`.`tb_cliente` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_funcionario` (
  `id_funcionario` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `matricula` CHAR(10) NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `telefone` CHAR(11) NOT NULL,
  `grupo` TINYINT(4) NOT NULL,
  `senha` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id_funcionario`),
  UNIQUE INDEX `matricula_UNIQUE` (`matricula` ASC),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_recebimento` (
  `id_recebimento` INT(11) NOT NULL AUTO_INCREMENT,
  `data_hora` DATETIME NOT NULL,
  `tipo` TINYINT(4) NOT NULL,
  `valor_acrescimo` DECIMAL(11,2) NULL DEFAULT NULL,
  `valor_desconto` DECIMAL(11,2) NULL DEFAULT NULL,
  `valor_total` DECIMAL(11,2) NOT NULL,
  `funcionario_id` INT(11) NOT NULL,
  PRIMARY KEY (`id_recebimento`),
  INDEX `fk_recebimento_funcionario_idx` (`funcionario_id` ASC),
  CONSTRAINT `fk_recebimento_funcionario`
    FOREIGN KEY (`funcionario_id`)
    REFERENCES `pastelaria_db`.`tb_funcionario` (`id_funcionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_comanda_recebimento` (
  `recebimento_id` INT(11) NOT NULL,
  `comanda_id` INT(11) NOT NULL,
  INDEX `fk_comanda_recebimento_comanda_idx` (`comanda_id` ASC),
  INDEX `fk_comanda_recebimento_recebimento_idx` (`recebimento_id` ASC),
  CONSTRAINT `fk_comanda_recebimento_comanda`
    FOREIGN KEY (`comanda_id`)
    REFERENCES `pastelaria_db`.`tb_comanda` (`id_comanda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comanda_recebimento_recebimento`
    FOREIGN KEY (`recebimento_id`)
    REFERENCES `pastelaria_db`.`tb_recebimento` (`id_recebimento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `pastelaria_db`.`tb_comanda_produto` (
  `id_comanda_produto` INT(11) NOT NULL AUTO_INCREMENT,
  `quantidade` INT(11) NOT NULL,
  `valor_unitario` DECIMAL(11,2) NOT NULL,
  `comanda_id` INT(11) NOT NULL,
  `produto_id` INT(11) NOT NULL,
  `funcionario_id` INT(11) NOT NULL,
  PRIMARY KEY (`id_comanda_produto`),
  INDEX `fk_comanda_produto_comanda_idx` (`comanda_id` ASC),
  INDEX `fk_comanda_produto_produto_idx` (`produto_id` ASC),
  INDEX `fk_comanda_produto_funcionario_idx` (`funcionario_id` ASC),
  CONSTRAINT `fk_comanda_produto_comanda`
    FOREIGN KEY (`comanda_id`)
    REFERENCES `pastelaria_db`.`tb_comanda` (`id_comanda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comanda_produto_produto`
    FOREIGN KEY (`produto_id`)
    REFERENCES `pastelaria_db`.`tb_produto` (`id_produto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comanda_produto_funcionario`
    FOREIGN KEY (`funcionario_id`)
    REFERENCES `pastelaria_db`.`tb_funcionario` (`id_funcionario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
