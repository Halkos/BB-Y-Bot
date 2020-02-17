class Utils:

    @staticmethod
    def try_convert(value, *types):
        for t in types:
            try:
                return t(value)
            except TypeError:
                return "type"
            except ValueError:
                return "value"
