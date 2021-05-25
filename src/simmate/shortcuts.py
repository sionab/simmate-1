# -*- coding: utf-8 -*-

"""
This file exists strictly for when you're testing with Simmate and don't want
to write out long imports every single time. When writing modules, you should
never use these shortcuts because they actually take longer to run. 

So if you're a beginner, use the shortcut. If you're contributing to Simmate
code or really care about speed of your code, avoid the shortcut.

By example, the import below is a shortcut for the longer line below it. They 
both load the same function, but have two key differences: (1) The shortcut is 
obiously easier to remember and write -- so it's best for when you're quickly 
testing things via Spyder; and (2) the shortcut loads slower (typically 1 second)
than the full import. This is because the shortcut module (this file) loads other
convient modules too. So you're actually loading extra things!
        
        # the convenient shortcut
        from simmate.shortcuts import setup
        
        # the faster import that does the same thing
        from simmate.configuration.django import setup_full

"""

# This import sets up Django so we can connect with the Simmate database
from simmate.configuration.django import setup_full as setup

# These are objects that each represent a table in the Simmate database
# from simmate.database.diffusion import Structure as Structure_DB

# These are the most commonly-used workflows for structures
# from simmate.workflows.energy import static
# from simmate.workflows.energy import relaxation

# This is the python object for a Structure
from pymatgen.core.structure import Structure as Structure_PMG
