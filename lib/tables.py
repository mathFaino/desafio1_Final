import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conta_pessoa (
        conta VARCHAR(9) NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        valor NUMERIC(9,2),
        valor_inicial NUMERIC(9,2)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS lancamento (
        id_lancamento INTEGER NOT NULL PRIMARY KEY,
        conta VARCHAR(9) NOT NULL,
        debito NUMERIC(9,2),
        credito NUMERIC(9,2),
        tipo_lancamento VARCHAR(7) NOT NULL,
        descricao TEXT,
        criado_em TEXT,
        conta_destinatario VARCHAR(9) NOT NULL,
        FOREIGN KEY (conta) REFERENCES conta_pessoa (conta),
        FOREIGN KEY (conta_destinatario) REFERENCES conta_pessoa (conta)
);
""")

print('Tabelas criadas!!!')

conn.close()