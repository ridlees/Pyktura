# -*- coding: UTF-8 -*-

def Taxtotal(total,tax,head):
    withoutTax =round(total/((100-tax)*0.01), 2)
    line = f"""<table>
<tr> <th>{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th></tr>
<tr> <th>{withoutTax}</th><th>{tax}%</th><th>{total}</th></tr>
</table>
"""
    return line
    
def Generate_table(payload,head,tax,hed):
    html_table = f"<table><tr> <th>{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th><th>{head[3]}</th> <th>{head[4]}</th></tr>"
    total = 0
    for item in payload:
        total = total + float(item[-1])
        html_table = html_table + f"<tr> <th>{item[0]}</th> <th>{item[1]}</th> <th>{item[2]}</th> <th>{item[3]}</th> <th>{item[4]}</th> </tr>"

    tax = Taxtotal(total, tax,hed)
    html_table = html_table +"</table>"
    return(html_table,tax)

def Generate_seller(seller,head):
    html_table = f"<table>"
    index = 0
    for data in seller:
        html_table = html_table + f"<tr> <th>{head[index]} </th> <th> {data}</th> </tr>"
        index += 1
    html_table = html_table +"</table>"
    return(html_table)

def Generate_buyer(buyer, head):
    html_table = f"<table>"
    index = 0
    for data in buyer:
        html_table = html_table + f"<tr> <th>{head[index]} </th> <th> {data}</th> </tr>"
        index += 1
    html_table = html_table +"</table>"
    return(html_table)

Lang_switch = {
    "cs":[["Popis","Cena","Množství","Měna","Celkem"],["Jméno", "Ulice","Město","PSČ","Stát","IČO","DIČ"],["Jméno","Ulice","Město","PSČ","Stát","IČO","DIČ","Webové stránky","Email","Tel.číslo"],["Celkem bez daně","DPH","Celkem"]],
    "en":[["Description","Price","Quantity","Currency","Total"],["Name", "Address","Town","Zip","Country","ICO","DIC"],["Name","Address","Town","Zip","Country","ICO","DIC","Website","Email","Phone"],["Without Tax","VAT","Total"]]
    }

def Generate(payload,language, buyer, seller):
    headers = Lang_switch.get(language)
    payload = [['fish', '120.00', 5, 'CZK', '600.00'], ['chips', '40.00', 1, 'CZK', '1.00']]
    items, tax = Generate_table(payload,headers[0],21,headers[3])
    buyer = Generate_buyer(["Jan Novák", "Terezie 43", "Ustí", "10800","ČR","32123123123","Z812Z38213"],headers[1])
    seller = Generate_seller(["Test","Veselá 22","Uhřívěnec","065 203","ČR","012931421031","012931421031","seznam.cz","hubert@seznam.cz","+420 000 000 000"],headers[2])
    html = f"""
    <!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>A simple, clean, and responsive HTML invoice template</title>
    
    <style>
    .invoice-box {
        max-width: 800px;
        margin: auto;
        padding: 30px;
        border: 1px solid #eee;
        box-shadow: 0 0 10px rgba(0, 0, 0, .15);
        font-size: 16px;
        line-height: 24px;
        font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
        color: #555;
    }
    
    .invoice-box table {
        width: 100%;
        line-height: inherit;
        text-align: left;
    }
    
    .invoice-box table td {
        padding: 5px;
        vertical-align: top;
    }
    
    .invoice-box table tr td:nth-child(2) {
        text-align: right;
    }
    
    .invoice-box table tr.top table td {
        padding-bottom: 20px;
    }
    
    .invoice-box table tr.top table td.title {
        font-size: 45px;
        line-height: 45px;
        color: #333;
    }
    
    .invoice-box table tr.information table td {
        padding-bottom: 40px;
    }
    
    .invoice-box table tr.heading td {
        background: #eee;
        border-bottom: 1px solid #ddd;
        font-weight: bold;
    }
    
    .invoice-box table tr.details td {
        padding-bottom: 20px;
    }
    
    .invoice-box table tr.item td{
        border-bottom: 1px solid #eee;
    }
    
    .invoice-box table tr.item.last td {
        border-bottom: none;
    }
    
    .invoice-box table tr.total td:nth-child(2) {
        border-top: 2px solid #eee;
        font-weight: bold;
    }
    
    @media only screen and (max-width: 600px) {
        .invoice-box table tr.top table td {
            width: 100%;
            display: block;
            text-align: center;
        }
        
        .invoice-box table tr.information table td {
            width: 100%;
            display: block;
            text-align: center;
        }
    }
    
    /** RTL **/
    .rtl {
        direction: rtl;
        font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
    }
    
    .rtl table {
        text-align: right;
    }
    
    .rtl table tr td:nth-child(2) {
        text-align: left;
    }
    </style>
</head>

<body>
    <div class="invoice-box">
    {seller}
    {buyer}
    {items}
    {tax}
</body>
</html>
"""
    with open('invoice.html',"w+") as f:
        f.write(html)

    
