Title: Publicando um Post com ghp-import
Date: 2015-03-27 21:18
Category: Python
Tags: pelican, ghp-import
Slug: publicando-post
Authors: Rafael Barrelo
Summary: publicando um post com ghp-import

Antes de publicar, é preciso ter instalado o **[ghp-import]**.

```sh
$ pip install ghp-import
```

Em seguida, basta executar os comandos:

```sh
//Gera as páginas na pasta output com as configurações de publishconf.py
$ pelican content -o output -s publishconf.py

//Gera o branch gh-pages com o contúdo da pasta output
$ ghp-import output

//Manda para o github
$ git push origin gh-pages
```

Para simplificar, podemos rodar tudo em um único comando:
```sh
$ pelican content -o output -s publishconf.py && ghp-import output && git push origin gh-pages
```

Pronto!
O site estará publicado no GitHub =)


[ghp-import]:https://github.com/davisp/ghp-import
