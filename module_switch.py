class ImportBlocker(object):
    def __init__(self, *args):
        self.module_names = args

    def find_module(self, fullname):
        try:
            import module_name
        except:
            pass  # or anything to log