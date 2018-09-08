'''Import Abstract Base Class

'''
import abc


class AbcImports(abc.ABC):
    '''Define an ABC for all imports classes'''

    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError
