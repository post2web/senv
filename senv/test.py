class Test(dict):

    def __getitem__(self, *args, **kwargs):
        print '__getitem__'
        result = super(Test, self).__getitem__(*args, **kwargs)
        return result

    def __setitem__(self, *args, **kwargs):
        print '__setitem__'
        result = super(Test, self).__setitem__(*args, **kwargs)
        return result

    def __delitem__(self, *args, **kwargs):
        print '__delitem__'
        result = super(Test, self).__delitem__(*args, **kwargs)
        return result

    def __repr__(self, *args, **kwargs):
        print '__repr__'
        result = super(Test, self).__repr__(*args, **kwargs)
        return result

    def __str__(self, *args, **kwargs):
        print '__str__'
        result = super(Test, self).__str__(*args, **kwargs)
        return result
