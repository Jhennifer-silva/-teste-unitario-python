## Uso de IA para geração de cenários de teste

### Função escolhida

`dividir(a, b)`

---

### Prompt utilizado

```text
Atue como um professor de Teste de Software.
Tenho a seguinte função Python:

def dividir(a, b):
    return a / b

Quero criar testes unitários usando unittest.

Liste cenários de teste para essa função, incluindo:
- divisão exata;
- divisão com resultado decimal;
- divisão de número negativo;
- divisão de zero por outro número;
- divisão por zero.

Para cada cenário, informe:
- nome do cenário;
- entrada;
- resultado esperado;
- tipo do cenário.

Não gere código ainda.


```
---

### 24. CHECKLIST FINAL

- [x] função definida  
- [x] prompt da IA  
- [x] cenários em tabela  
- [x] análise dos cenários  
- [x] testes com subTest  
- [x] exceção tratada  
- [x] execução documentada  
- [x] README completo  