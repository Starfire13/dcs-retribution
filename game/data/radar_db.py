from dcs.ships import (
    ALBATROS,
    CVN_71,
    CVN_72,
    CVN_73,
    CV_1143_5,
    Forrestal,
    KUZNECOW,
    LHA_Tarawa,
    MOLNIYA,
    MOSCOW,
    NEUSTRASH,
    PERRY,
    PIOTR,
    REZKY,
    Stennis,
    TICONDEROG,
    Type_052B,
    Type_052C,
    Type_054A,
    USS_Arleigh_Burke_IIa,
    VINSON,
)
from dcs.vehicles import AirDefence

from pydcs_extensions import highdigitsams as hds
from pydcs_extensions import vietnamwarvessels as vwv
from pydcs_extensions import chinesemilitaryassetspack as cmap
from pydcs_extensions import russianmilitaryassetspack as rmap


TELARS = {
    AirDefence.x_2S6_Tunguska,
    AirDefence.SA_11_Buk_LN_9A310M1,
    AirDefence.Osa_9A33_ln,
    AirDefence.Tor_9A331,
    AirDefence.Roland_ADS,
    hds.SAM_SA_17_Buk_M1_2_LN_9A310M1_2,
    cmap.PGL_625,
    cmap.HQ17A,
    rmap.CH_BukM3_9A317M,
    rmap.CH_BukM3_9A317MA,
    rmap.CH_S350_50P6_9M96D,
    rmap.CH_S350_50P6_9M100,
}

TRACK_RADARS = {
    AirDefence.Kub_1S91_str,
    AirDefence.snr_s_125_tr,
    AirDefence.S_300PS_40B6M_tr,
    AirDefence.S_300PS_5H63C_30H6_tr,
    AirDefence.Hawk_tr,
    AirDefence.Patriot_str,
    AirDefence.SNR_75V,
    AirDefence.RPC_5N62V,
    AirDefence.rapier_fsa_blindfire_radar,
    AirDefence.HQ_7_STR_SP,
    AirDefence.NASAMS_Radar_MPQ64F1,
    hds.SAM_SA_10B_S_300PS_30N6_TR,
    hds.SAM_SA_12_S_300V_9S32_TR,
    hds.SAM_SA_20_S_300PMU1_TR_30N6E,
    hds.SAM_SA_20B_S_300PMU2_TR_92H6E_truck,
    hds.SAM_SA_23_S_300VM_9S32ME_TR,
    cmap.CH_HQ22_STR,
    rmap.CH_BukM3_9S36M,
    rmap.CH_S350_50N6,
}

LAUNCHER_TRACKER_PAIRS = {
    AirDefence.Kub_2P25_ln: (AirDefence.Kub_1S91_str,),
    AirDefence.x_5p73_s_125_ln: (AirDefence.snr_s_125_tr,),
    AirDefence.S_300PS_5P85C_ln: (
        AirDefence.S_300PS_40B6M_tr,
        AirDefence.S_300PS_5H63C_30H6_tr,
    ),
    AirDefence.S_300PS_5P85D_ln: (
        AirDefence.S_300PS_40B6M_tr,
        AirDefence.S_300PS_5H63C_30H6_tr,
    ),
    AirDefence.Hawk_ln: (AirDefence.Hawk_tr,),
    AirDefence.Patriot_ln: (AirDefence.Patriot_str,),
    AirDefence.S_75M_Volhov: (AirDefence.SNR_75V,),
    AirDefence.rapier_fsa_launcher: (AirDefence.rapier_fsa_blindfire_radar,),
    AirDefence.HQ_7_LN_SP: (AirDefence.HQ_7_STR_SP,),
    AirDefence.S_200_Launcher: (AirDefence.RPC_5N62V,),
    AirDefence.NASAMS_LN_B: (AirDefence.NASAMS_Radar_MPQ64F1,),
    AirDefence.NASAMS_LN_C: (AirDefence.NASAMS_Radar_MPQ64F1,),
    hds.SAM_SA_2__V759__LN_SM_90: (AirDefence.SNR_75V,),
    hds.SAM_HQ_2_LN_SM_90: (AirDefence.SNR_75V,),
    hds.SAM_SA_3__V_601P__LN_5P73: (AirDefence.snr_s_125_tr,),
    hds.SAM_SA_10B_S_300PS_5P85SE_LN: (hds.SAM_SA_10B_S_300PS_30N6_TR,),
    hds.SAM_SA_10B_S_300PS_5P85SU_LN: (hds.SAM_SA_10B_S_300PS_30N6_TR,),
    hds.SAM_SA_12_S_300V_9A82_LN: (hds.SAM_SA_12_S_300V_9S32_TR,),
    hds.SAM_SA_12_S_300V_9A83_LN: (hds.SAM_SA_12_S_300V_9S32_TR,),
    hds.SAM_SA_20_S_300PMU1_LN_5P85CE: (hds.SAM_SA_20_S_300PMU1_TR_30N6E,),
    hds.SAM_SA_20_S_300PMU1_LN_5P85DE: (hds.SAM_SA_20_S_300PMU1_TR_30N6E,),
    hds.SAM_SA_20B_S_300PMU2_LN_5P85SE2: (hds.SAM_SA_20B_S_300PMU2_TR_92H6E_truck,),
    hds.SAM_SA_23_S_300VM_9A82ME_LN: (hds.SAM_SA_23_S_300VM_9S32ME_TR,),
    hds.SAM_SA_23_S_300VM_9A83ME_LN: (hds.SAM_SA_23_S_300VM_9S32ME_TR,),
    cmap.CH_HQ22_LN: (cmap.CH_HQ22_STR,),
    rmap.CH_BukM3_9A317M: (rmap.CH_BukM3_9S36M,),
    rmap.CH_BukM3_9A317MA: (rmap.CH_BukM3_9S36M,),
    rmap.CH_S350_50P6_9M96D: (rmap.CH_S350_50N6,),
    rmap.CH_S350_50P6_9M100: (rmap.CH_S350_50N6,),
}

