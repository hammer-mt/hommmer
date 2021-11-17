# https://github.com/sibylhe/mmm_stan#13-diminishing-return
def hill_saturation(x, ec, slope):
    return 1 / (1 + (x / ec)**(-slope))