from openpyxl import load_workbook as lwb
import pandas as pd
import streamlit as st

ref = []

latest_file = "Available stock.xlsx"
st.write('MODULYSS STOCK'+'\n\n')
st.write('The file loaded is '+latest_file+'\n')



modref = lwb('ModRef.xlsx').active
stockfile = lwb(latest_file).active

stocklist = []

for a,b in modref:
    ref.append([a.value, b.value.split('*')])

for a,b,c,d,e,f,g,h,i,j,k,*l in stockfile:
    for x,y in ref:
        if b.value == x:
            stocklist.append((y[0],y[1],h.value,str(k.value)))

sorted_list = sorted(stocklist)
df = pd.DataFrame(data=sorted_list, columns=('RANGE','COLOUR','QTY(m²)','BATCH'))

range = list(set(df['RANGE']))
range.sort()
range.insert(0, 'ALL')

option = st.selectbox(
    'RANGE SELECTOR',
     range)

if option == 'ALL':
    df
else:
    df[df['RANGE']==option]
