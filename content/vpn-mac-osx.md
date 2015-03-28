Title: Automatizando conexão com VPN no MAC OSX
Date: 2014-06-14
Category: VPN
Tags: automatizar, bash, conexão, dica, mac, osx, vpn
Slug: vpn-mac-osx
Authors: rafaelbarrelo
Summary: Automatizando conexão com VPN no MAC OSX

Primeiro, é preciso configurar a VPN no Mac pelo painel de configurações (não vou entrar nesse detalhe aqui, mas é bem tranquilo…). Para o exemplo, vamos supor que o nome da VPN criada é RBARRELO, já configurada com usuario e senha e sem marcar a opção “Send all traffic over VPN connection”, pois vamos criar uma rota para isso.

Abra seu editor de texto preferido e coloque o seguinte código:

```sh
#!/usr/bin/osascript

tell application "System Events"
    tell current location of network preferences
        set VPNservice to service "RBARRELO"
        if exists VPNservice then
            connect VPNservice
        end if
        repeat until (connected of current configuration of VPNservice)
            delay 1
            "Aguardando conexão com rede RBARRELO..."
        end repeat

        "Estamos conectado =)"
    end tell
end tell
```
Salve o arquivo com o nome **vpn_connect_script**

Em seguida, crie outro arquivo:
```sh
#!/usr/bin/osascript

tell application "System Events"
 tell current location of network preferences
  set VPNservice to service "RBARRELO"
  set isConnected to connected of current configuration of VPNservice
  if isConnected then disconnect VPNservice
 end tell
end tell
```
Salve-o com o nome **vpn_disconnect_script** no mesmo diretório do primerio.

Agora, abra o terminal e execute o comando:
```sh
sudo chmod a+x vpn_connect_script && sudo chmod a+x vpn_disconnect_script
```
Isso irá dar permissão de execução para os scripts.

Pronto, agora se executar *.vpn_connect_script*, você irá se conectar à VPN e *.vpn_disconnect_script* irá te desconectar.

Ok, mas para isso funcionar, você precisaria estar no diretório dos scripts… Vamos melhorar isso?

Pelo terminal, entre na raiz do seu usuário com o comando:

```sh
$ cd ~/
```
Veja se existe o arquivo .profile com o comando:
```sh
$ ls -la
```
Se existir, basta abri-lo com o comando:
```sh
$ open -e .profile
```
Caso não exista, abra seu editor preferido e salve um arquivo com o nome .profile (sim, tem um ponto na frente!) no seu diretório raiz. Ou rode o comando:
```sh
$ touch .profile && open -e .profile
```
Para criar e abrir o arquivo.

Coloque no arquivo o seguinte texto:
```
alias vpn_connect='~/{caminho_do_script}/vpn_connect_script && sudo route add {IP} {Gateway} {Mask} && ping -a -c 5 {IP}'
alias vpn_disconnect='~/{caminho_do_script}/vpn_disconnect_script'
```
Troque *{caminho_do_script}* pelo diretório onde salvou os scripts, *{IP}*, *{Gateway}* e *{Mask}* pelos dados referente a rota que deseja adicionar.

Salve o arquivo e feche o terminal.

Abra o terminal novamente e agora basta digitar **vpn_connect** para conectar e **vpn_disconnect** para desconectar.

Legal, não?!

Agradecimentos especiais ao [Mazola] do blog http://blog.mazolini.com.br/ pela ajuda nas configurações! =)

Abraços

[Mazola]:https://plus.google.com/+EduardoMazolini



> Esse post foi publicado originalmente no meu antigo blog em WordPress
