# -*- coding: UTF-8 -*-
'''created by Martin Kodada
An easy python command line script to keep my own invoices in check for future projects.

'''

import QR_code 
import Invoice_body
import Supplier

def Eur_CZK(EUR):
    return (round(int(EUR)/Supplier.course))

class Invoice_creator:

    #init should include info about the other "guy"
    
    def __init__(self,code,currency,theme):
        self.code = code
        self.currency = currency
        self.payload = []
        self.total = 0
        self.items= 0
        self.theme = theme

    #sets the type of invoice (hours for work and items for item selling)
        
    def chang_theme(self,theme):
        self.theme = theme
        
    def change_lang(self,language):
        self.currency = language
        
    #Function to add new items to invoice
    def add(self, item_description, price_per_item, quantity, currency):
        price_total = int(quantity) * float(price_per_item)
        if currency == "EUR":
            price_total  = Eur_CZK(price_total)
            currency = "CZK"
        self.total = self.total + price_total
        self.payload.append([item_description,'{:.2f}'.format(float(price_per_item)),quantity,currency,'{:.2f}'.format(float(price_total))])
        self.items = self.items + 1
        
     # to check the current status of invoice
    def status(self):
        print(f'The Invoice {self.code} contains: \n Total of {self.items} items in price of {self.total} \n The current payload is: {self.payload}')
        
    # to delete line (on position arg) from invoice
    def delete(self, arg):
        deleted = self.payload.pop(int(arg - 1))
        print(f'The following line {deleted} was deleted')
        self.items = self.items - 1
        self.total = self.total - float(deleted[-1])
        
    # generates pdf of the invoice
    def create(self):
        message = input("message for the payer \n")
        QR_code.CreateQR(Supplier.bank, Supplier.bank_code,self.total,self.currency,message)
        Invoice_body.Generate("img.png",self.code,self.payload)
        
def help():
    print() #TODO Finish help()

def credits():
    print("Pyktura was created by Ridlees(https://github.com/ridlees)\nThanks to Aleš Dynda(info@qr-platba.cz) and Petr Dvořák(info@qr-platba.cz) for the QR code API\nThanks to  Christopher Jones(cjones@insub.org),Peter Waller(p@pwaller.net) and Stefano Rivera(stefano@rivera.za.net) for pyfiglet")

def licence():
    print("Pyktura is under MIT licence (see https://opensource.org/licenses/MIT OR https://wiki.pirati.cz/kci/mit_licence if you are czech)")
    
def main():
    import pyfiglet
    ascii_banner = pyfiglet.figlet_format("Pyktura")
    print(ascii_banner)
    print("Pyktura is simple command line tool for quick invoices created by Ridlees.\nSupports both CZK and EUR as currencies.\nIf you need help, call help().\nType credits() to see credits, or licence() for licence.\nOtherwise, may the script be with you.")


if __name__ == '__main__':
    main()
    invoice = Invoice_creator("00001","CZK","hours")
    invoice.add("oral",120,5, "CZK")
    invoice.add("anál", 40, 1, "EUR")
