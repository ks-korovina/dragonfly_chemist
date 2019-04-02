"""

Molecular function callers.
@author: kkorovin@cs.cmu.edu

A harness for calling functions defined over Molecules.
Makes use of the mols/mol_functions.py

"""

from copy import deepcopy
import numpy as np
from time import sleep

from dragonfly.exd.experiment_caller import CPFunctionCaller
from dragonfly.exd.exd_core import EVAL_ERROR_CODE
from dragonfly.utils.reporters import get_reporter

# Local imports
# replaces the one from exp.cp_domain_utils:
from chemist_opt.domains.domains import load_cp_domain_from_config_file


def _get_cpfc_args_from_config(config):
	""" Return arguments as a dict. """
	if isinstance(config, str):
		from dragonfly.exd.cp_domain_utils import load_config_file
		config = load_config_file(config)
	ret = {'domain': config.domain,
		'domain_orderings':config.domain_orderings,
		'fidel_space':config.fidel_space,
		'fidel_to_opt':config.fidel_to_opt,
		'fidel_space_orderings':config.fidel_space_orderings}
	return ret


class MolFunctionCaller(CPFunctionCaller):
	""" Function Caller for Mol evaluations. """
	def __init__(self, objective, config, train_params, 
				 descr='', debug_mode=False,
				 reporter='silent'):
		""" train_params is a Namespace with .data_dir field """
		constructor_args = _get_cpfc_args_from_config(config)
		super(MolFunctionCaller, self).__init__(objective, descr=descr,
							fidel_cost_func=self._fidel_cost, **constructor_args)
		self.train_params = deepcopy(train_params)  # unclear if this is needed
		self.debug_mode = debug_mode
		self.reporter = get_reporter(reporter)

		# other methods? ----------------------------

		@classmethod
		def is_mf(cls):
			""" Returns True if Multi-fidelity. """
			return False




