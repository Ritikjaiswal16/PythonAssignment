def convert(number):
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
            '1000':'Thousand'}
    if number not in words:
        times=10**(len(number)-1)
        for i in range(len((number))):
            n=int(number[i])*times
            n=str(n)
            #print("Loop")
            if int(i)>1 and len(n)>2:
                #print(i)
                convert(i)
                convert(str(times))
            print(i)
            convert(i)
            #print(words[str(n)],end=' ')
            times=times//10
            
    else:
        print(words[number])
            
        
convert('571')
