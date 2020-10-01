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
