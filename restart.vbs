Set WshShell = CreateObject("WScript.Shell" )
WshShell.Run chr(34) & "server.exe" & Chr(34) & " restart", 0
Set WshShell = Nothing