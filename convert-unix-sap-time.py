import re
import datetime
import pytz

def convert_sap_time(str_dt_offset, str_tz):
    '''
    Convert SAP datetime offset into a normal datetime.
    Step 1: use regex to extract the offset.
    Step 2: convert the offset into UTC datetime.
    Step 3: convert UTC to local timezone.  
    
    Example: '/Date(1569613743944)/'
    
    Time zones in pytz
        'America/Los_Angeles': [x for x in pytz.all_timezones if 'Angeles' in x]
        'UTC': [x for x in pytz.all_timezones if 'UTC' in x]
    
    Imports:
        re
        datetime
        pytz
        pandas as pd
    Inputs:
        str_dt_offset
        str_tz
    Returns:
        result : datetime in specific time-zome, e.g. Pacific Time
    
    Usage:
      
    print('Test out the convert_sap_time() function ...')
    print('Convert examples of sap_time ...')

    # convert SAP time to UTC timezone
    result1 = convert_sap_time('/Date(1504224000000)/', 'UTC')
    print('result1', result1)
    
    # convert SAP time to Los Angeles timezone
    result2 = convert_sap_time('/Date(1504224000000)/', 'America/Los_Angeles')
    print('result2', result2)
    
    References:
        https://blogs.sap.com/2013/04/28/working-with-odata-dates/
        https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
        https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
        https://docs.python.org/3.7/library/re.html
        https://avilpage.com/2014/11/python-unix-timestamp-utc-and-their.html
        https://www.calazan.com/dealing-datetime-objects-and-time-zones-python-3/
        https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
    '''
    str_dt_offset = str(str_dt_offset)
    str_regex = '/Date\((.+?)\)'

    try:
        found = re.search(str_regex, str_dt_offset).group(1)
        assert len(found) == 13
        str_found = (found[:-3] + '.' + found[-3:])
        float_found = float(str_found)
        
        convert_timezone = pytz.timezone(str_tz)
        dt_utc = datetime.datetime.utcfromtimestamp(float_found).replace(tzinfo=pytz.utc)
        result = dt_utc.astimezone(tz=convert_timezone)
        
    except AttributeError:
        # AAA, ZZZ not found in the original string
        result = pd.NaT
    
    return result
