# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
from numpy.fft import fft
from scipy.signal import savgol_filter



#Values of the Signal 
M = np.loadtxt('data_1.txt')
N=np.loadtxt('data_2.txt')



################################## Fonction Utilisée ##########################


def Norm_Value(Data):
    #Normalize the value of The Datas 
     absValues = [abs(number) for number in Data]
     max_value = max(absValues)
     print('max value of the Datas:',max_value)
     Value_norm=Data/max_value
     
     return Value_norm



def Find_Fc(Data_Norm,Fe,Fc):
    #Fréquence de Nyquist 
    f_nyq = Fe / 2.  # Hz
   
   #Calcul Coeff Butter
    b, a = signal.butter(5, Fc/f_nyq, 'low', analog=False)
    s_but = signal.filtfilt(b, a, Data_Norm)
    
    #Re calcul Valeur Max
    absValues1 = [abs(number) for number in s_but]
    max_value1 = max(absValues1)
    print('max value is : ', max_value1)
    print('fc equals to :' , Fc)
    #recursivité avec un pas de 20Hz
    if (0.700<max_value1<0.705): 
        Fc_out=Fc
        return Fc_out
    else :
       if(max_value1>0.707):
          return Find_Fc(Data_Norm,Fe,(Fc-100))  
       else:
          return Find_Fc(Data_Norm,Fe,(Fc+100))



def Butter_filter(Data,Fe,Fc1):
    
    f_nyq = Fe / 2.  # Hz    

    #Pass the Datas in a ButterWorth of 16 around the Fc found for the highest peak of Power  
    a,b= signal.butter(8, Fc1/f_nyq, 'low', analog=False)
    s_but = signal.filtfilt(a, b, Norm_Value(Data))
    s_but1 = signal.filtfilt(a, b, s_but)
    return s_but1


def Print_courbe(Data,Abs,number):
    # Affichage du signal 
    plt.figure()
    plt.plot(Abs,Data, color='red', label='Signal')
    plt.grid(True, which='both')
    plt.legend(loc="best")
    title='Signal',number
    plt.title(title)
 
#def FFT_signal(Data)
################################## Exploitation ###############################


#Value of the Time 
A=M[:,0]
#C=N[:,0]

#Value of the Field 
B=M[:,1]
#D=N[:,1]

# Fréquence d'échantillonnage
Fe =5000000   # Hz

Print_courbe(B,A,1)
##Print_courbe(D,C,2)
#
#
#Value_norm1=Norm_Value(B)
##Value_norm2=Norm_Value(D)
#
#
#Fc1=Find_Fc(Value_norm1,Fe,40000)
#print('Fc cutoff1 is :',Fc1)
#Values1_Filter=Butter_filter(B,Fe,Fc1)
#Print_courbe(Values1_Filter,A,3)
#
##Fc2=Find_Fc(Value_norm2,Fe,12000)
##print('Fc cutoff2 is :',9000)
##Values2_Filter=Butter_filter(D,Fe,15000)
##Print_courbe(Values2_Filter,C,4)
#
#    

fft_signal1=fft(B)
Print_courbe(fft_signal1,A,1)







