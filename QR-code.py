# -*- coding: UTF-8 -*-
'''created by Martin Kodada
An easy python Script to keep my own invoices in check for future projects.
One day, I will use it for all my invoices.

Thanks to   Aleš Dynda, info@qr-platba.cz
            Petr Dvořák, info@qr-platba.cz
for https://qr-platba.cz/ API I use. It is seriously really good and I like it a lot
'''

import requests  #to get HTML
import shutil


def CreateQR(accountNumber,bankCode,amount,currency,message):

    URL = f"http://api.paylibo.com/paylibo/generator/czech/image?accountNumber={accountNumber}&bankCode={bankCode}&amount={amount}&currency={currency}&vs=333&message={message}"
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0', "Accept":"application/png"}
    response = requests.get(URL,headers=headers, stream=True)
    print(response)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    
if __name__ == '__main__':
    CreateQR("123457","5500","10.00","CZK","1")
