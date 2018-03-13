__author__ = "Andre Barbe"
__project__ = "GTAP-E-Validation"
__created__ = "2018-3-9"
__altered__ = "2018-3-12"

# Import methods
# Import External Methods
import yaml, os, subprocess

# Import My Methods
from CleanWorkFiles import CleanWorkFiles
from CopyInputFiles import CopyInputFiles
from CreateSTI import CreateSTI

# Import control variables from yaml
with open('config.yaml', 'r') as f:
    config = yaml.load(f)
# Define control variables from yaml
solution_method = config["solution_method"]
gtap_file_name = config["gtap_file_name"]

# Call Methods
# Setup files for running GEMSIM
CleanWorkFiles().create()
CopyInputFiles().create()

# Run Simulation
# Change working directory to Work_Files so all output (and logs) will go there when gemsim or sltoht is called
os.chdir("Work_Files")
# Create GSS and GST files for shocks and model gemsim
CreateSTI(gtap_file_name, "NA", "gtap").create()
subprocess.call("tablo -sti {0}.sti".format(gtap_file_name))
