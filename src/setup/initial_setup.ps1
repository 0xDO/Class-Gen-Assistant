# Define the path to the text file containing the list of modules
$moduleListPath = ".\src\settings\python_modules_required.txt"

# Read the file line by line
Get-Content $moduleListPath | ForEach-Object {
    # Check if the module is already installed
    $module = pip show $_

    # If the module is not installed, install it
    if (-not $module) {
        pip install $_
    }
}