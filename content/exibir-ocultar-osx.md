Title: Exibir/ocultar arquivos ocultos no Mac (OSX)
Date: 2014-02-09
Category: Mac
Tags: finder, mac, dica, osx
Slug: exibir-ocultar-osx
Authors: rafaelbarrelo
Summary: Exibir/ocultar arquivos ocultos no Mac (OSX)

No terminal use os seguintes comandos:

* Exibir:
```sh
$ defaults write com.apple.finder AppleShowAllFiles -bool true
$ KillAll Finder
 ```
* Ocultar:
```sh
$ defaults write com.apple.finder AppleShowAllFiles -bool false
$ KillAll Finder
```
Simples!

> Esse post foi publicado originalmente no meu antigo blog em WordPress
