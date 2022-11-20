# AV4 - Simulado

Simulado Avaliação 4 - Bits e Proc

Você possui um total de 1h20 para realizar a avaliação, você pode decidir
como usar o seu tempo.

- **NÃO PODE USAR O GITHUB COPILOT**
- **Trabalhar sozinho**
- **1h20 min**
- **REALIZAR UM COMMIT (A CADA QUESTÃO) E DAR PUSH AO FINALIZAR**

## Teóricas

Podem cair questões do tipo a seguir:

1. Linguagem de máquina: 1. https://insper.github.io/bits-e-proc/commum-content/exercicios/Linguagem_de_maquina.pdf
1. Pilha VM: https://docs.google.com/spreadsheets/d/1dywPIHgpUztDtpqzuEuGzAuTlcK9ryVUTp9-b84stJ4/edit?usp=sharing
1. Como funciona o acesso ao LCD ou LED na linguagem VM?

## VM

Resolva as questões vm a seguir

### abs

| Arquivo: `vm/abs/abs.vm` | pts HW | pts SW |
|--------------------------|--------|--------|
| `pytest -k abs_positivo` |        | x      |
| `pytest -k abs_negativo` |        | x      |

Escreva uma função (`abs.vm`) em linguagem VM que retorna o valor absoluto (módulo) de um único valor passado como argumento.

``` python
def abs(val)
```

### factorial

| Arquivo: `vm/fact/fact.vm` | test | pts HW | pts SW |
|----------------------------|------|--------|--------|
| `pytest -k fact_zero`      | `0!` |        | x      |
| `pytest -k fact_one`       | `1!` |        | x      |
| `pytest -k fact_three`     | `3!` |        | x      |
| `pytest -k fact_generic`   | `x!` |        | x      |

Escreva uma função (`fact.vm`) em linguagem VM que retorna o fatorial de um valor passado como argumento.

> Você deve usar a função mult que já foi fornecida.

Lembre que:

``` text
0! = 1
1! = 1
3! = 3*2*1   ... 
4! = 4*3*2*1 ...
```

## Vm translator

Questões relacionadas ao vmtranslator

### `delete`

| Arquivo: `vmtranslator/Code.vm` | pts HW | pts SW |
|---------------------------------|--------|--------|
| `pytest -k delete`              |        | x      |

Esta nova instrução VM deve deletar um valor da pilha, como no exemplo a seguir;

``` text
   
       14                 14
       12          SP-->  12
 SP-->              
          delete
```

A tradução do comando `delete` de `vm` para `nasm` deve ser feito no `Code.py`

``` python
    if   command == "delete":
```

### `swap`

| Arquivo: `vmtranslator/Code.vm` | pts HW | pts SW |
|---------------------------------|--------|--------|
| `pytest -k swap`                |        | x      |

Esta nova instrução VM deve trocar o valor do topo da pilha, como no exemplo a seguir;

``` text
   
       14                 12
       12          SP-->  14
 SP-->              
          swap
```

A tradução do comando `swap` de `vm` para `nasm` deve ser feito no `Code.py`

``` python
    if command == "swap":
```

### `add3`

| Arquivo: `vmtranslator/Code.vm` | pts HW | pts SW |
|---------------------------------|--------|--------|
| `pytest -k add3`                |        | x      |

Esta nova instrução VM deve fazer o valor do topo da pilha, como no exemplo a seguir:

``` text
       14                 27
       12          SP --> 12
       01                 01
 SP-->              
             add3
```

A tradução do comando `add3` de `vm` para `nasm` deve ser feito no `Code.py`

``` python
    elif command == "add3":
```
