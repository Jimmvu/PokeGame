route31 = {

    'S Forest': {
        'east': 'SE Forest',
        'west': 'SW Forest',
    },
    'SW Forest': {
        'north': 'MW Forest',
        'east': 'S Forest'
    },
    'MW Forest': {
        'east': 'M Forest',
        'south': 'SW Forest',
        'item': 'potion'
    },
    'M Forest': {
        'west': 'MW Forest',
        'east': 'ME Forest'
    },

    'SE Forest': {
        'north': 'ME Forest',
        'west': 'S Forest',
        'item': 'pokeball'
    },
    'ME Forest': {
        'west': 'M Forest',
        'south': 'SE Forest',
        'north': 'NE Forest',
    },
    'NE Forest': {
        'west': 'Forest End',
        'south': 'ME Forest'
    }
}
