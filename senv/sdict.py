import pdb
from store import PickleStore

class Sdict(dict):

    def __init__(self, name='default', empty=False):
        self.store = PickleStore(parent=self, name=name)
        if empty:
            super(Sdict, self).__init__()
            self.store.write()
        else:
            super(Sdict, self).__init__(self.store.read())

    def read_if_changed(self):
        if hash(self) != hash(self.store):
            self.clear()
            self.update(self.store.read())

    def __getitem__(self, *args, **kwargs):
        self.read_if_changed()
        result = super(Sdict, self).__getitem__(*args, **kwargs)
        return result

    def __setitem__(self, *args, **kwargs):
        self.read_if_changed()
        result = super(Sdict, self).__setitem__(*args, **kwargs)
        self.store.write()
        return result

    def __delitem__(self, *args, **kwargs):
        self.read_if_changed()
        result = super(Sdict, self).__delitem__(*args, **kwargs)
        self.store.write()
        return result

    def __hash__(self, *args, **kwargs):
        return hash(str(dict(self)))

    def __repr__(self, *args, **kwargs):
        self.read_if_changed()
        result = super(Sdict, self).__repr__(*args, **kwargs)
        return result

    def __str__(self, *args, **kwargs):
        self.read_if_changed()
        result = super(Sdict, self).__str__(*args, **kwargs)
        return result
