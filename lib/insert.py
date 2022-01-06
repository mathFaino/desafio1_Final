import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO conta_pessoa (conta, nome, valor, valor_inicial)
VALUES ('0000123-4', 'Astrogildo Flores', 1090.00, 1090.00)
""")

cursor.execute("""
INSERT INTO conta_pessoa (conta, nome, valor, valor_inicial)
VALUES ('0000321-4', 'PinBom', 0.00, 0.00)
""")

conn.commit()

print('Dados registrados!')

conn.close()