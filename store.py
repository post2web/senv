import cPickle as pickle
import os
import pdb

class PickleStore(object):

    path = '/Users/evo/projects/senv/store_location/'

    def __init__(self, name='defalult'):
        self.filename = self.path + name

    def get(self):
        if not os.path.exists(self.filename):
            return dict()
        else:
            data = pickle.load(open(self.filename, "rb" ))
            assert isinstance(data, dict)
            return data

    def set(self, data):
        assert isinstance(data, dict)
        pickle.dump(data, open(self.filename, "wb"))
