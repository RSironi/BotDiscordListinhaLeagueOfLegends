/* lol_listinha: */
create schema if not exists lollistinha;
use lollistinha;
CREATE TABLE champs (
    nome_champ char(20) PRIMARY KEY,
    img_champ varchar(200)
);

CREATE TABLE listinha (
    fk_champs_nome_champ char(20),
    id_usuario bigint,
    PRIMARY KEY (id_usuario, fk_champs_nome_champ)
);

ALTER TABLE listinha ADD CONSTRAINT FK_listinha_1listinha
    FOREIGN KEY (fk_champs_nome_champ)
    REFERENCES champs (nome_champ)
    ON DELETE CASCADE;
    
-- importar CSV contendo champions via 'Table Data Import Wizard'