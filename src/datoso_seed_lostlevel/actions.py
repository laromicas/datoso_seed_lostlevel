"""Actions for the base seed."""
from datoso_seed_lostlevel.dats import LostLevelDat, LostLevelExtraDat

actions = {
    '{dat_origin}/DATs': [
        {
            'action': 'LoadDatFile',
            '_class': LostLevelDat,
        },
        {
            'action': 'DeleteOld',
            'folder': '{dat_destination}',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
    '{dat_origin}/Extra/Lost Level Archive Extras': [
        {
            'action': 'LoadDatFile',
            '_class': LostLevelExtraDat,
        },
        {
            'action': 'DeleteOld',
            'folder': '{dat_destination}',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
}

def get_actions() -> dict:
    """Get the actions dictionary."""
    return actions
