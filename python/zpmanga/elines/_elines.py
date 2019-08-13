'''
emission line list
'''

from collections import ChainMap

balmer_high = {
    'H_30': 3662.220,
    'H_29': 3663.410,
    'H_28': 3664.650,
    'H_27': 3666.080,
    'H_26': 3667.730,
    'H_25': 3669.450,
    'H_24': 3671.320,
    'H_23': 3673.810,
    'H_22': 3676.376,
    'H_21': 3679.370,
    'H_20': 3682.823,
    'H_19': 3686.931,
    'H_18': 3691.551,
    'H_17': 3697.157,
    'H_16': 3703.859,
    'H_15': 3711.978,
    'H_14': 3721.946,
    'H_13': 3734.369,
    'H_12': 3750.151,
    'H_11': 3770.633,
    'H_10': 3797.900,
    'H_9': 3835.397,
    'H_8': 3889.064
}

balmer_low = {
    'H_epsilon': 3970.075,
    'H_delta': 4101.709,
    'H_gamma': 4340.437,
    'H_beta': 4861.350,
    'H_alpha': 6562.790
}

paschen = {
    'P18': 8437.9500,
    'P17': 8467.2600,
    'P16': 8502.4900,
    'P15': 8545.3800,
    'P14': 8598.3900,
    'P13': 8665.0200,
    'P12': 8750.4600,
    'P11': 8862.8900,
    'P10': 9015.3000,
    'P9': 9229.7000,
    'P8': 9546.2000
}

helium = {
    'HeI_5876': 5875.621,
    'HeI_3819': 3819.607,
    'HeI_3889': 3888.648,
    'HeI_4026': 4026.191,
    'HeI_4388': 4387.930,
    'HeI_4471': 4471.480,
    'HeII_4685': 4685.703,
    'HeI_4922': 4921.931,
    'HeI_5015': 5015.678,
    'HeI_5047': 5047.738,
    'HeI_6678': 6678.151,
    'HeI_7065': 7065.190,
    'HeI_7281': 7281.349
}

bright_metal = {
    'OII_3726': 3726.040,
    'OII_3729': 3728.800,
    'NeIII_3869': 3868.760,
    'OIII_4959': 4958.911,
    'OIII_5007': 5006.843,
    'NII_6548': 6548.050,
    'NII_6584': 6583.450,
    'SII_6717': 6716.440,
    'SII_6731': 6730.815
}

faint_metal = {
    'NeIII_3967': 3967.470,
    'SII_4069': 4068.600,
    'SII_4076': 4076.350,
    'OIII_4363': 4363.209,
    'FeIII_4658': 4658.050,
    'FeIII_4702': 4701.53,
    'FeIV_4704': 4703.426,
    'ArIV_4711': 4711.37,
    'ArIV_4740': 4740.16,
    'FeIII_4989': 4988.8,
    'NI_5197': 5197.902,
    'FeIII_5270': 5270.400,
    'ClIII_5518': 5517.709,
    'ClIII_5538': 5537.873,
    'NII_5755': 5754.590,
    'OI_6300': 6300.304,
    'SIII_6312': 6312.060,
    'OI_6363': 6363.776,
    'ArIII_7135': 7135.800,
    'OII_7319': 7319.920,
    'OII_7330': 7330.190,
    'ArIII_7751': 7751.060,
    'ArIII_8036': 8036.520,
    'OI_8446': 8446.3600,
    'ClII_8585': 8585.9700,
    'N_I_8683': 8683.4000,
    'SIII_8829': 8829.400,
    'SIII_9069': 9068.600,
    'SIII_9531': 9530.600
}

eline_ls = ChainMap(balmer_high, balmer_low, paschen, helium, bright_metal, faint_metal)
