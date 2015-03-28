Title: Erro ao fazer deploy no Google App Engine
Date: 2014-01-21
Category: AppEngine
Tags: appengine, eclipse, google, java
Slug: erro-deploy-appengine
Authors: rafaelbarrelo
Summary: Erro ao fazer deploy no Google App Engine

Hoje estava tentando publicar um atualização serviço do aplicativo Mídia Palestrina, mas tive alguns problemas de comunicação com o Google App Engine. Depois de tanto insistir, consegui iniciar o deploy… Porém, chegou em 86% e travou. Fui forçado a parar e recomeçar, tendo que dar um force close no Eclipse.

Quando tentei novamente o deploy, recebi o erro:

> Unable to update app: Error posting to URL:
> https://appengine.google.com/api/appversion/create?app_id=appname&version=1&
> 409 Conflict
> Another transaction by user userid is already in progress for app: s~appname, version: 1.
> That user can undo the transaction with “appcfg rollback”.
> See the deployment console for more details
> Unable to update app: Error posting to URL:
> https://appengine.google.com/api/appversion/create?app_id=appname&version=1&
> 409 Conflict
> Another transaction by user userid is already in progress for app: s~appname, version: 1.
> That user can undo the transaction with “appcfg rollback”.

A mensagem me pareceu bem clara, como forcei o stop, a transação ficou aberta e precisava fecha-la antes de realizar o novo deploy.

Pesquisando um pouco na net, achei o seguinte tutorial que funcionou perfeitamente pra mim:


* Abra o console e entre no diretório BIN do App Engine SDK, no meu caso:
```
/Applications/Eclipse/eclipse/plugins/com.google.appengine.eclipse.sdkbundle_1.8.8/appengine-java-sdk-1.8.8/bin
```
* Rode o comando para torar o appcfg.sh em 'executável':
```sh
$ sudo chmod a+x appcfg.sh
```
* Identifique o diretório war do seu projeto. No meu caso:
````
/Users/rafaelbarrelo/Dev/Eclipse/workspace/MidiaPalestrinaServerV2/war/
```
* Rode o comando de roolback
```sh
$ ./appcfg.sh rollback /Users/rafaelbarrelo/Dev/Eclipse/workspace/MidiaPalestrinaServerV2/war/
```

Ele irá iniciar o processo… Coloque o e-mail e senha!
Fim, processo concluído e deploy “liberado”!
Obs: No meu caso, como uso Google Authenticator, tive que criar uma senha de aplicativo quando o script solicitou a senha do e-mail. Apenas criei a senha e depois de finalizado excluí-la.

*Referência:*
http://stackoverflow.com/questions/11675632/how-do-i-execute-the-command-appcfg-rollback


> Esse post foi publicado originalmente no meu antigo blog em WordPress
