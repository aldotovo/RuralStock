# AgroStock — Modelagem do Sistema

## 1. Descrição do Projeto

Sistema web para controle de insumos no meio rural, permitindo registrar entradas e saídas de produtos, acompanhar o consumo e manter um histórico de movimentações.

---

## 2. Objetivo

Fornecer uma ferramenta simples e eficiente para gestão de estoque rural, auxiliando na tomada de decisão e evitando desperdícios.

---

## 3. Funcionalidades (MVP)

* [ ] Cadastro de produtos
* [ ] Cadastro de categorias
* [ ] Registro de entrada de estoque
* [ ] Registro de saída de estoque
* [ ] Controle automático de quantidade
* [ ] Histórico de movimentações
* [ ] Filtro por produto

---

## 4. Entidades do Sistema

###  Produto

Representa um item do estoque (ração, medicamento, insumo).

###  Categoria

Classificação dos produtos (ração, químico, equipamento).

###  Movimentação

Registro de entrada ou saída de produtos.

### Lote 

Representa um grupo de produção (ex: lote de tilápia).

---

## 5. Atributos das Entidades

### Produto

* nome
* unidade (kg, litro, unidade)
* quantidade_atual
* categoria

### Categoria

* nome

### Movimentação

* produto
* tipo (entrada/saída)
* quantidade
* data
* lote (opcional)

### Lote

* nome
* data_inicio
* descricao

---

##  6. Relacionamentos

* Um Produto pertence a uma Categoria
* Uma Movimentação está ligada a um Produto
* Uma Movimentação pode estar ligada a um Lote
* Um Lote pode ter várias Movimentações

---

##  7. Regras de Negócio

* [ ] Entrada adiciona quantidade ao estoque
* [ ] Saída remove quantidade do estoque
* [ ] Não permitir estoque negativo
* [ ] Toda movimentação deve ser registrada
* [ ] Atualização automática da quantidade do produto

---

##  8. Possíveis Expansões Futuras

* [ ] Controle por propriedade rural
* [ ] Multiusuário
* [ ] Dashboard com gráficos
* [ ] Exportação para Excel
* [ ] API REST

---

##  9. Checklist da Modelagem

* [ ] Entidades definidas
* [ ] Atributos definidos
* [ ] Relacionamentos claros
* [ ] Regras de negócio definidas
* [ ] Estrutura simples e escalável

---

##   10. Observações Técnicas

* O sistema será desenvolvido utilizando Python (Django)
* Banco de dados inicial: SQLite
* Possível migração futura para PostgreSQL
