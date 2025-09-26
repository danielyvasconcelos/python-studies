# Curso Completo de Python - do Zero ao Avançado (Masterclass)

O curso "Curso Completo de Python - do Zero ao Avançado (Masterclass)" abrange uma vasta gama de tópicos, desde as estruturas mais básicas até recursos avançados.

---

## 1. Introdução e Configuração Inicial

- [x] Apresentação do Python (origem, motivação, características, aplicações).
- [x] Instalação da Linguagem Python.
- [x] Instalação e Configuração do Editor de Código (IDE/Editor de Textos).
- [x] Uso e configuração do **Visual Studio Code (VS Code)**.
- [x] Instalação de extensões do VS Code (Python, VS Code Icons, Code Runner).
- [x] Configuração do ambiente de projeto.
- [x] Alternativas de IDEs/Editores de Código (PyCharm, IDLE, Projeto Jupyter/Jupyter Lab, IDEs Online como Programs, Online GDB, Online Python).
- [x] Uso do Shell Interativo (REPL) e Scripts.

---

## 2. Fundamentos da Linguagem

- [x] Variáveis em Python.
  - [x] Nomenclatura e convenções.
  - [x] Atribuição de valores (incluindo atribuição múltipla).
- [x] Tipos de Dados em Python (Classes).
  - [x] Tipos Primitivos: **Inteiro** (int), **Ponto Flutuante/Real** (float), **String/Caractere** (str), **Lógico/Booleano** (bool).
  - [x] Tipos Adicionais: **Número Complexo** (complex).
  - [x] Verificação de Tipos com as funções `type()` e `is instance()`.
- [x] Função `print()`.
  - [x] Sintaxe e exibição de dados.
  - [x] Uso de argumentos posicionais.
  - [x] Concatenação de strings.
  - [x] Uso do argumento `end` para controle de quebra de linha.
  - [x] Formatação de strings com `format()`.
  - [x] Uso de f-strings (Formatted String Literals).
  - [x] Caracteres de escape (`\n`, `\t`, `\\`).

---
- [x] Captura de entrada do usuário com `input()` e conversão de tipo (Casting: `int()`).

## 3. Operadores
- [x] Operadores Aritméticos.
  - [x] Soma, subtração, multiplicação, divisão real.
  - [x] Divisão inteira, Módulo (resto da divisão), Potenciação.
  - [x] Ordem de Precedência.

- [x] Operadores de Comparação.
  - [x] Igualdade (`==`), Diferença (`!=`), Maior/Menor (`>`, `<`), Maior/Menor ou Igual (`>=`, `<=`).
- [x] Operadores Lógicos (Booleanos).
  - [x] `and` (E), `or` (OU), `not` (NÃO).
  - [x] Tabela Verdade.

## 4.Estruturas de Controle


- [x] Desvios Condicionais.
  - [x] Condicional Simples (`if`).
  - [x] Condicional Composto (`if...else`).
  - [x] Condicional Encadeado (`if...elif...else`).
- [x] Estruturas de Repetição: Laço `while`.
  - [ ] Teste lógico e condição de parada.
  - [ ] Incremento e Decremento.
  - [ ] Laços infinitos e a instrução `break`.
- [ ] Estruturas de Repetição: Laço `for`.
  - [ ] Iteração em sequências (listas, strings).
  - [ ] Geração de sequências com a função `range()` (início, fim, passo).
  - [ ] Instrução `continue`.
  - [ ] Encadeamento de Laços de Repetição (Laços aninhados).

---

## 4. Modularidade, Funções e Exceções

- [ ] Módulos e Pacotes.
  - [ ] Gerenciamento de pacotes com **PIP** (`pip install`, `pip list`, `pip show`, `pip uninstall`, atualização do PIP).
  - [ ] Importação genérica (`import math`).
  - [ ] Importação específica (`from math import sqrt`).
  - [ ] Alias (`as`) na importação.
  - [ ] Criação e importação de módulos próprios.
  - [ ] Ponto de entrada do programa (`if __name__ == "__main__":`).
- [ ] Números Aleatórios.
  - [ ] Uso do Módulo `random`.
  - [ ] Métodos `randint` (inteiros), `random` (float entre 0 e 1), `uniform` (float em faixa).
  - [ ] Arredondamento com `round()`.
  - [ ] Métodos de sequência (`choice`, `sample`, `shuffle`).
- [ ] Funções em Python (Definidas pelo Usuário).
  - [ ] Criação com `def`.
  - [ ] Argumentos/Parâmetros.
  - [ ] Retorno de valores com `return`.
  - [ ] Parâmetros Opcionais e Valores Padrão.
  - [ ] Escopo de Variáveis (Local e Global).
  - [ ] Uso da palavra-chave `global` para alteração de variáveis globais.
- [ ] Funções Especiais.
  - [ ] Funções Lambda (Funções Anônimas).
  - [ ] Programação Funcional: Função `map()`.
  - [ ] Programação Funcional: Função `filter()`.
  - [ ] Programação Funcional: Função `reduce()` (necessita de `functools`).
