# Atividade 4 — Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats  
**Modalidade:** Individual  
**Responsável:** Rafaela Martins

## 1. Objetivo

Implementar uma regra de negócio em Python, desenvolver testes unitários com pytest seguindo a abordagem TDD e automatizar fluxos da interface do LocalEats com Playwright.

## 2. Parte 1 — Testes unitários e TDD

### Regra escolhida: verificar valor mínimo do pedido

Foi implementada a função `pedido_atingiu_valor_minimo(valor_pedido)`, localizada em `src/regras_localeats.py`.

Regras:
- Pedidos de R$ 30,00 ou mais retornam `True`.
- Pedidos abaixo de R$ 30,00 retornam `False`.
- Valores negativos geram `ValueError`.

### Testes unitários

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Rafaela Martins | Unitário | Pedido exatamente no valor mínimo retorna `True` | `tests/test_regras_localeats.py::test_pedido_com_valor_igual_ao_minimo_retorna_true` |
| TU02 | Rafaela Martins | Unitário | Pedido abaixo do mínimo retorna `False` | `tests/test_regras_localeats.py::test_pedido_abaixo_do_minimo_retorna_false` |
| TU03 | Rafaela Martins | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_com_valor_negativo_gera_value_error` |

### Registro do TDD de Rafaela Martins

**Regra escolhida:** verificar se o pedido atingiu o valor mínimo de R$ 30,00.

**Primeiro teste escrito:** teste para verificar se um pedido de exatamente R$ 30,00 retorna `True`.

**Por que o teste falhou inicialmente:** antes da implementação, a função ainda não existia no módulo, portanto o teste não conseguia importar a função. Após criar a implementação mínima, o teste passou ao comparar o valor do pedido com R$ 30,00.

**Implementação mínima realizada:** foi criada a função que retorna o resultado da comparação `valor_pedido >= 30`.

**Segundo teste escrito:** teste para verificar se um pedido de R$ 29,99 retorna `False`.

**Melhoria ou refatoração realizada:** foi adicionada a validação de valores negativos, lançando `ValueError`. Também foi criado um teste específico para essa situação, utilizando `pytest.raises`.

> O registro descreve a sequência de desenvolvimento. Para comprovar os ciclos Red/Green no ambiente local, é necessário executar o teste antes e depois da implementação.

## 3. Parte 2 — Testes funcionais com Playwright

### Exploração da interface

A partir da tela apresentada e do código-fonte de `login.html` disponibilizado no GitHub do projeto, foram identificados os seguintes elementos:

| Elemento | Seletor |
|---|---|
| Botão Entrar (alternância) | `#showLoginBtn` |
| Botão Criar Conta | `#showRegisterBtn` |
| Formulário de login | `#loginForm` |
| Campo de e-mail do login | `#loginEmail` |
| Campo de senha do login | `#loginPassword` |
| Formulário de cadastro | `#registerForm` |
| Campo nome | `#regName` |
| Campo e-mail do cadastro | `#regEmail` |
| Campo senha do cadastro | `#regPassword` |

### TF01 — Exibição e preenchimento da tela de login

O teste acessa `https://local-eats-unisenac.vercel.app/static/login.html`, verifica se o formulário de login está visível e preenche os campos de e-mail e senha com dados fictícios.

**Assertions principais:**
- O formulário e os campos estão visíveis.
- O campo de e-mail contém o endereço preenchido.
- O campo de senha contém o valor preenchido.

**Arquivo:** `tests/test_localeats.py`  
**Função:** `test_login_exibe_campos_e_permite_preencher_credenciais`  
**Responsável:** Rafaela Martins

### TF02 — Alternância entre login e cadastro

O teste clica no botão `Criar Conta` e verifica se o formulário de cadastro aparece e se o formulário de login fica oculto. Em seguida, clica em `Entrar` e verifica se a tela retorna ao formulário de login.

**Assertions principais:**
- O formulário de cadastro fica visível.
- O formulário de login fica oculto.
- Os campos de nome, e-mail e senha do cadastro ficam visíveis.
- Ao retornar, o formulário de login fica visível e o cadastro fica oculto.

**Arquivo:** `tests/test_localeats.py`  
**Função:** `test_alternar_entre_login_e_cadastro`  
**Responsável:** Rafaela Martins

Os testes funcionais não enviam credenciais ao serviço de autenticação nem criam contas reais. Eles verificam comportamentos observáveis da interface.

## 4. Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Rafaela Martins | Unitário | Pedido exatamente no valor mínimo | `tests/test_regras_localeats.py::test_pedido_com_valor_igual_ao_minimo_retorna_true` |
| TU02 | Rafaela Martins | Unitário | Pedido abaixo do mínimo | `tests/test_regras_localeats.py::test_pedido_abaixo_do_minimo_retorna_false` |
| TU03 | Rafaela Martins | Unitário | Valor negativo gera exceção | `tests/test_regras_localeats.py::test_pedido_com_valor_negativo_gera_value_error` |
| TF01 | Rafaela Martins | Funcional | Exibição e preenchimento do login | `tests/test_localeats.py::test_login_exibe_campos_e_permite_preencher_credenciais` |
| TF02 | Rafaela Martins | Funcional | Alternância entre login e cadastro | `tests/test_localeats.py::test_alternar_entre_login_e_cadastro` |

## 5. Instalação e execução

No PowerShell, dentro da pasta `atividade-04`, executar:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```

Para gerar o relatório solicitado:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

O relatório deve ser gerado após a execução local, para refletir os resultados reais. Se algum teste for ignorado ou falhar, verificar a causa antes da entrega.

## 6. Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como a ferramenta foi utilizada:** apoio na interpretação do enunciado, organização dos arquivos, elaboração da função Python, criação dos testes unitários com pytest, estruturação dos testes funcionais com Playwright e documentação em Markdown.

**Uma sugestão que precisou ser alterada ou rejeitada:** inicialmente foi sugerido automatizar a pesquisa de restaurantes. Após explorar a aplicação e consultar o código de `login.html`, foi identificado que a tela de autenticação oferecia fluxos mais adequados e verificáveis. Por isso, os testes funcionais foram direcionados ao login e à alternância para cadastro.

**Como o código sugerido foi verificado:** os testes unitários foram executados com pytest. Os locators dos testes funcionais foram conferidos com os IDs existentes no HTML fornecido. A execução funcional deve ser confirmada localmente com Chromium instalado.

## 7. Estrutura dos arquivos

```text
atividade-04/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
└── tests/
    ├── __init__.py
    ├── test_regras_localeats.py
    └── test_localeats.py
```
