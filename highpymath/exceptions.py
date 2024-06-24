from highpymath import MathBaseError as _mbe

class MathTypeError(_mbe):
    """
    Exception Class for Type Errors from HighPyMath.
    """
    def __init__(self, *args: object):
        """
        Initial the Exception Class with Given Arguments.
        """
        self.args_list = list(args)
        self.args_str = str(args)
        super().__init__(*args)