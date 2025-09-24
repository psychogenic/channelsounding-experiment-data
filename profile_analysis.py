#!/usr/bin/env python
import argparse
import re 
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
import json


def getArgs():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Profiling log analyser')
    parser.add_argument('log_files', type=str, nargs='+', help='Path to the log file')
    parser.add_argument('--csv', action='store_true', help='output as CSV')
    args = parser.parse_args()
    return args
    

def extractLinesAsCSV(filepath:str, prefix:str):
    retLines = []
    matcher = re.compile(f'.*({prefix}.*)$')
    # print(matcher)
    with open(filepath, 'r') as f:
        
        ln = f.readline()
        while ln:
            m = matcher.match(ln)
            if m:
                # print(ln)
                v = m.group(1).split(',')
                #yo = re.sub(r'[^0-9]+$', '', v[-1])
                #v[-1] = yo
                vals = []
                for av in v:
                    try:
                        x = float(av) 
                        if x == int(x):
                            vals.append(int(x))
                        else:
                            vals.append(x)
                            
                    except:
                        vals.append(av)
                retLines.append(vals)
            ln = f.readline()
    
    return retLines
    

def getProfileData(from_logfile:str):
    all_entries = extractLinesAsCSV(from_logfile, 'profile,')
    header =  ['profile', 'conn', 'index', 'rssi', 'quality', 'phase', 'rtt', 'ifft']
    
    return  pd.DataFrame(all_entries, columns=header)
    
def summarizeProfileData(dataframe:pd.DataFrame):
    
    
    num_samps = len(dataframe)
    report = {
    
        'num_samples': num_samps,
        'rssi_mean': dataframe['rssi'].mean(),
        'rssi_std': dataframe['rssi'].std(),
        'min_dist': 0
    }
    
    min_dist = 1e6
    for algo in ['ifft', 'phase', 'rtt']:
        filtered = dataframe[dataframe[algo] != 0.0][algo]
        meanval = filtered.mean()
        numfails = dataframe[algo].value_counts().get(0.0, 0)
        if meanval < min_dist:
            min_dist = meanval
        algodetails = {
            'mean': meanval,
            'std': filtered.std(),
            'fails': numfails,
            'success': num_samps - numfails,
            'failure_rate': numfails/num_samps,
            'mean_delta_min': 0
        
        }
        report[algo] = algodetails
        dataframe[f'{algo}_delta'] = dataframe[algo] - meanval
        
    report['min_dist'] = min_dist
    for algo in ['ifft', 'phase', 'rtt']:
        if report[algo]['mean'] - min_dist > 0.1:
            report[algo]['mean_delta_min'] = report[algo]['mean'] - min_dist
    return report
    
    
    

def displayWinners(winners, keyidx:int):
            
    numWinnersToPrint = 15
    
    winners_p = list(reversed(sorted(winners['pearson'], key=lambda x: x[keyidx])))
    winners_s = list(reversed(sorted(winners['spearman'], key=lambda x: x[keyidx])))
    
    print("       Pearson " + ' '*60 + " Spearman  ")
    for i in range(numWinnersToPrint):
        outstr = ''
        if i < len(winners_p):
            w = winners_p[i]
            outstr = f'{w[0].ljust(35)} cor:{w[1]:.3f} p={w[2]:.3f}'
            olen = len(outstr)
            outstr += ' '*(70 - olen)
        else:
            outstr = ' '*30
        
        if i < len(winners_s):
            w = winners_s[i]
            outstr += f'{w[0].ljust(35)} cor={w[1]:.3f} p={w[2]:.3f}'
        
        print(outstr)
        
        
        

def findCorrelations(df:pd.DataFrame, param_cols:list, result_cols:list):
    
    X = df[param_cols]
    Y = df[result_cols]
    
    # Initialize a dictionary to store correlation results
    correlations = {}

    # Calculate correlations for each parameter-result pair
    for p in param_cols:
        correlations[p] = {}
        for r in result_cols:
            # Pearson correlation
            pearson_corr, pearson_p = pearsonr(X[p], Y[r])
            #pearson_corr = 1 
            # pearson_p = 2
            # Spearman correlation (for non-linear relationships)
            spearman_corr, spearman_p = spearmanr(X[p], Y[r])
            correlations[p][r] = {
                'pearson': pearson_corr,
                'pearson_p': pearson_p,
                'spearman': spearman_corr,
                'spearman_p': spearman_p
            }

    # Display correlations
    pMinimum = 0.06
    
    winners = {
        'pearson': [],
        'spearman': []
    }
    
    for p in correlations:
        for r in correlations[p]:
            pearson_corr = correlations[p][r]['pearson']
            pearson_p = correlations[p][r]['pearson_p']
            spearman_corr = correlations[p][r]['spearman']
            spearman_p = correlations[p][r]['spearman_p']
            if all(np.isnan(val) for val in [pearson_corr, spearman_corr]):
                continue
            
            if pearson_p < pMinimum and spearman_p < pMinimum:
                continue 
            if np.isnan(pearson_corr) or pearson_p < 0.1:
                pstring = ''  
            else:
                pstring = f"(Pr){pearson_corr:.3f} (p-val: {pearson_p:.3e})"
                winners['pearson'].append((f'{p} - {r}', pearson_corr, pearson_p))
                
            if np.isnan(spearman_corr) or spearman_p < 0.1:
                sstring = ''
            else:
                sstring = f"(Sp){spearman_corr:.3f} (p-val: {spearman_p:.3e})"
                winners['spearman'].append((f'{p} - {r}', spearman_corr, spearman_p))
                
            print(f"{p}<->{r}: {pstring} {sstring}")
            
            
    
    
    
    print("\n\n\n***  Winners: strongest p-value ***")
    displayWinners(winners, 2)
    
    print("\n\n***  Winners: strongest correlation ***")
    displayWinners(winners, 1)
    
    

def summarize(filepath:str, args):
    vals = getProfileData(filepath)
    rep = summarizeProfileData(vals)
    
    if args.csv:
        for algo in ['ifft', 'phase', 'rtt']:
            d = rep[algo]
            print(f'{d['mean']:.3f},', end='')
        
        print()
                    
    else:
        print(f'\n\n ******** {filepath} ********')
        print(f'{rep['num_samples']} samples, RSSI {rep['rssi_mean']:.1f}/{rep['rssi_std']:.3f} report:')
        
        print('      algo:\tavg\tstd\tpts\tfail rate')
        print('------------------------------------------------')
        for algo in ['ifft', 'phase', 'rtt']:
            d = rep[algo]
            print(f'{algo:>10}:\t{d['mean']:.3f}\t{d['std']:.4f}\t{d['success']}\t{d['failure_rate']*100:.1f}%')
            
        for algo in ['ifft', 'phase', 'rtt']:
            if rep[algo]['mean_delta_min']:
                percentage = (rep[algo]['mean_delta_min']/rep[algo]['mean']) * 100.0
                print(f'{algo:>5}: {percentage:.1f}% greater distance ({rep[algo]['mean_delta_min']:.2f}m) ')
        
        print()
        
def main():
    args = getArgs()
    for log_file in args.log_files:
        summarize(log_file, args)

    

if __name__ == '__main__':
    main()
    
    
