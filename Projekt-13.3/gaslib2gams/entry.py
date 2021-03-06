###########################################################################
#              This file is part of the program and library               #
#                                                                         #
#                        Electricity Network Lib                          #
#                                                                         #
# Copyright (C) 2015                                                      #
# Friedrich-Alexander-Universitaet Erlangen-Nuremberg                     #
# Discrete Optimization                                                   #
# Contact: Martin Schmidt (mar.schmidt@fau.de)                            #
#          Lars Schewe (lars.schewe@math.uni-erlangen.de)                 #
# All rights reserved.                                                    #
###########################################################################

# Global imports
from collections import namedtuple

# Local imports
from node import Node


class Entry(namedtuple('EntryNamedTuple',
                       Node._fields
                       + ('flow_min', 'flow_max',
                          'gas_temp', 'calorific_value',
                          'norm_density', 'heat_coeff_A',
                          'heat_coeff_B', 'heat_coeff_C',
                          'molar_mass', 'pseudocritical_pressure',
                          'pseudocritical_temperature'))):
    """
    Entry node in a gas transport network.
    Realized by inheritance from a suitable namedtuple.
    """
