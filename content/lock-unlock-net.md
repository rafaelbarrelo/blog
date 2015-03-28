Title: Como identificar LOCK e UNLOCK do Windows em .NET? E o Screen Saver?
Date: 2014-01-15
Category: .Net
Tags: .net, windows, c#, csharp
Slug: lock-unlock-net
Authors: rafaelbarrelo
Summary: Como identificar LOCK e UNLOCK do Windows em .NET? E o Screen Saver?

Para identificar os comandos de LOCK e UNLOCK do Windows em .NET basta implementar o seguinte:

```c#
//Habilita controle do bloqueio de tela
Microsoft.Win32.SystemEvents.SessionSwitch +=
  new Microsoft.Win32.SessionSwitchEventHandler(SystemEvents_SessionSwitch);

//Trata os eventos
void SystemEvents_SessionSwitch(object sender, Microsoft.Win32.SessionSwitchEventArgs e)
{
    if (e.Reason == SessionSwitchReason.SessionLock){
        //Bloqueou estação
    }
    else if (e.Reason == SessionSwitchReason.SessionUnlock){
        //Desbloqueou estação
    }
}
```

Mas… Se entra o ScreenSaver, ele não bloqueia a tela imediatamente. O comando de bloquei só ocorre quando o ScreenSaver fecha. Assim, podemos “saber” se o ScreenSaver está ativado e tomar uma ação:

```c#
using System.Runtime.InteropServices;

const int SPI_GETSCREENSAVERRUNNING = 114;

[DllImport("user32.dll", CharSet = CharSet.Auto)]
private static extern bool SystemParametersInfo(int uAction, int uParam, ref bool lpvParam, int flags);

// Retorna TRUE se estiver executando
public static bool GetScreenSaverRunning()
{
    bool isRunning = false;
    SystemParametersInfo(SPI_GETSCREENSAVERRUNNING, 0, ref isRunning, 0);
    return isRunning;
}
```
Assim, pode-se criar uma thread para monitorar o screensaver. Talvez não seja a solução ideal, mas por enquanto está funcionando.

> Esse post foi publicado originalmente no meu antigo blog em WordPress
