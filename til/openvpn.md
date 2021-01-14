# OpenVPN

## installation
- デフォ
    - `C:\Program Files\OpenVPN`
    - `"C:\Program Files\OpenVPN\bin\openvpn-gui.exe"`
- Uninstall key
    - `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
    - UninstallString
        - `MsiExec.exe /X{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}`
        - `{}` の中身は masked
        - /X は正しい
