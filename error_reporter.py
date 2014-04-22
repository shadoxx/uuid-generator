"""
# DESIGN GOAL - to create a robust and modular error handling(reporting?) class
#
#---FEATURE PROPOSALS-----------------------------------------------------------
#   + define a standardized set of error codes and a structure to store them
#   + ability to choose error reporting method, or choose multiple (stdout, stderr, file, etc)
#   + gracefully handle exceptions
#   + keep track of last 'x' amount of error codes
#   + log name of function that called our error reporter
#   + take in an arbitrary list of STATUS_CODEs at instantiation
#-------------------------------------------------------------------------------
#
    Things to keep in mind:
        - how is this function going to be used? what would be a sane return value?
        - how can we make this code as reuseable as possible?
#
    Dependency explanation:
        - we require 'inspect' to figure out who called the error handler
"""

################################################################################
import inspect

class ErrorReporter:
    """ Error handling and reporting made easy. """

    # hex based status codes
    STATUS_CODE_LIST = {
        'STATUS_EVERYTHING_OK' : (00, "OK"),
        'STATUS_GENERAL_ERROR' : (01, "Unspecified General Error"),
        'ERROR_BAD_USER_INPUT' : (90, "Bad User Input"),
        'ERROR_GENERAL_IO_ERR' : (20, "General I/O Error")
    }

    # format string definitions for outputting pretty code
    STATUS_FORMAT_INFO = "[{3}] {0}: {2}".format
    STATUS_FORMAT_CODES = "name: {1}\tcode: {0:0>2d}\tdescription: {2}".format

    def return_formatted_status(cls, status_code, description):
        """ return a human readable status description, numerical code, and calling function """
        my_calling_function = str(inspect.stack()[1][3])
        return cls.STATUS_FORMAT_INFO(status_code, cls.STATUS_CODE_LIST[status_code][1], str(description), my_calling_function)

    def print_status_code_list(cls):
        """ print out an unsorted list of all status codes this class is capable of handling with descriptions """
        for codes in cls.STATUS_CODE_LIST:
            print cls.STATUS_FORMAT_CODES(cls.STATUS_CODE_LIST[codes][0], codes, cls.STATUS_CODE_LIST[codes][1])

    def get_numerical_error_code(cls, status_code):
        """ return the numerical error code that corresponds to the given STATUS_CODE """
        return cls.STATUS_CODE_LIST[status_code][0]

################################################################################

def caller_method():
    test_instance.print_status_code_list()
    return 0

if __name__ == "__main__":
    test_instance = ErrorReporter()
    print "#"*80 + "\n    ErrorReporter STATUS_CODE List - Use 'name' when calling class functions\n" + "#"*80 + "\n"
    if caller_method() == 0:
        print "\n" + test_instance.return_formatted_status('STATUS_EVERYTHING_OK', "The program terminated normally.")
    else:
        print "\n" + test_instance.return_formatted_status('STATUS_GENERAL_ERROR', "This program encountered a general error during runtime.")
    
