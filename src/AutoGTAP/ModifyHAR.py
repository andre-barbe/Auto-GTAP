__author__ = "Andre Barbe"
__project__ = "Auto-GTAP"
__created__ = "2018-3-28"

import os
import subprocess


class ModifyHAR(object):
    """Modifies the values of a HAR file"""

    __slots__ = ["config", "simulation_name", "part_num", "input_file", "output_file", "sti_file", "modifications"]

    def __init__(self, config, simulation_name: str, part_num: int) -> None:
        self.config = config
        self.simulation_name = simulation_name
        self.part_num = part_num

        parameter_modification_list = \
            self.config.yaml_file["simulations"][simulation_name]["subparts"][part_num]["parameter_modifications"]

        part_work_folder = self.config.yaml_file["simulations"][self.simulation_name]["subparts"][self.part_num][
            "work_folder"]

        self.input_file = "olddefault"
        self.output_file = "default"
        self.sti_file = "cmd_modify_har.sti"
        self.modifications = parameter_modification_list

        old_work_directory = os.getcwd()
        os.chdir("WorkFiles\\{0}\\{1}".format(simulation_name, part_work_folder))

        self.createsti()

        os.rename("default.prm", "olddefault.har")
        subprocess.call("modhar -sti cmd_modify_har.sti")
        os.chdir(old_work_directory)

    def createsti(self) -> None:
        # Create lines for sti file that controls modhar
        line_list_start = [
            "bat",
            "",
            "y",
            self.input_file + ".har",  # old filename
            self.output_file + ".prm"  # new filename
            #
            # "mw",  # task menu: modify and write
            # "EFNC",  # header to modify
            # "m",  #subcommand: modify the data
            # "s",  # scale entries of array
            # "w",  # whole matrix to be scaled
            # "s",  # multiply by scalar or matrix
            # "0.1",  # value of scalar
            # "w",  # write it to new file
            # "n",  # reuse array again?
            #
        ]
        line_list_modifications = []

        for modification in self.modifications:
            header = modification[0]
            location = modification[1]
            value = modification[2]
            line_list_new_mod = [
                "mw",  # task menu: modify and write
                "{0}".format(header),  # header to modify
                "m",  # subcommand: modify the data
                "r",  # replace entries of array
                "o",  # one entry to be changed
                "{0}".format(location),  # entry to be changed
                "{0}".format(value),  # value of replacement
                "w",  # write it to new file
                "n"  # reuse array again?
            ]

            #
            line_list_modifications = line_list_modifications + line_list_new_mod

        # "mw",  # task menu: modify and write
        # "ESBM",  # header to modify ESBD
        # "m",  # subcommand: modify the data
        # "r",  # replace entries of array
        # "o",  # one entry to be changed
        # "4",  # entry to be changed
        # "0.2",  # value of replacement
        # "w",  # write it to new file
        # "n",  # reuse array again?

        line_list_end = [
            "ex",  # task menu: exit, saving changes
            "a",  # transfer all remaining arrays
            "0"  # do not add history for the new file
        ]

        line_list_total = line_list_start + line_list_modifications + line_list_end

        # Create final file
        with open(self.sti_file, "w+") as writer:  # Create the empty file
            writer.writelines(line + '\n' for line in line_list_total)  # write the line list to the file
