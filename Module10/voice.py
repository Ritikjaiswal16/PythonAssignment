from winsound import *
def convert(num):
    words={ '0':'Zero',
            '1':'One',
            '2':'Two',
            '3':'Three',
            '4':'Four',
            '5':'Five',
            '6':'Six',
            '7':'Seven',
            '8':'Eight',
            '9':'Nine',
            '10':'Ten',
            '11':'Eleven',
            '12':'Twelve',
            '13':'Thirteen',
            '14':'Fourteen',
            '15':'Fifteen',
            '16':'Sixteen',
            '17':'Seventeen',
            '18':'Eighteen',
            '19':'Nineteen',
            '20':'Twenty',
            '30':'Thirty',
            '40':'Fourty',
            '50':'Fifty',
            '60':'Sixty',
            '70':'Seventy',
            '80':'Eighty',
            '90':'Ninty',
            '100':'Hundred',
            '1000':'Thousand',
            '10000':'Lakh'}
    if num not in words:
        
        
        times=10**(len(num)-1)
        s=int(num[0])*times
        if str(s) not in words:
            #print(s)
            convert(num[0])
            convert(str(times))
        else:
            convert(str(s))
        convert(num[1:])
      
            
    else:
        print(words[num],end=' ')
        PlaySound(num,SND_FILENAME)
            
a=input('ENTER A NUMBER -: ')        
convert(a)
