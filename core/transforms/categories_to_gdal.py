# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from typing import Mapping, Tuple, List
import random

from Gv3GEWRF.core.util import gdal
from Gv3GEWRF.core.constants import UNUSED_CATEGORY_LABEL

def get_gdal_categories(categories: Mapping[int,Tuple[str,str]], category_min: int, category_max: int) -> Tuple[gdal.ColorTable,List[str]]:
    ct = gdal.ColorTable()
    names = [UNUSED_CATEGORY_LABEL] * min(category_min, category_max)
    for i in range(category_min, category_max+1):
        if i in categories:
            name, color_hex = categories[i]
            color = tuple(int(color_hex[i:i+2], 16) for i in (1, 3, 5))
        else:
            name = ''
            # random color for now
            # TODO pick colors such that they are spaced out maximally
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        ct.SetColorEntry(i, color)
        names.append(name)
    return ct, names
  
