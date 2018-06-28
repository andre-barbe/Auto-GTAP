__author__ = "Andre Barbe"
__project__ = "Auto-GTAP"
__created__ = "2018-3-12"

import shutil


class CopyInputFiles(object):
    """Copies files from the input files directory to the work files directory"""

    __slots__ = ["simulation_name", "input_folder", "work_folder"]

    def __init__(self, simulation_name: str, input_folder: str, work_folder: str) -> None:
        self.simulation_name = simulation_name
        self.input_folder = input_folder
        self.work_folder = work_folder

    def copy(self):
        shutil.copytree('InputFiles\\{0}'.format(self.input_folder),
                        'WorkFiles\\{0}\\{1}'.format(self.simulation_name, self.work_folder))
