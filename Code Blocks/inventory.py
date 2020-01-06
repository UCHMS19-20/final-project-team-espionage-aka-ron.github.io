class Inventory:
    """Creating player's inventory for their mission"""

    tools = {
        'binoculars': {
            'quantity': 1,
            'uses': ['zoom_in', 'night_vision', 'thermal_vision']
        },
        'bug' :  {
            'quantity': 3,
            'uses': ['eavesdrop', 'record']
        },
        'camera':  {
            'quantity': 1,
            'uses': ['zoom_in', 'taking_pictures', 'image_filtering', 'image_to_chip']
        },
        'flashdrive':  {
            'quantity': 1,
            'uses': ['storage']
        },
        'phone':  {
            'quantity': 1,
            'uses': ['receive_instructions', 'erase', 'tracking', 'self_destruct']
        }
    }

 