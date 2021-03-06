# Copyright 2014-2020 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyscf.solvent import ddcosmo
from pyscf.solvent import ddpcm

def ddCOSMO(method_or_mol, solvent_obj=None, dm=None):
    '''Initialize ddCOSMO model.

    Examples::

    >>> mf = ddCOSMO(scf.RHF(mol))
    >>> mf.kernel()
    >>> sol = ddCOSMO(mol)
    >>> mc = ddCOSMO(CASCI(mf, 6, 6), sol)
    >>> mc.kernel()
    '''
    from pyscf import gto
    from pyscf import scf, mcscf
    from pyscf import tdscf

    if isinstance(method_or_mol, gto.mole.Mole):
        return ddcosmo.DDCOSMO(method_or_mol)

    elif isinstance(method_or_mol, scf.hf.SCF):
        return ddcosmo.ddcosmo_for_scf(method_or_mol, solvent_obj, dm)
    elif isinstance(method_or_mol, mcscf.mc1step.CASSCF):
        return ddcosmo.ddcosmo_for_casscf(method_or_mol, solvent_obj, dm)
    elif isinstance(method_or_mol, mcscf.casci.CASCI):
        return ddcosmo.ddcosmo_for_casci(method_or_mol, solvent_obj, dm)
    elif isinstance(method_or_mol, (tdscf.rhf.TDA, tdscf.rhf.TDHF)):
        return ddcosmo.ddcosmo_for_tdscf(method_or_mol, solvent_obj, dm)
    else:
        return ddcosmo.ddcosmo_for_post_scf(method_or_mol, solvent_obj, dm)
DDCOSMO = ddCOSMO

def ddPCM(method_or_mol, solvent_obj=None, dm=None):
    '''Initialize ddPCM model.

    Examples::

    >>> mf = ddPCM(scf.RHF(mol))
    >>> mf.kernel()
    >>> sol = ddPCM(mol)
    >>> mc = ddPCM(CASCI(mf, 6, 6), sol)
    >>> mc.kernel()
    '''
    from pyscf import gto
    from pyscf import scf, mcscf
    from pyscf import tdscf

    if isinstance(method_or_mol, gto.mole.Mole):
        return ddpcm.DDPCM(method_or_mol)

    elif isinstance(method_or_mol, scf.hf.SCF):
        return ddpcm.ddpcm_for_scf(method_or_mol, solvent_obj, dm)
    elif isinstance(method_or_mol, mcscf.mc1step.CASSCF):
        return ddpcm.ddpcm_for_casscf(method_or_mol, solvent_obj, dm)
    elif isinstance(method_or_mol, mcscf.casci.CASCI):
        return ddpcm.ddpcm_for_casci(method_or_mol, solvent_obj, dm)
    elif isinstance(method_or_mol, (tdscf.rhf.TDA, tdscf.rhf.TDHF)):
        return ddpcm.ddpcm_for_tdscf(method_or_mol, solvent_obj, dm)
    else:
        return ddpcm.ddpcm_for_post_scf(method_or_mol, solvent_obj, dm)
DDPCM = ddPCM
