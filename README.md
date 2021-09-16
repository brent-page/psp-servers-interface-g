# PSP servers interface

Python routines for browsing and loading data from PSP data servers

Typical Usage:

* Browsing available data products at level 2:
```
>>> get_products_FIELDS(level = 2)
['dfb_ac_bpf/', 'dfb_ac_spec/', 'dfb_ac_xspec/', 'dfb_dbm_dvac/', 'dfb_dbm_dvdc/', 'dfb_dbm_scm/', 'dfb_dbm_vdc/', 'dfb_dc_bpf/', 'dfb_dc_spec/', 'dfb_dc_xspec/', 'dfb_wf_dvdc/', 'dfb_wf_scm/', 'dfb_wf_vdc/', 'f2_100bps/', 'mag_RTN/', 'mag_RTN_1_min/', 'mag_RTN_1min/', 'mag_RTN_4_Sa_per_Cyc/', 'mag_SC/', 'mag_SC_1_min/', 'mag_SC_1min/', 'mag_SC_4_Sa_per_Cyc/', 'mag_VSO/', 'rfs_burst/', 'rfs_hfr/', 'rfs_lfr/', 'rfs_lfr_ne/', 'tds_wf/']
```

* Getting a list of all cdfs from dfb_dbm_dvac at level 2 in March of 2019:
```
>>> get_paths_FIELDS('dfb_dbm_dvac', level = 2, years = 2019, months = 3)
['http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032518_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032518_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032600_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032600_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032606_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032606_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032618_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032618_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032700_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032700_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032706_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032706_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032718_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032718_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032800_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032800_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032806_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032806_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032818_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032818_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032900_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032900_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032906_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032906_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032918_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032918_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033100_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033100_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033106_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033106_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033112_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033112_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033118_v01.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019033118_v02.cdf']
```

* Further specifying the day to be the 26th and the version to be 2:
```
>>> get_paths_FIELDS('dfb_dbm_dvac', level = 2, years = 2019, months = 3, days = 26, ver = 2)
['http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032600_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032606_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032618_v02.cdf']
```

* Further specifying interest in events at hours 3 and 23:
```
>>> get_paths_FIELDS('dfb_dbm_dvac', level = 2, years = 2019, months = 3, days = 26, hours = [3, 23], ver = 2)
['http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032600_v02.cdf', 'http://sprg.ssl.berkeley.edu/data/spp/data/sci/fields/staging/l2/dfb_dbm_dvac/2019/03/psp_fld_l2_dfb_dbm_dvac_2019032618_v02.cdf']
```

* Load the cdf spanning hours 00-06 into the Python shell:
```
>>> new_cdf = get_cdf(get_paths_FIELDS('dfb_dbm_dvac', level = 2, years = 2019, months = 3, days = 26, hours = [3, 26], ver = 2)[0])
```

* Or download the cdfs into the current working directory:
```
>>> download_files(paths = get_paths_FIELDS('dfb_dbm_dvac', level = 2, years = 2019, months = 3, days = 26, hours = [3, 23], ver = 2), directory = './')
```
