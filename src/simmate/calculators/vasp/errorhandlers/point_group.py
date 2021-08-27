# -*- coding: utf-8 -*-

import os

from simmate.workflow_engine.tasks.errorhandler import ErrorHandler
from simmate.calculators.vasp.inputs.incar import Incar


class PointGroup(ErrorHandler):
    """
    ???
    """

    # run this while the VASP calculation is still going
    is_monitor = True

    # we assume that we are checking the vasp.out file
    filename_to_check = "vasp.out"

    # These are the error messages that we are looking for in the file
    possible_error_messages = ["group operation missing"]

    def correct(self, error, dir):

        # load the INCAR file to view the current settings
        incar_filename = os.path.join(dir, "INCAR")
        incar = Incar.from_file(incar_filename)

        # turn off symmetry
        incar["ISYM"] = 0
        correction = "switched ISYM to 0"

        # rewrite the INCAR with new settings
        incar.to_file(incar_filename)

        return correction
