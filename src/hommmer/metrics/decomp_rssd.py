import numpy as np
# https://github.com/facebookexperimental/Robyn/issues/82#issuecomment-845846447
# https://github.com/facebookexperimental/Robyn/issues/110
# https://github.com/facebookexperimental/Robyn/blob/dbd8d1f0e640265d5c0a1c3750e51ccf5e3e117d/source/fb_robyn.func.R#L1177
# https://github.com/facebookexperimental/Robyn/issues/95

# decomposition distance (DECOMP.RSSD, decomposition root-sum-square distance, a major innovation of Facebook Robyn
# The intuition is this: assuming you're spending 90% on TV and 10% on FB. If you get 10% effect for TV and 90% for FB, 
# you'd probably not believe this result, no matter how low the model error (NRMSE) is. If you get 80% TV and 20% FB as 
# effect share, it'll more "realistic". This is where the logic is from: minimising the distance between share of spend 
# and share of effect. It's really about getting rid of the very extreme cases and have a set of results that are more realistic.

# decomposition root sum of squared distance
def decomp_rssd(effect_share, spend_share):
    value = round(np.sqrt(sum((np.array(effect_share)-np.array(spend_share))**2)),3)
    passed = "✔️" if value < 0.5 else "❌"
    return value, passed

