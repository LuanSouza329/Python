# Python: aulas e projetos

Repositório de estudos e exercícios desenvolvidos durante as aulas de Python, com exemplos de lógica de programação, estruturas de dados, funções, manipulação de arquivos, JSON, CSV e análise de dados com Pandas.

## Conteúdo

- `aula01` a `aula10`: fundamentos de Python, condicionais, laços, funções e estruturas de dados.
- `ml001`: primeiro exercício relacionado a Machine Learning.
- `pandas01` a `pandas20`: leitura, limpeza, transformação e análise de dados com Pandas.
- `projetos/projeto01`: análise comercial de vendas e rentabilidade.

## Projeto em destaque

### Análise Comercial

O projeto analisa o desempenho comercial de uma empresa a partir de dados de vendas. A análise busca responder perguntas como:

- Qual foi o faturamento total?
- Qual foi o lucro total?
- Qual vendedor apresentou o melhor desempenho?
- Quais produtos geraram maior faturamento e lucro?
- Quais produtos apresentaram maior margem de lucro?

Tecnologias utilizadas:

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

Acesse os arquivos do projeto:

- [Relatório em HTML](projetos/projeto01/index.html)
- [Notebook](projetos/projeto01/projeto_01_analise_comercial.ipynb)
- [Dados das vendas](projetos/projeto01/dados.csv)

## Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/LuanSouza329/python.git
   cd python
   ```

2. Crie e ative um ambiente virtual, se desejar:

   ```bash
   python -m venv .venv
   ```

   No Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as bibliotecas usadas nos exercícios de análise:

   ```bash
   pip install pandas matplotlib jupyter
   ```

4. Abra o notebook:

   ```bash
   jupyter notebook projetos/projeto01/projeto_01_analise_comercial.ipynb
   ```

Os exercícios das aulas podem ser executados individualmente com Python, por exemplo:

```bash
python aula01/aula01.py
```

## Observações

O relatório HTML é uma versão estática exportada do notebook. Ele apresenta os códigos, tabelas, gráficos e conclusões já gerados, sem necessidade de executar Python no navegador.

## Autor

**Luan Souza**

- GitHub: [LuanSouza329](https://github.com/LuanSouza329)
