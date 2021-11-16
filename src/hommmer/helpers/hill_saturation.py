def hill_transform(x, ec, slope):
    # https://github.com/sibylhe/mmm_stan#13-diminishing-return
    return 1 / (1 + (x / ec)**(-slope))