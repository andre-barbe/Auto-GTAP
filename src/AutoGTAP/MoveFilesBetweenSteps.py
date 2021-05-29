__author__ = "Andre Barbe"
__project__ = "Auto-GTAP"
__created__ = "2018-4-25"

import shutil


class MoveFilesBetweenSteps(object):
    """Moves files. Typically moves the output of one module to the input of another module"""

    __slots__ = ["source_type", "destination_type", "files", "simulation_name", "source_part_folder",
                 "destination_part_folder"]

    def __init__(self, config, simulation_name: str, part_num: int) -> None:
        prev_part_num = part_num - 1

        self.simulation_name = simulation_name
        self.source_type = config.yaml_file["simulations"][simulation_name]["subparts"][prev_part_num]["type"]
        self.destination_type = config.yaml_file["simulations"][simulation_name]["subparts"][part_num]["type"]
        self.source_part_folder = config.yaml_file["simulations"][simulation_name]["subparts"][prev_part_num][
            "work_folder"]
        self.destination_part_folder = config.yaml_file["simulations"][simulation_name]["subparts"][part_num][
            "work_folder"]

        # Define folders containing source and destination files
        source_part_folder = "WorkFiles\\" + self.simulation_name + "\\" + self.source_part_folder + "\\"
        destination_part_folder = "WorkFiles\\" + self.simulation_name + "\\" + self.destination_part_folder + "\\"

        # Define location of source files
        if self.source_type == "GTPAg2":
            flexagg_output_folder = source_part_folder + "GTAP10p2\\GTAP\\output\\"
            source_flows_file = "{0}basedata.har".format(flexagg_output_folder)
            source_parameters_file = "{0}default.prm".format(flexagg_output_folder)
            source_sets_file = "{0}sets.har".format(flexagg_output_folder)
            source_tax_rates_file = "{0}baserate.har".format(flexagg_output_folder)
            source_view_file = "{0}baseview.har".format(flexagg_output_folder)

        elif self.source_type == "MSplitCom-Exe" or self.source_type == "GTAP-Adjust":
            source_folder = source_part_folder + "output\\"
            source_flows_file = "{0}basedata.har".format(source_folder)
            source_parameters_file = "{0}default.prm".format(source_folder)
            source_sets_file = "{0}sets.har".format(source_folder)
            source_tax_rates_file = "{0}taxrates.har".format(source_folder)
            source_view_file = "{0}gtapview.har".format(source_folder)

        elif self.source_type == "GTAP-V7" or self.source_type == "GTAP-V6":
            source_folder = source_part_folder
            source_flows_file = "{0}gtap.har".format(source_folder)
            source_parameters_file = "{0}default.prm".format(source_folder)
            source_sets_file = "{0}sets.har".format(source_folder)
            source_tax_rates_file = None
            source_view_file = None

        elif self.source_type == "GTPVEW-V6":
            source_folder = source_part_folder
            source_flows_file = "{0}gtap.har".format(source_folder)
            source_parameters_file = "{0}default.prm".format(source_folder)
            source_sets_file = "{0}sets.har".format(source_folder)
            source_tax_rates_file = "{0}newrate.har".format(source_folder)
            source_view_file = "{0}newview.har".format(source_folder)

        elif self.source_type == "Shocks-V6":
            source_folder = source_part_folder
            source_flows_file = "{0}basedata.har".format(source_folder)
            source_parameters_file = "{0}default.prm".format(source_folder)
            source_sets_file = "{0}sets.har".format(source_folder)
            source_tax_rates_file = "{0}baserate.har".format(source_folder)
            source_view_file = "{0}baseview.har".format(source_folder)

        elif self.source_type == "modify_har":
            source_folder = source_part_folder
            source_flows_file = "{0}basedata.har".format(source_folder)
            source_parameters_file = "{0}default.prm".format(source_folder)
            source_sets_file = "{0}sets.har".format(source_folder)
            source_tax_rates_file = "{0}baserate.har".format(source_folder)
            source_view_file = "{0}baseview.har".format(source_folder)

        else:
            raise ValueError('Unexpected source type: %s' % self.source_type)

        # Define location of destination files
        if self.destination_type == "MSplitCom-Exe" or self.destination_type == "GTAP-Adjust":
            destination_folder = destination_part_folder + "input\\"
            destination_flows_file = "{0}basedata.har".format(destination_folder)
            destination_parameters_file = "{0}default.prm".format(destination_folder)
            destination_sets_file = "{0}sets.har".format(destination_folder)
            destination_tax_rates_file = "{0}baserate.har".format(destination_folder)
            destination_view_file = "{0}baseview.har".format(destination_folder)

        elif self.destination_type == "GTAP-V7" or \
                self.destination_type == "GTAP-V6" or \
                self.destination_type == "GTAP-E":
            destination_folder = destination_part_folder
            destination_flows_file = "{0}basedata.har".format(destination_folder)
            destination_parameters_file = "{0}default.prm".format(destination_folder)
            destination_sets_file = "{0}sets.har".format(destination_folder)
            destination_tax_rates_file = "{0}baserate.har".format(destination_folder)
            destination_view_file = "{0}baseview.har".format(destination_folder)

        elif self.destination_type == "GTPVEW-V6":
            destination_folder = destination_part_folder
            destination_flows_file = "{0}gtap.har".format(destination_folder)
            destination_parameters_file = "{0}default.prm".format(destination_folder)
            destination_sets_file = "{0}sets.har".format(destination_folder)
            destination_tax_rates_file = None
            destination_view_file = None

        else:
            raise ValueError('Unexpected destination type: %s' % self.destination_type)

        # Associate pairs of source and destination file locations
        self.files = {
            "flows": [source_flows_file, destination_flows_file],
            "parameters": [source_parameters_file, destination_parameters_file],
            "sets": [source_sets_file, destination_sets_file],
        }

        if source_tax_rates_file and destination_tax_rates_file:
            self.files["tax_rates"] = [source_tax_rates_file, destination_tax_rates_file]
        if source_view_file and destination_view_file:
            self.files["view"] = [source_view_file, destination_view_file]

        # Shock files only need to be created once, and then only updated if tax rates change.
        # So they can be moved around constantly
        # if self.destination_type != "Shocks-V6" and (
        #         self.source_type == "GTAP-V6" or \
        #         self.source_type == "GTAP-V7" or \
        #         self.source_type == "GTPVEW-V6" \
        #         or self.source_type == "Shocks-V6"):
        #     shockfiles = ["to", "tf", "tpi", "tpd", "tgi", "tgd", "tfi", "tfd", "txs", "tms"]
        #     for shockfile in shockfiles:
        #         self.files[shockfile] = [source_folder + shockfile + ".shk", destination_folder + shockfile + ".shk"]

        # Actually copies files
        for key, value in self.files.items():
            shutil.copy(value[0], value[1])
