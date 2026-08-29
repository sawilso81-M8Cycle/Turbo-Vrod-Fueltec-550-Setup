$ErrorActionPreference = 'Stop'

$OutputDir = Join-Path $PSScriptRoot 'vendor'
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$Manuals = @(
    @{
        Name = 'FT450_FT550_FT550LITE_FT600.pdf'
        Url  = 'https://files.fueltech.net/manuals/FT450_FT550_FT550LITE_FT600.pdf'
    },
    @{
        Name = 'Kit_Terminais_FT550.pdf'
        Url  = 'https://files.fueltech.net/manuals/Kit_Terminais_FT550.pdf'
    },
    @{
        Name = 'PROBIKE_Harness.pdf'
        Url  = 'https://files.fueltech.net/manual/Ingles/PROBIKE_Harness.pdf'
    }
)

foreach ($Manual in $Manuals) {
    $Destination = Join-Path $OutputDir $Manual.Name
    Write-Host "Downloading $($Manual.Name)..."
    Invoke-WebRequest -Uri $Manual.Url -OutFile $Destination -UseBasicParsing
    Write-Host "Saved: $Destination"
}

Write-Host ''
Write-Host 'FuelTech manuals downloaded from official FuelTech URLs.'
Write-Host 'Verify the current revision in the FuelTech manuals library before freezing a production wiring revision:'
Write-Host 'https://www.fueltech.net/pages/manuals-fueltech'
