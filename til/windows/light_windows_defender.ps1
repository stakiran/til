
# Disables
# ========

Set-MpPreference -DisableBehaviorMonitoring $True
Set-MpPreference -DisableCatchupFullScan $True
Set-MpPreference -DisableCatchupQuickScan $True
# This values are changed by `control schedtasks` "\Microsoft\Windows\Windows Defender *" tasks.
Set-MpPreference -DisableRealtimeMonitoring $True
Set-MpPreference -DisableScanningNetworkFiles $True

# Realtimes
# =========

# 0:every 1:sun... 7:sat 8:never
Set-MpPreference -ScanScheduleDay 7
Set-MpPreference -RemediationScheduleDay 8
Set-MpPreference -ScanScheduleTime "03:33:33"
Set-MpPreference -ScanScheduleQuickScanTime "01:11:11"
Set-MpPreference -ScanOnlyIfIdleEnabled $True
# 1:quick 2:full
Set-MpPreference -ScanParameters 1
# NTFS / 0:both, 1:incoming 2:outgoing
Set-MpPreference -RealTimeScanDirection 2

# Exclusion
# =========

# > such as obj or lib, to exclude from scheduled, custom, and real-time scanning.
Set-MpPreference -ExclusionExtension md,txt,
                                     log,json,
                                     js,py,
                                     lib,obj,
# > You can specify a folder to exclude all the files under the folder.
Set-MpPreference -ExclusionPath "C:\ProgramData\Microsoft\Windows Defender",
                                "C:\Program Files",
                                "C:\Program Files (x86)",
                                "%appdata%",
                                "%localappdata%",
Set-MpPreference -ExclusionProcess "C:\Program Files\Mozilla Firefox\firefox.exe",
                                   "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                                   "D:\bin1\vscode\Code.exe",
                                   "C:\Program Files\Windows Defender\MsMpEng.exe",

# Output current configs
Get-MpPreference > after.txt
$pre = Get-MpPreference
$pre.ExclusionExtension | Out-File -Encoding UTF8 after_exclusion_extension.txt
$pre.ExclusionPath | Out-File -Encoding UTF8 after_exclusion_path.txt
$pre.ExclusionProcess | Out-File -Encoding UTF8 after_exclusion_files_opened_from_process.txt
