Set WshShell = CreateObject("WScript.Shell" )
WshShell.Run chr(34) & "server.exe" & Chr(34) & " stop", 0
Set WshShell = Nothing