UNITS_WITH_RADAR = {
    # Radars
    AirDefence.x_2S6_Tunguska,
    AirDefence.SA_11_Buk_LN_9A310M1,
    AirDefence.Osa_9A33_ln,
    AirDefence.Tor_9A331,
    AirDefence.Gepard,
    AirDefence.Vulcan,
    AirDefence.Roland_ADS,
    AirDefence.ZSU_23_4_Shilka,
    AirDefence.x_1L13_EWR,
    AirDefence.Kub_1S91_str,
    AirDefence.S_300PS_40B6M_tr,
    AirDefence.S_300PS_40B6MD_sr,
    AirDefence.x_55G6_EWR,
    AirDefence.S_300PS_64H6E_sr,
    AirDefence.SA_11_Buk_SR_9S18M1,
    AirDefence.Dog_Ear_radar,
    AirDefence.Hawk_tr,
    AirDefence.Hawk_sr,
    AirDefence.Patriot_str,
    AirDefence.Hawk_cwar,
    AirDefence.p_19_s_125_sr,
    AirDefence.Roland_Radar,
    AirDefence.snr_s_125_tr,
    AirDefence.SNR_75V,
    AirDefence.RLS_19J6,
    AirDefence.RPC_5N62V,
    AirDefence.rapier_fsa_blindfire_radar,
    AirDefence.HQ_7_LN_SP,
    AirDefence.HQ_7_STR_SP,
    AirDefence.FuMG_401,
    AirDefence.FuSe_65,
    cmap.PGL_625,
    cmap.HQ17A,
    cmap.CH_PGZ09,
    cmap.CH_HQ22_SR,
    cmap.CH_HQ22_STR,
    cmap.CH_LD3000,
    cmap.CH_LD3000_stationary,
    cmap.CH_PGZ95,
    rmap.PantsirS1,
    rmap.PantsirS2,
    rmap.TorM2,
    rmap.TorM2K,
    rmap.TorM2M,
    rmap.CH_S350_96L6,
    rmap.CH_S350_50N6,
    rmap.CH_BukM3_9S18M13,
    rmap.CH_BukM3_9S36M,
    # Ships
    ALBATROS,
    CVN_71,
    CVN_72,
    CVN_73,
    CV_1143_5,
    Forrestal,
    KUZNECOW,
    LHA_Tarawa,
    MOLNIYA,
    MOSCOW,
    NEUSTRASH,
    PERRY,
    PIOTR,
    REZKY,
    Stennis,
    TICONDEROG,
    Type_052B,
    Type_052C,
    Type_054A,
    USS_Arleigh_Burke_IIa,
    VINSON,
    vwv.Cva_31,
    vwv.USS_Fletcher,
    vwv.USS_Laffey,
    vwv.USS_Maddox,
    vwv.USS_Sumner,
    vwv.USS_The_Sullivans,
    cmap.CH_Type022,
    cmap.Type052D,
    cmap.CH_Type054B,
    cmap.Type055,
    cmap.CH_Type056A,
    rmap.Admiral_Gorshkov,
    rmap.CH_Steregushchiy,
    rmap.CH_Project22160,
    rmap.CH_Grigorovich_AShM,
    rmap.CH_Grigorovich_LACM,
    rmap.CH_Gremyashchiy_AShM,
    rmap.CH_Gremyashchiy_LACM,
}
