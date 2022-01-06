import sqlite3

def calcular_saldo(conta):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT valor FROM conta_pessoa where conta = '"""+conta+"""';
    """)

    valorconta = cursor.fetchone()
    print('VALOR EM CONTA: \n')
    print(valorconta[0])
    return valorconta[0]
