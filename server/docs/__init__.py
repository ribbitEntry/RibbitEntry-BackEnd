def param(name, description, required=True):
    return {
        'name': name,
        'description': description,
        'in': 'json',
        'type': 'str',
        'required': required
    }