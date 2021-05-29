from src.AutoGTAP.AggregateModelData import *
from src.AutoGTAP.CleanWorkFiles import *
from src.AutoGTAP.CopyInputFiles import *
from src.AutoGTAP.CreateConfig import *
from src.AutoGTAP.CreateMAP import *
from src.AutoGTAP.CreateOutput import *
from src.AutoGTAP.CreateSTI import *
from src.AutoGTAP.ExportDictionary import *
from src.AutoGTAP.ExportResults import *
from src.AutoGTAP.GTAPAdjustCMF import *
from src.AutoGTAP.GtapModel import *
from src.AutoGTAP.Gtpvew import *
from src.AutoGTAP.ImportCsvSl4 import *
from src.AutoGTAP.ModifyDatabase import *
from src.AutoGTAP.ModifyHAR import *
from src.AutoGTAP.MoveFilesBetweenSteps import *
from src.AutoGTAP.Shocks import *
from src.AutoGTAP.SimulationCMF import *
from src.AutoGTAP.SplitCommodities import *



# Call Methods
# Load config files that will control program
config = CreateConfig("config.yaml")
# Delete working files directory
CleanWorkFiles()
# For each simulation, perform the different subparts (data aggregation, splitting,
# experiment simulation, etc) that make up that simulation
for simulation_name in config.simulation_list:
    # Add one to final range so that python will run the last part too
    for part_num in range(1, config.num_parts(simulation_name) + 1):

        part_type = config.yaml_file["simulations"][simulation_name]["subparts"][part_num]["type"]

        # Copy input files for this part to the appropriate work directory
        CopyInputFiles(config, simulation_name, part_num).copy()

        # Copy Work files from the previous part to the work directory for this part, unless this is the first part
        if part_num != 1:
            MoveFilesBetweenSteps(config, simulation_name, part_num)

        # Run the actual work for this part, depending on which type of part it is
        if part_type == "GTPAg2":
            AggregateModelData(config, simulation_name, part_num)

        elif part_type == "MSplitCom-Exe":
            SplitCommodities(simulation_name)

        elif part_type == "modify_har":
            ModifyHAR(config, simulation_name, part_num)

        elif part_type == "GTPVEW-V6" or part_type == "Shocks-V6":
            Gtpvew(config, simulation_name, part_num)

        elif part_type == "GTAP-Adjust":
            GTAPAdjustCMF(config, simulation_name, part_num)

        elif part_type == "GTAP-V6" or part_type == "GTAP-E":
            GtapModel(config, simulation_name, part_num)

        else:
            raise ValueError('Unexpected part type: %s' % part_type)

ExportResults(config)
