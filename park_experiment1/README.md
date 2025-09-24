## A walk in the park: Experiment 2, measurement precision


In this experiment,  a reflector was placed about 2m above the ground and marker flags positioned every 5 meters out to 45m.

The various log files were identified by where I was at the time and those used in calculations suffixed according to position (e.g. ...10m.txt for readings at the 10m mark).


Raw data was collected, allowing for "low quality" results, with no filtering and entry is of the form
```
18:13:56.607 profile,0,737,-67,1.00,11.276, 11.152,9.369 
```

  * profile line entry prefix marker 
  * connection id
  * reading index
  * rssi
  * quality as reported by CS
  * phase slope estimate
  * rtt estimate 
  * ifft estimate
  
## Analysis 

Running each file through the profiling analysis script gives the results below.  

The short of it is that:

  * RTT succeeds pretty much all the time, while other two methods are much more sensitive to disturbance
  
  * RTT has a lot of variance but averages out to a good value
  
  * RTT and iFFT mostly agree on distance, phase slope is alway reporting a greater value
  
  * moving from one position to the next would, if my markers were misplaced but estimates were accurate or consistent, lead to a corresponding increase in all three methods, but I don't think the delta between positions doesn't really show any good correlation.  So: need more diversity with antenna/better algo to get down to +/- 20cm.
  
  
This is the output from [profile_analysis.py](../profile_analysis.py), which just counts the failure rate (reported as a value of exactly 0.00), ignores those entries and finds the mean and std dev for each type of distance estimation algorithm.


```


 ******** serial_20250914_181226_5m.txt ********
138 samples, RSSI -60.9/1.808 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	5.317	0.1687	125	9.4%
     phase:	5.935	0.3141	138	0.0%
       rtt:	4.929	1.5513	138	0.0%
 ifft: 7.3% greater distance (0.39m) 
phase: 16.9% greater distance (1.01m) 



 ******** serial_20250914_181601_15m.txt ********
109 samples, RSSI -71.8/1.855 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	13.928	0.6359	56	48.6%
     phase:	17.620	1.1677	93	14.7%
       rtt:	13.467	3.7005	109	0.0%
 ifft: 3.3% greater distance (0.46m) 
phase: 23.6% greater distance (4.15m) 



 ******** serial_20250914_181931_25m.txt ********
154 samples, RSSI -72.2/3.472 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	24.273	0.4905	75	51.3%
     phase:	26.267	0.8041	112	27.3%
       rtt:	24.071	3.7002	154	0.0%
 ifft: 0.8% greater distance (0.20m) 
phase: 8.4% greater distance (2.20m) 



 ******** serial_20250914_182617_35m.txt ********
305 samples, RSSI -72.9/3.641 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	34.137	0.6287	106	65.2%
     phase:	35.928	0.8094	174	43.0%
       rtt:	34.414	3.8644	305	0.0%
phase: 5.0% greater distance (1.79m) 
  rtt: 0.8% greater distance (0.28m) 



 ******** serial_20250914_183711_45m.txt ********
178 samples, RSSI -72.7/1.578 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	43.688	0.2163	101	43.3%
     phase:	45.007	0.5906	147	17.4%
       rtt:	42.969	3.0220	178	0.0%
 ifft: 1.6% greater distance (0.72m) 
phase: 4.5% greater distance (2.04m) 



 ******** serial_20250914_181353_10m.txt ********
118 samples, RSSI -66.8/1.294 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	9.406	0.5040	106	10.2%
     phase:	11.454	0.7474	118	0.0%
       rtt:	9.378	2.7367	118	0.0%
phase: 18.1% greater distance (2.08m) 



 ******** serial_20250914_181601_15m.txt ********
109 samples, RSSI -71.8/1.855 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	13.928	0.6359	56	48.6%
     phase:	17.620	1.1677	93	14.7%
       rtt:	13.467	3.7005	109	0.0%
 ifft: 3.3% greater distance (0.46m) 
phase: 23.6% greater distance (4.15m) 



 ******** serial_20250914_181750_20m.txt ********
155 samples, RSSI -75.7/3.205 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	19.410	0.1779	24	84.5%
     phase:	24.864	2.0704	61	60.6%
       rtt:	19.573	4.9122	154	0.6%
phase: 21.9% greater distance (5.45m) 
  rtt: 0.8% greater distance (0.16m) 



 ******** serial_20250914_181931_25m.txt ********
154 samples, RSSI -72.2/3.472 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	24.273	0.4905	75	51.3%
     phase:	26.267	0.8041	112	27.3%
       rtt:	24.071	3.7002	154	0.0%
 ifft: 0.8% greater distance (0.20m) 
phase: 8.4% greater distance (2.20m) 



 ******** serial_20250914_182105_30m.txt ********
143 samples, RSSI -74.0/1.844 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	29.411	0.3390	39	72.7%
     phase:	31.866	0.8453	71	50.3%
       rtt:	28.452	3.6090	143	0.0%
 ifft: 3.3% greater distance (0.96m) 
phase: 10.7% greater distance (3.41m) 



 ******** serial_20250914_182617_35m.txt ********
305 samples, RSSI -72.9/3.641 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	34.137	0.6287	106	65.2%
     phase:	35.928	0.8094	174	43.0%
       rtt:	34.414	3.8644	305	0.0%
phase: 5.0% greater distance (1.79m) 
  rtt: 0.8% greater distance (0.28m) 



 ******** serial_20250914_182915_40m.txt ********
139 samples, RSSI -72.0/1.160 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	38.819	0.2038	71	48.9%
     phase:	39.981	0.6231	118	15.1%
       rtt:	38.279	2.8939	139	0.0%
 ifft: 1.4% greater distance (0.54m) 
phase: 4.3% greater distance (1.70m) 



 ******** serial_20250914_183711_45m.txt ********
178 samples, RSSI -72.7/1.578 report:
      algo:	avg	std	pts	fail rate
------------------------------------------------
      ifft:	43.688	0.2163	101	43.3%
     phase:	45.007	0.5906	147	17.4%
       rtt:	42.969	3.0220	178	0.0%
 ifft: 1.6% greater distance (0.72m) 
phase: 4.5% greater distance (2.04m) 

```


