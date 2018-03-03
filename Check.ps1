$VMName = "VMNAME"
$folder = 'C:\Export'
$SnapshotName = 'Test_Snap'

$VM = @{
    Name = $VMName
    MemoryStartupBytes = 32MB
    Generation = 1
    }


if (Get-VM $VMName){
    Remove-VM -Name $VMName -Force
}
New-VM @VM | Out-Null
Checkpoint-VM -Name $VMName -SnapshotName $SnapshotName
#Remove-VMCheckpoint -VMName $VMName -Name $SnapshotName
$c = Get-VMSnapshot -VMName $VMName | Out-Null
if ($c -eq $SnapshotName){
$a="Prohibition create and delete checkpoints: Disabled"
$a
}
else{
$a="Prohibition create and delete checkpoints: Enabled"
$a
}

if (Test-Path $folder){
Remove-Item $folder -Recurse
}
New-Item -Path $folder -ItemType "directory" | Out-Null
Export-VM -Name $VMName -Path $folder | Out-Null
