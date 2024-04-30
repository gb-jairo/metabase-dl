# metabase-dl

Script python para baixar CSV do Metabase. Usar com moderação.


#### Como usar

Clonar e entrar na pasta. Depois:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

1) Entre na home do metabase, abra o console do navegador e vá na seção network, clique em algum request e procure a opção <kbd>Copy All as HAR</kbd> (essa opção existe no firefox e chrome, com esse mesmo nome)

2) Salve o conteúdo em um arquivo chamado `db.json` na pasta do projeto

3) No script `main.py` digite a consulta e o nome do banco onde vai ser executada. O nome do banco é de acordo como é exibido na UI do Metabase.

4) Execute o script `./main.py`. Será criado um arquivo `output.csv` com o resultado.

Caso aconteça algum erro na execução:
- O token de autenticação provavelmente expirou. Tente renovar o arquivo db.json.
- Verifique a sua consulta por erros de sintaxe.


# TESTADO APENAS COM BANCOS SQL
