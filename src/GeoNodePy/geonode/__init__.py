__version__= (1, 2, 0, 'alpha', '+uwi')

def get_version():
    import geonode.utils
    return geonode.utils.get_version(__version__)
