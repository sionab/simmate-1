# -*- coding: utf-8 -*-

import os

from simmate.workflow_engine.tasks.errorhandler import ErrorHandler
from simmate.calculators.vasp.inputs.incar import Incar


class Pssyevx(ErrorHandler):
    """
    This fixes subspace rotation error by switching ALGO to Normal
    """

    # run this while the VASP calculation is still going
    is_monitor = True

    # we assume that we are checking the vasp.out file
    filename_to_check = "vasp.out"

    # These are the error messages that we are looking for in the file
    possible_error_messages = ["ERROR in subspace rotation PSSYEVX"]

    def correct(self, error, dir):

        # load the INCAR file to view the current settings
        incar_filename = os.path.join(dir, "INCAR")
        incar = Incar.from_file(incar_filename)

        # make the fix
        incar["ALGO"] = "Normal"
        correction = "switched ALGO to Normal"

        # rewrite the INCAR with new settings
        incar.to_file(incar_filename)

        return correction
