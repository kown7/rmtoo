'''Import Abstract Base Class

'''
import abc


class AbcImports(abc.ABC):
    '''Define an ABC for all imports classes'''


    @abc.abstractmethod
    def __init__(self, self_cfg, import_dest):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError
