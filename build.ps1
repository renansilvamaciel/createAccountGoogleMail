$exclude = @("venv", "testeCreateAcountGoogle.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "testeCreateAcountGoogle.zip" -Force