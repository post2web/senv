from store import PickleStore

class SENV(object):

    store = PickleStore('default')

    @staticmethod
    def set(key, value):
        data = SENV.store.get()
        data[key] = value
        SENV.store.set(data)

    @staticmethod
    def get(key):
        data = SENV.store.get()
        return data[key]

    @staticmethod
    def data():
        return SENV.store.get()
