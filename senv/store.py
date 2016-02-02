import cPickle as pickle
import pdb
import shutil
import sys
import os
import errno

class PickleStore(object):

    def __init__(self, parent, name='defalult'):
        self.parent = parent
        user_home = os.path.expanduser("~")
        sep = os.path.sep
        self.data_dir = user_home + sep + '.senv' + sep + 'data' + sep + name + sep
        self.data_filename = self.data_dir + 'data.p'
        self.hash_filename = self.data_dir + 'hash'
        try:
            os.makedirs(self.data_dir)
        except OSError, e:
            if e.errno != errno.EEXIST:
                raise

    def __hash__(self):
        if not os.path.exists(self.hash_filename):
            return hash(str({}))
        f = open(self.hash_filename, 'r')
        hash_key = int(f.read())
        f.close()
        return hash_key

    def read(self):
        if not os.path.exists(self.data_filename):
            return {}
        else:
            data = pickle.load(open(self.data_filename, "rb" ))
            assert isinstance(data, dict)
            return data

    def write(self):
        data = dict(self.parent)
        pickle.dump(data, open(self.data_filename, "wb"))
        f = open(self.hash_filename, 'w')
        hash_key = f.write(str(hash(self.parent)))
        f.close()
