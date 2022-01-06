import json
import sqlite3
import calc


payload = '{"conta": "0000123-4", "debito": 990.00, "credito": 0.0, "tipo_lancamento": "debito", "descricao": "Transferência para PinBom", "criado_em": "2021-08-02T20:48:23Z", "sistema": "mobile"}'

conta_pinbom = "0000321-4"

payload_converted = json.loads(payload)
payload_converted["conta_destinatario"] = conta_pinbom

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

v = calc.calcular_saldo(payload_converted["conta"])

if (payload_converted["tipo_lancamento"] == 'debito') and (v >= payload_converted['debito']):
    cursor.execute("""
      INSERT INTO lancamento (conta, debito, credito, tipo_lancamento , descricao, criado_em , conta_destinatario)
      VALUES (?,?,?,?,?,?,? ) ;""", (payload_converted["conta"], payload_converted["debito"],
           payload_converted["credito"], payload_converted["tipo_lancamento"],
           payload_converted["descricao"], payload_converted["criado_em"],
           payload_converted["conta_destinatario"])
    )
    cursor.execute("""
          UPDATE conta_pessoa 
            SET valor = ?
            WHERE conta = '"""+payload_converted["conta"]+"""' ;"""
            , (v - payload_converted["debito"],)
    )
calc.calcular_saldo(payload_converted["conta"])
conn.commit()
conn.close()
