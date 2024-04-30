import pytest
import sys
import os

# Set the current working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Define the test modules or directories you want to run
test_targets = [
    "Tests/test_checkbox.py",  # Specific test module
    "Tests/OrangeHRM/",        # Entire directory
]

# Additional pytest options
pytest_options = [
    "-v",                      # Verbose output    
    "--maxfail=3",             # Stop after 3 test failures  
]

# Combine test targets and options
pytest_args = test_targets + pytest_options

# Run pytest with the specified arguments
exit_code = pytest.main(["--trace-config"] + pytest_args)

# Exit the script with the same exit code as pytest
sys.exit(exit_code)
