# Gv3GEWRF 
# Copyright (c) Odycloud.

from Gv3GEWRF.core.util import export
from Gv3GEWRF.core.readers.geogrid_tbl import GeogridTbl, GeogridTblKeys

@export
def write_geogrid_tbl(tbl: GeogridTbl, path: str) -> None:
    sep = 31 * '='
    indent = 8 * ' '

    with open(path, 'w', newline='\n') as f:
        out = lambda s: print(s, file=f)
        out(sep)
        for variable in tbl.variables.values():
            out('name = ' + variable.name)

            for key, val in variable.options.items():
                if GeogridTblKeys.is_derived(key):
                    continue
                out(indent + '{} = {}'.format(key, val))
            
            group_option_keys = set() # type: Set[str]
            for group_options in variable.group_options.values():
                group_option_keys |= group_options.keys()
            for key in group_option_keys:
                if GeogridTblKeys.is_derived(key):
                    continue
                for group_name, group_options in variable.group_options.items():
                    out(indent + '{} = {}:{}'.format(key, group_name, group_options[key]))
            
            out(sep)