- [ ] Recursividade.
  - [ ] Conceito e definição (Caso Base e Caso Recursivo).
  - [ ] Exemplo: Cálculo de Fatorial Recursivo.
  - [ ] Erro de Recursão (`RecursionError`).
- [ ] Tratamento de Exceções (Erros).
  - [ ] Uso dos Blocos `try`, `except`, `else` e `finally`.
  - [ ] Exceções Padrão (`ZeroDivisionError`, `ValueError`, `IOError`, `RecursionError`).
  - [ ] Forçando o Lançamento de Exceções com `raise`.
  - [ ] Criação de Exceções Personalizadas (Classes de Exceção).

---

## 5. Sequências e Estruturas de Dados

- [ ] Funções Matemáticas.
  - [ ] Funções Built-in (`max`, `min`, `abs`, `pow`, `sum`, `round`).
  - [ ] Uso do Módulo `math` (Ex: `sqrt`, `ceil`, `floor`, `log`, `factorial`, constantes Pi).
- [ ] Listas.
  - [ ] Criação, acesso por índice (positivo e negativo).
  - [ ] Concatenação, Slicing (fatiamento).
  - [ ] Métodos de manipulação (`append`, `pop`, `insert`, `sort`).
  - [ ] Funções de Agregação (`len`, `sorted`, `sum`, `min`, `max`).
- [ ] Tuplas.
  - [ ] Criação (notação de parênteses).
  - [ ] Característica principal: **Imutabilidade** (operações não disponíveis: `append`, `sort`, `pop`).
  - [ ] Acesso, concatenação e slicing.
  - [ ] Conversão entre Tuplas e Listas.
- [ ] Strings (Sequências de Caracteres).
  - [ ] Imutabilidade e acesso por índice.
  - [ ] Slicing.
  - [ ] Métodos de divisão (`split`).
  - [ ] Métodos de caixa (`upper`, `lower`, `capitalize`, `title`).
  - [ ] Busca (`find`, `in`, `not in`).
  - [ ] Substituição (`replace`).
  - [ ] Remoção de espaços (`lstrip`, `rstrip`, `strip`).
  - [ ] Alinhamento (`rjust`, `center`).
  - [ ] Prefixos/Sufixos (`startswith`, `endswith`).
  - [ ] Doc Strings (Documentação em múltiplas linhas).
- [ ] Dicionários.
  - [ ] Armazenamento em pares **Chave e Valor**.
  - [ ] Acesso, adição, alteração e exclusão de itens.
  - [ ] Métodos `items()`, `keys()`, `values()`.
  - [ ] Desempacotamento de chave e valor em loops `for`.
- [ ] Sets (Conjuntos).
  - [ ] Coleções de valores únicos.
  - [ ] Operações de Conjunto (União com `|` ou `union`, Intersecção com `&` ou `intersection`, Diferença Simétrica).
  - [ ] Métodos de manipulação (`add`, `remove`, `discard`, `pop`, `clear`).
- [ ] Compreensão de Lista (List Comprehension).
  - [ ] Sintaxe concisa (`[expressão for item in lista if condição]`).
  - [ ] Uso de `if` para filtragem.
  - [ ] Uso de múltiplos `for`.

---

## 6. Programação Avançada e Recursos Extras

- [ ] Classes e Objetos (Orientação a Objetos - OO).
  - [ ] Conceitos: Classes, Objetos, Atributos, Métodos.
  - [ ] Definição de Classes (`class`), Argumento `self`.
  - [ ] Método Construtor (`__init__`).
  - [ ] Encapsulamento (Atributos Privados com `__`).
  - [ ] Métodos de Acesso (Setters e Getters).
  - [ ] Herança e Superclasse (`super()`).
  - [ ] Polimorfismo (Substituição de métodos).
- [ ] Gerenciamento de Arquivos e Sistema Operacional.
  - [ ] Módulo `os` (Comandos de Diretório: `getcwd`, `listdir`, `chdir`, `mkdir`, `rmdir`, `rename`).
  - [ ] Módulo `os.path` (`basename`, `dirname`, `join`, `exists`, `isfile`, `isdir`, `splitext`).
  - [ ] Remoção recursiva de diretórios (`shutil.rmtree`).
- [ ] Manipulação de Arquivos de Texto.
  - [ ] Função `open()` e Modos de Acesso (`R`, `W`, `A`).
  - [ ] Leitura de conteúdo (`read`, `readline`, `readlines`).
  - [ ] Escrita de conteúdo (`write`, `writelines`).
  - [ ] Fechamento do manipulador (`close`).
- [ ] Recursos Finais.
  - [ ] Troca simples de valores entre variáveis.
  - [ ] Operador Condicional Ternário (`valor_a if condição else valor_b`).
  - [ ] Generators (Uso de parênteses em vez de colchetes para economia de memória).
  - [ ] Função `enumerate()` (Iteração com índice e item simultaneamente).
  - [ ] Gerenciamento de Contexto com `with` (garantindo o fechamento automático de recursos, ex: `with open(...) as f:`).