# Python-Code als Lösungshilfe für die Paiwise-Übung in Abschnitt 9.2
# (CC) BY-NC-SA 4.0 - Röttger, Runze, Dietrich - aus dem Buch "Basiswissen KI-Testen" ISBN 978-3-86490-947-4

import os
import re
import itertools
#import math
from pathlib import Path

def parse_parameters(text):
    if not re.search("\n",text):
        filename = Path('./'+text)
        if filename.exists():
            text = filename.read_text()
    matches = re.findall(r"(?m:^\s*(\w[\w_-]+)\s*[:,]\s*(.*$))",text)
    parameters = {}
    for match in matches:
        values = match[1].split(",")
        for i in range(len(values)): values[i] = values[i].strip() 
        parameters[match[0]] = values
    return parameters

def print_parameters(parameters):
    maxwidth = 10
    for key in list(parameters):
         maxwidth = max(maxwidth, len(key)+1)
    for key in list(parameters):
        print('{0:<{width}} {values}'.format(key+":", width=maxwidth, values=', '.join(parameters[key])))
    print()

def parse_tests(text):
    if not re.search("\n",text):
        filename = Path('./'+text)
        if filename.exists():
            text = filename.read_text()
    lines = text.splitlines()
    # skip leading empty lines:
    while lines[0].strip()=='':
        lines = lines[1:]
    sep = re.compile(r"\s*[\s\t,;:]\s*")
    parameters = sep.split(lines[0])
    testcases = []
    for line in lines[1:]:
        testcases.append(dict(zip(parameters,sep.split(line))))
    return {'parameters':parameters,'tests':testcases}

def print_tests(tests):
    param     = tests['parameters'].copy()
    testcases = tests['tests']
    
    for i in range(len(param)):
        param[i] = {'param':param[i], 'width':len(param[i])}
    for parameter in param:
        for testcase in testcases:
            if parameter['param'] in testcase:
                parameter['width'] = max(parameter['width'],len(str(testcase[parameter['param']])))

    for parameter in param:
        print('{0:<{width}}'.format(parameter['param'],width=parameter['width']), end=' | ')
    print()
    for parameter in param:
        print('-' * parameter['width'],end='-|-')
    print()
    for testcase in testcases:
        for parameter in param:
            if parameter['param'] in testcase:
                print('{:{width}}'.format(testcase[parameter['param']],width=parameter['width']), end=' | ')
            else:
                print('{:^{width}}'.format("---",width=parameter['width']), end=' | ')
        print()
    print()

def check(parameters, tests, verb=0):
    pparam = list(parameters)
    tparam = list(tests['parameters'])
    param  = []
    for p in pparam:
        if p in tparam: param.append(p)
    n = len(param)
    nparam  = []
    numcomb = 1
    for p in param:
        num = len(parameters[p])
        nparam.append(num)
        numcomb *= num

    comb = list(itertools.combinations(param,2))
    comb_numeric = list(itertools.combinations(range(len(param)),2))
    pwcount=0
    for par in comb:
        pwcount += len(parameters[par[0]])*len(parameters[par[1]])
    
    print('CHECK FÜR PAARWEISES TESTEN')
    if verb>0:
        print('Parameter            : {}'.format(n), end=' ')
        print(param)  if verb>1 else print()
        print('Werte je Parameter   : {}'.format(nparam))
        if verb>1:
            for p in param:
                print('  {0:<19}: {1}'.format(p,parameters[p]))
        print('Volle Kombinationen  : {}'.format(numcomb))
        print('Parameterpaarungen   : {:n}'.format(n*(n-1)/2), end=' ')
        if verb==2:
            print('[',end='')
            for i in range(3):
                print(comb[i],end=', ')
            print('..., ',end='')
            print(comb[-1],']')
        elif verb>2:
            print(comb)
        else:
            print()
        #print(comb_numeric) if verb>1 else print()
    
    
    print('Anzahl Wertepaare    : {:n}'.format(pwcount)) if verb>0 else None
    print('Anzahl Testfälle     : {}'.format(len(tests['tests']))) if verb>0 else None
    
    missing = []
    found = []
    for par in comb:
        val = list(parameters[p] for p in par)
        for v0 in val[0]:
            for v1 in val[1]:
                pair = {par[0]:v0,par[1]:v1}
                num_tc=0
                for tc in tests['tests']:
                    if par[0] in tc and par[1] in tc:
                        if tc[par[0]]==v0 and tc[par[1]]==v1:
                            num_tc += 1
                if num_tc>0:
                    pwcount -= 1
                    #print('gefunden: {} mal.'.format(num_tc))
                else:
                    missing.append(pair)
    
    if verb>0: print()
    
    if pwcount==0:
        print('ALLE Parameter-Werte-Paarungen wurden gefunden! die Testfälle sind vollständig.')
    else:
        print('Die Testfälle decken NICHT alle Parameter-Werte-Paarungen ab, es fehlen {} Paare!'.format(len(missing)))
        for pair in missing:
            print(' ',pair) if verb>0 else None
    
