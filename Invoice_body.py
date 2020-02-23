# -*- coding: UTF-8 -*-
'''created by Martin Kodada
Super cool invoice creator that can even do a QR payments.

Using  PyFPDF
(docs here https://pyfpdf.readthedocs.io/en/latest/Templates/index.html)

'{:.2f}'.format(int(price_per_item)) -> changes number to look like 0.00

'''



def Generate(qr,code,payload,buyer):
    from fpdf import Template
    import Supplier
    #test implementation
    print(buyer.name)

    elements = [
    {'name':'invoice','type': 'T', 'x1': 0.0, 'y1': 0.0, 'x2': 10.0, 'y2': 30.0, 'font': 'Arial', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 1, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 2, },    
    { 'name': 'company_logo', 'type': 'I', 'x1': 15.0, 'y1': 15.0, 'x2': 25.0, 'y2': 25.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 2, },
    { 'name': 'person', 'type': 'T', 'x1': 17.0, 'y1': 32.5, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'company_name', 'type': 'T', 'x1': 30.0, 'y1': 32.5, 'x2': 130.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
    { 'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial', 'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 2, },
    { 'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    { 'name': 'QR', 'type': 'I', 'x1': 30.0, 'y1': 30, 'x2': 60.0, 'y2': 60.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
    ]

#here we instantiate the template and define the HEADER
    f = Template(format="A4", elements=elements,
             title="Invoice")
    f.add_page()
#we FILL some of the fields of the template with the information we want
#note we access the elements treating the template instance as a "dict"
    f["invoice"] = f'Invoice #{code}'
    f["person"] = Supplier.name
    f["company_name"] = Supplier.company_name
    f["company_logo"] = Supplier.logo
    f["QR"] = qr
    

#and now we render the page
    f.render(f'./invoice{code}.pdf')

if __name__ == '__main__':
    Generate("img.png","000001",["",""])
