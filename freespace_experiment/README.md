## Hanging by a thread: measurements in "free space"


In this experiment,  a reflector was placed on a clothesline--about maybe 6 meters above ground--and pushed out to around 5, 10 and 15 meters.

The goal was simply to look at how much variance there would be between distance estimation algorithms and between individual measurements.


The `_raw.txt` files are values, including "low quality" ones, as they came out.  The `_lp.txt` are low-passed, in the sense that a small averaging window was applied to the values, and only "high quality" tones were accepted.

This is the output from [profile_analysis.py](../profile_analysis.py), which just counts the failure rate (reported as a value of exactly 0.00), ignores those entries and finds the mean and std dev for each type of distance estimation algorithm.

Raw data:

```
 ******** clothesline_5m_raw.txt ********
351 samples, RSSI -62.1/1.721 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	3.484	0.1687	117	66.7%
     phase:	5.118	0.5049	198	43.6%
       rtt:	3.808	2.1380	319	9.1%
phase: 31.9% greater distance (1.63m) 
  rtt: 8.5% greater distance (0.32m) 



 ******** clothesline_10m_raw.txt ********
537 samples, RSSI -62.0/2.490 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	8.485	0.4290	235	56.2%
     phase:	10.909	0.5605	373	30.5%
       rtt:	8.779	2.5830	534	0.6%
phase: 22.2% greater distance (2.42m) 
  rtt: 3.3% greater distance (0.29m) 



 ******** clothesline_15m_raw.txt ********
389 samples, RSSI -65.1/2.949 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	10.673	0.5120	42	89.2%
     phase:	14.287	0.8459	97	75.1%
       rtt:	11.021	3.5772	383	1.5%
phase: 25.3% greater distance (3.61m) 
  rtt: 3.2% greater distance (0.35m) 


```


Filtered data:

```
 ******** clothesline_5m_lp.txt ********
182 samples, RSSI -62.1/1.698 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	3.470	0.1941	174	4.4%
     phase:	5.215	0.4845	182	0.0%
       rtt:	3.459	2.0194	182	0.0%
phase: 33.7% greater distance (1.76m) 



 ******** clothesline_10m_lp.txt ********
61 samples, RSSI -61.6/2.672 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	8.452	0.7234	59	3.3%
     phase:	11.053	0.5977	61	0.0%
       rtt:	8.888	2.3392	61	0.0%
phase: 23.5% greater distance (2.60m) 
  rtt: 4.9% greater distance (0.44m) 



 ******** clothesline_15m_lp.txt ********
100 samples, RSSI -63.9/2.725 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	10.685	0.6288	84	16.0%
     phase:	13.748	0.6981	100	0.0%
       rtt:	11.146	2.5512	100	0.0%
phase: 22.3% greater distance (3.06m) 
  rtt: 4.1% greater distance (0.46m) 



```


