#Alumn - Cadastro de Alunos (Python 3)

Um sistema simples para cadastro e distribuição de notas para alunos de determinada matéria. Faz o uso de SQLite3 para banco de dados e comunicação entre os dados.
Interface gráfica com Tkinter.

##Executar

São apenas passos:

No terminal, execute os arquivos criarbd.py e criartabela.py para criar o banco de dados e a tabela do mesmo

```sh
$ python3 criarbd.py
$ python3 criartabela.py
```

Após isso, basta executar o arquivo:

```sh
$ python3 principal.py
```
ou este para com a UI
```sh
$ python3 principalTkinter.py
```

##Executável

####Para OS X:
Utilize o [py2app](https://pythonhosted.org/py2app/)

####Para Windows:
Utilize o [py2exe](http://www.py2exe.org)
