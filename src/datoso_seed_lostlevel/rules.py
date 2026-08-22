"""Rules for the 'base' seed."""
from datoso_seed_lostlevel.dats import LostLevelDat

rules = [
    {
        'name': 'Lost Level Dat',
        '_class': LostLevelDat,
        'seed': 'lostlevel',
        'priority': 0,
        'rules': [
            {
                'key': 'url',
                'operator': 'contains',
                'value': 'lost-level-archive',
            },
            {
                'key': 'homepage',
                'operator': 'eq',
                'value': 'Lost Level Archive',
            },
        ],
    },
]


def get_rules() -> list:
    """Get the rules."""
    return rules
