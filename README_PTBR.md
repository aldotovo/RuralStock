# RuralStock

Sistema web desenvolvido para gerenciamento de estoque em pequenas propriedades rurais, com foco no controle de insumos, movimentações de estoque e visualização de dados em dashboard.

---

## Sobre o Projeto

O RuralStock foi desenvolvido a partir de experiências reais na área de piscicultura, onde o controle de insumos como ração, sal, vacinas, produtos químicos e estoque de peixes faz parte da rotina operacional.

O projeto foi expandido para atender pequenas propriedades rurais de forma geral, oferecendo uma solução simples e eficiente para gerenciamento de estoque, rastreabilidade de insumos e acompanhamento em tempo real dos recursos disponíveis.

Seu principal objetivo é contribuir para a tecnificação dos processos de gestão no meio rural, auxiliando produtores na tomada de decisão e na redução de perdas operacionais.

---

## Objetivo

Fornecer uma ferramenta acessível para pequenos produtores rurais e pequenas empresas do setor agro realizarem o controle de estoque de forma organizada, registrando entradas e saídas de insumos e visualizando informações por meio de dashboard.

---

## Funcionalidades

- Gerenciamento de categorias de insumos  
- Cadastro de produtos  
- Controle de estoque em tempo real  
- Registro de entradas e saídas (movimentações)  
- Atualização automática do estoque  
- Dashboard com visualização gráfica  
- Interface administrativa para gerenciamento de dados  

---

## Público-Alvo

- Pequenos produtores rurais  
- Piscicultores  
- Pequenas empresas do setor agro  
- Técnicos e gestores de produção  

---

## Diferenciais

- Projeto baseado em experiência prática no setor agro  
- Foco na melhoria dos processos de gestão rural  
- Interface simples e intuitiva  
- Integração entre lógica de negócio e visualização de dados  

---

## Tecnologias Utilizadas

- Python  
- Django  
- SQLite (banco de dados padrão)  
- HTML / CSS  
- Chart.js (visualização de dados)  

---

## Como Executar o Projeto

```bash
# Clonar o repositório
git clone https://github.com/your-username/ruralstock.git

# Entrar na pasta do projeto
cd ruralstock

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Criar usuário administrador
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver