import numpy as np
import urllib.request
import re
import os
from bs4 import BeautifulSoup as BS
import spacepy
from spacepy import pycdf

FIELDS_prefix = 'http://sprg.ssl.berkeley.edu/data/psp/data/sci/fields/'
SWEAP_prefix = 'http://sweap.cfa.harvard.edu/pub/data/sci/sweap/'

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# put FIELDS username and password here
USERNAME = ''
PASSWORD = ''

password_mgr.add_password(None, FIELDS_prefix, USERNAME, PASSWORD)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

def get_products_FIELDS(level=1):
    """Get the FIELDS data products from a given level.
    """

    prefix_full = FIELDS_prefix + 'l{}/'.format(level)
    pattern = '^[a-zA-Z].+'
    pattern = re.compile(pattern)
    products = []
    with urllib.request.urlopen(prefix_full) as response:
        html = response.read()
        soup = BS(html, 'html.parser')
        for link in soup.find_all('a'):
            string = link.get('href')
            if pattern.match(string):
                products.append(string)
    return products


def get_paths_FIELDS(product, level=1, years=None, months=None, days=None, hours=None, ver=None):
    """Get the urls for a desired set of FIELDS cdfs.

    Arguments:
        product (str): the desired data product
        level (int): the desired data level  
        years (None, int, or list of ints): If None, the function returns cdf urls from all available years.  If an int or list of ints, the function returns cdf urls from the specified year(s).
        months (None, int, or list of ints): analogous documentation to that of 'years'.
        days (None, int, or list of ints): analogous documentation to that of 'years'.
        hours (None, int, or list of ints): 
            For data products (like full-sampled mag) that are broken up into blocks of hours: if None, the function returns urls from all available hours.  If an int or list of ints, the function returns cdf urls for the specified hours.
            For data products that are broken up into days: specifying the hours has no effect.
        ver (None or int): If None, the function returns cdf urls for all data product versions.  If >= 0, returns the cdf urls for the specified version.
    """

    latest_ver = False
    if (ver == -1):
        latest_ver = True
        ver = None

    years_regexp, months_regexp, days_regexp, hours_regexp, ver_regexp = assemble_regexps(years, months, days, hours, ver)
    if (level == 1):
        sc_id = 'spp'
    else:
        sc_id = 'psp'
    prefix_full = '{}l{:d}/{}/'.format(FIELDS_prefix, level, product)
    patterns = [years_regexp, months_regexp, r'^{}_fld_l{:d}_{}.*_[0-9]{{6}}{}{}{}\.cdf$'.format(sc_id, level, product, days_regexp, hours_regexp, ver_regexp)]

    pattern_results = get_pattern_results(prefix_full, patterns)
    if latest_ver:
        pattern_results = to_latest_ver(pattern_results)

    return pattern_results

def to_latest_ver(pattern_results):
    vers_collected = {}
    latest_ver_files = []
    for fname in pattern_results:
        if fname[:-8] not in vers_collected.keys():
            vers_collected[fname[:-8]] = [fname]
        else:
            vers_collected[fname[:-8]].append(fname)
    for file_list in vers_collected.values():
        file_list.sort()
        latest_ver_files.append(file_list[-1])
    return latest_ver_files

def get_cdf(path):
    """Download and load a cdf file.

    Arguments:
        path (str): a url pointing to the desired cdf
    """
    fname = path[path.find('spp_fld'):]
    with urllib.request.urlopen(path) as response:
        cdf_file = open(fname, 'wb')
        cdf_file.write(response.read())
        cdf_file.close()

    cdf = spacepy.pycdf.CDF(fname)
    os.remove(fname)

    return cdf

def get_paths_SWEAP(subinst, subsubinst=None, level=2, years=None, months=None, days=None, ver=None):
    """Get the urls for a desired set of SWEAP cdfs.  

    Arguments:
        subinst (str): spc, spe, or spi
        subsubinst (str):
            spc: None
            spe:
                L2: spa_sf0, spa_sf1, spb_sf0, or spb_sf1
                L3: spa_sf0_pad, spb_sf0_pad, or spe_sf0_pad
            spi:
                L2: spi_sf00
                L3: spi_sf00 or spi_sf0a
        level (int): the desired data level  
        years (None, int, or list of ints): If None, the function returns cdf urls from all available years.  If an int or list of ints, the function returns cdf urls from the specified year(s).
        months (None, int, or list of ints): analogous documentation to that of 'years'.
        days (None, int, or list of ints): analogous documentation to that of 'years'.
        ver (None or int): If None, the function returns cdf urls for all data product versions.  If >= 0, returns the cdf urls for the specified version.
    """
    latest_ver = False
    if (ver == -1):
        latest_ver = True
        ver = None

    years_regexp, months_regexp, days_regexp, _, ver_regexp = assemble_regexps(years, months, days, None, ver)

    # subsubinst is None means subinst must be spc
    if (subsubinst is None):
        prefix_full = '{}{}/L{:d}/'.format(SWEAP_prefix, subinst, level)
        patterns = [years_regexp, months_regexp, r'^psp_swp_spc_l{:d}i_[0-9]{{6}}{}_{}\.cdf$'.format(level, days_regexp, ver_regexp)]
    else:
        prefix_full = '{}{}/L{:d}/{}/'.format(SWEAP_prefix, subinst, level, subsubinst)
        # positioning of 'L3' in cdf file names is different for pad cdfs
        if ('pad' in subsubinst):
            patterns = [years_regexp, months_regexp, r'^psp_swp_{}_L{:d}_pad.*_[0-9]{{6}}{}_{}\.cdf$'.format(subsubinst[:7], level, days_regexp, ver_regexp)]
        else:
            patterns = [years_regexp, months_regexp, r'^psp_swp_{}_L{:d}.*_[0-9]{{6}}{}_{}\.cdf$'.format(subsubinst, level, days_regexp, ver_regexp)]

    pattern_results = get_pattern_results(prefix_full, patterns)

    if latest_ver:
        pattern_results = to_latest_ver(pattern_results)

    return pattern_results

def download_files(paths, directory=''):
    """Download the files pointed to by a set of urls into a local directory

    Arguments:
        paths (list): a set of urls, each pointing to a file
        directory (str): local directory to download the files into
    """

    for path in paths:
        fname_start = path.find('spp_')
        if (fname_start == -1):
            fname_start = path.find('psp_')

        fname = path[fname_start:]
        with urllib.request.urlopen(path) as response:
            cdf_file = open(directory + fname, 'wb')
            cdf_file.write(response.read())
            cdf_file.close()

# backend function
def assemble_regexps(years, months, days, hours, ver):
    def regexp_any(my_list):
        regexp = '^(?:'
        for item in my_list:
            regexp += '{:02d}|'.format(item)
        regexp = regexp[:-1] + ')/'
        return regexp
    if (years is None):
        years_regexp = '^20[1-2][0-9]/'
    else:
        if isinstance(years, int):
            years = [years]
        years_regexp = regexp_any(years)

    if (months is None):
        months_regexp = '^[0-1][1-9]/'
    else:
        if isinstance(months, int):
            months = [months]
        months_regexp = regexp_any(months)

    if (days is None):
        days_regexp = '[0-3][1-9]'
    else:
        if isinstance(days, int):
            days = [days]
        days_regexp = '(?:'
        for day in days:
            days_regexp += '{:02d}|'.format(day)
        days_regexp = days_regexp[:-1] + ')'
    if (hours is None):
        hours_regexp = '(?:00_|06_|12_|18_|_)'
    else:
        if isinstance(hours, int):
            hours = np.array([hours])
        elif isinstance(hours, list):
            hours = np.array(hours)

        hours_regexp = '(?:'
        if np.any(hours < 6):
            hours_regexp += '00_|'
        if np.any((hours >= 6) & (hours < 12)):
            hours_regexp += '06_|'
        if np.any((hours >= 12) & (hours < 18)):
            hours_regexp += '12_|'
        if np.any(hours >= 18):
            hours_regexp += '18_|'

        hours_regexp = hours_regexp[:-1] + '|_)'

    if (ver is None):
        #latter option for FIELDS level 3 QTN 
        ver_regexp = 'v(?:[0][0-9]|[0-9].[0-9])'
    else:
        #latter option for FIELDS level 3 QTN 
        ver_regexp = 'v(?:{:02d}|{:1d}.[0-9])'.format(ver,ver)

    return years_regexp, months_regexp, days_regexp, hours_regexp, ver_regexp


# backend function
def get_pattern_results(prefix_full, patterns):
    pattern_results = [[] for i in range(len(patterns))]
    pattern_results.insert(0, [prefix_full])

    for i, pattern in enumerate(patterns):
        pattern = re.compile(pattern)
        for pattern_result in pattern_results[i]:
            with urllib.request.urlopen(pattern_result) as response:
                html = response.read()
                soup = BS(html, 'html.parser')
                for link in soup.find_all('a'):
                    result = pattern.findall(link.get('href'))
                    if len(result) > 0:
                        pattern_results[i + 1].append(pattern_result + result[0])
    return pattern_results[-1]
