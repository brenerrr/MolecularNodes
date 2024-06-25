from . import molecule, universe
from .density import MN_OT_Import_Map
from .dna import MN_OT_Import_OxDNA_Trajectory
from .download import download
from .ensemble.cellpack import CellPack
from .ensemble.star import StarFile
from .ensemble.ui import MN_OT_Import_Cell_Pack, MN_OT_Import_Star_File
from .molecule.pdb import PDB
from .molecule.pdbx import BCIF, CIF
from .molecule.sdf import SDF
from .molecule.ui import MN_OT_Import_wwPDB, fetch, load_local
from .universe.universe import MNUniverse

ops_io = (
    [
        MN_OT_Import_Cell_Pack,
        MN_OT_Import_Map,
        MN_OT_Import_OxDNA_Trajectory,
        MN_OT_Import_Star_File,
        MN_OT_Import_wwPDB,
    ]
    + universe.CLASSES
    + molecule.CLASSES
)
