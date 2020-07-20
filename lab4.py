
# VARIANT 16

# from nltk import ngrams # ngrams(text, n)

from time import time
from collections import Counter
from re import findall

def impulseFunction(polDegree):
    impF = str()
    for i in range(0, polDegree-1):
        impF += '0'
    return impF + '1'

def L1(impF, maxPeriod, polDegree): #
    rs = impF
    for i in range(0,maxPeriod-polDegree):
        rs += str(int(rs[i+17])^int(rs[i+16])^int(rs[i+14])^int(rs[i+13])^int(rs[i+12])^int(rs[i+6])^int(rs[i+4])^int(rs[i+0]))
    return rs

def L2(impF, maxPeriod, polDegree): #
    rs = impF
    for i in range(0,maxPeriod-polDegree):
        rs += str(int(rs[i+19])^int(rs[i+17])^int(rs[i+16])^int(rs[i+15])^int(rs[i+12])^int(rs[i+10])^int(rs[i+8])^int(rs[i+6])^int(rs[i+3])^int(rs[i+0]))
    return rs

def period(recurrenceSequence, impulseFunction):
    period = 1  
    for i in range(1, len(recurrenceSequence)):
        if recurrenceSequence[i:i+len(impulseFunction)] == impulseFunction:
            return period
        else:
            period += 1
    return period

def whatIsPolynomial(polynomial, period, maxPeriod):
    print('Поліном: ' + polynomial)
    print('Період: ' + str(period))
    print('Максимальний період: '+ str(maxPeriod))
    if period == maxPeriod:
        print("Примітивний, з чого слідує що він незвідний")
    else:
        if maxPeriod % period == 0:
            print("Непримітивний, можливо незвідний, бо період ділить максимальний період")
        else:
            print("Непримітивний, звідний")
     
def autoCorrelation(polynomial, newRs, period=10):     # 10 по методе   
    autoCor = dict()
    for d in range(0, period+1):                                         
        shiftedRs = newRs[len(newRs)-d:] + newRs[:len(newRs)-d]        #  циклический сдвиг
        autoCor[d] = 0
        for i in range(0, len(newRs)):
            if newRs[i] != shiftedRs[i]:
                autoCor[d] += 1
    print('Поліном: ' + polynomial)            
    print('Кількість неспівпадаючих бітів на періоді послідовності на d-ому зсуві: ')            
    for d in autoCor:
        print('d = ' + str(d) + ' : ' + str(autoCor[d]))

def distributionInThePeriod(polynomial, RecurrenceSequence, polDegree):   
    print('Поліном: ' + polynomial)    
    print('Розподіл k-грам на періоді: ')
    reg = '.'
    for k in range(1, polDegree+1):
        distribution = dict(Counter(findall(reg * k, RecurrenceSequence)))    # непересекающиеся
        sumValues = sum(distribution.values())
        for kgram in distribution:
            distribution[kgram] /= sumValues
        print(str(k)+'-грами: ')
        print(distribution)
        #for kgram in distribution:                                           # 2 часа работало и не досчитало
            #print(str(kgram) + ' : ' + str(distribution[kgram]))

def main():
    Pol1 = 'P1(X)= X21 + X17 + X16 + X14 + X13 + X12 + X6 + X4 + 1'
    Pol2 = 'P2(X)= X25 + X19 + X17 + X16 + X15 + X12 + X10 + X8 + X6 + X3 + 1'
    polDegree1 = 21                                                              # степень полинома
    polDegree2 = 25

    begin = time()
    
    impF1 = impulseFunction(polDegree1)        # импульсная функция
    impF2 = impulseFunction(polDegree2)

    recurrenceSequence1 = L1(impF1, pow(2,polDegree1)-1, polDegree1)  # нулевая последовательность не должна быть в регистре
    recurrenceSequence2 = L2(impF2, pow(2,polDegree2)-1, polDegree2)  # максимальний період

    period1 = period(recurrenceSequence1, impF1)                    # число после которого последовательность повторится
    period2 = period(recurrenceSequence2, impF2)  

    whatIsPolynomial(Pol1, period1, pow(2,polDegree1)-1)
    whatIsPolynomial(Pol2, period2, pow(2,polDegree2)-1)
                
    newRecurrenceSequence1 = L1(impF1, period1, polDegree1)
    newRecurrenceSequence2 = L2(impF2, period2, polDegree2)

    autoCorrelation(Pol1, newRecurrenceSequence1)
    autoCorrelation(Pol2, newRecurrenceSequence2)
                
    distributionInThePeriod(Pol1, newRecurrenceSequence1, polDegree1)
    distributionInThePeriod(Pol2, newRecurrenceSequence2, polDegree2)

    finish = time()

    print ('Час на розрахунки: ', finish-begin)

main()    










    





    
        
