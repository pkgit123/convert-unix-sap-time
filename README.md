# convert-unix-sap-time
Convert Unix epoch time (aka SAP Timestamp)

Unix operating system counts time as the number of seconds elasped since Jan 1, 1970 UTC (aka GMT).  SAP also uses this same format, referred as SAP datetime offset.

However most data analysis uses standard datetime formats, not Unix/SAP time.  So this is a helper function to convert to normal time format, and optionally convert to local timezone.

Example input:
* Unix time - '1601582856'
* SAP datetime offset - '/Date(1569613743944)/'

Example output:
* UTC: 2017-09-01 00:00:00+00:00
* PST: 2017-08-31 17:00:00-07:00

References:
* https://en.wikipedia.org/wiki/Unix_time
* https://www.epochconverter.com/
* https://blogs.sap.com/2013/04/28/working-with-odata-dates/
* https://stackoverflow.com/questions/6999726/how-can-i-convert-a-datetime-object-to-milliseconds-since-epoch-unix-time-in-p
* https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
* https://docs.python.org/3.7/library/re.html
* https://avilpage.com/2014/11/python-unix-timestamp-utc-and-their.html
* https://www.calazan.com/dealing-datetime-objects-and-time-zones-python-3/
* https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
