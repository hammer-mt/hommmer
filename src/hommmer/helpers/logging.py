# print logs if verbose
def log(string):
    print(string) if VERBOSE else False

# set a global variable for logging
def init_logging(verbose):
    global VERBOSE
    if verbose:
        VERBOSE = True
    else:
        VERBOSE = False