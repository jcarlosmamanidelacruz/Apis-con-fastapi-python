CREATE DATABASE person;
USE person;

CREATE TABLE IF NOT EXISTS `person`.`tbperson` (
    co_person INT NOT NULL AUTO_INCREMENT,
    fe_regist TIMESTAMP(0) NOT NULL DEFAULT NOW(),
    co_docide VARCHAR(10) NOT NULL,
    no_apepat VARCHAR(200) NOT NULL,
    no_apemat VARCHAR(200) NOT NULL,
    no_nombre VARCHAR(200) NOT NULL,
    ti_genero VARCHAR(1) NOT NULL,
    fe_nacimi date,
    no_corper VARCHAR(200) NOT NULL,
    PRIMARY KEY (`co_person`)
);
  
INSERT INTO `person`.`tbperson` (co_docide, no_apepat, no_apemat, no_nombre, ti_genero, fe_nacimi, no_corper)
		SELECT '44477258', 'Mamani', 'de la Cruz', 'Juan Carlos', 'M', '1987-03-30', 'jmamanidelacruz_microsoft@gmail.com'
UNION SELECT '7985451', 'Rolando', 'Gutierrez', 'Miguel Roberto', 'M', '1997-10-25', 'mrolandomiguel_microsoft@gmail.com';

SELECT * FROM `person`.`tbperson`;