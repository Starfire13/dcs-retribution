from .SWPack import *
from .a4ec import *
from .a7e import *
from .a6a import *
from .bandit_clouds import *
from .ea6b import *
from .f9f import *
from .f100 import *
from .f104 import *
from .f105 import *
from .f106 import *
from .f15d import *
from .f15i_idf import *
from .f16i_idf import *
from .f22a import *
from .f4 import *
from .f84g import *
from .fa18efg import *
from .fa18ef_tanker import *
from .frenchpack import *
from .hercules import *
from .highdigitsams import *
from .irondome import *
from .jas39 import *
from .oh6 import *
from .oh6_vietnamassetpack import *
from .ov10a import *
from .spanishnavypack import *
from .super_etendard import *
from .sk60 import *
from .su15 import *
from .su30 import *
from .su57 import *
from .swedishmilitaryassetspack import *
from .coldwarassets import *
from .uh60l import *
from .vietnamwarvessels import *
from .chinesemilitaryassetspack import *
from .russianmilitaryassetspack import *
from .usamilitaryassetspack import *


def load_mods() -> None:
    """Loads all mods.

    Note that this function doesn't *do* anything. Its purpose is to prevent editors
    from removing `import pydcs_extensions` when it is "unused", because mod imports
    have side effects (unit types are registered with pydcs).
    """
