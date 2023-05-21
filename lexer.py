import ply.lex as lex
import sys
import re
import codecs
import os


#definimos una lista con los tokens a utilizar
tokens=[
    'TEXTO', #Texto alfanumerico
    'NUMERO',
    'DOCTYPE',
    'OpART', #Apertura - ARTICLE (Open)
    'ClART', #Cierre - ARTICLE  (Close)
    'OpSECT', #SECTION
    'ClSECT',
    'OpSSECT', #simplesection
    'ClSSECT',
    'OpINFO', 
    'ClINFO',
    'OpABST',
    'ClABST',
    'OpADD',    
    'ClADD',
    'OpAUTHOR',
    'ClAUTHOR',
    'OpCOPY',
    'ClCOPY',
    'OpTIT',
    'ClTIT',
    'OpSPARA',
    'ClSPARA',
    'OpEMPH',
    'ClEMPH',
    'OpCOM',
    'ClCOM',   
    'OpPARA',
    'ClPARA',
    'OpFNAME',
    'ClFNAME',
    'OpSNAME',
    'ClSMANE',
    'OpSTREET',
    'ClSTREET',
    'OpCITY',
    'ClCITY',
    'OpSTATE',
    'ClSTATE',
    'OpPHONE',
    'ClPHONE',
    'OpEMAIL',
    'ClEMAIL',
    'OpDATE',
    'ClDATE',
    'OpYEAR',
    'ClYEAR',
    'OpHOLDER',
    'ClHOLDER',
    'OpMOBJ', #MEDIA OBJECT
    'ClMOBJ',
    'OpVOBJ', #VIDEO  OBJECT
    'ClVOBJ',
    'VIDAT', #VIDEO DATA
    'VFORM', #VIDEO FORMATO
    'OpIMOBJ', #IMAGEN OBJECT
    'ClIMOBJ',
    'IMDATA', #IMAGEN DATA
    'IMFORM', #IMAGEN FORMAT
    'OpILIST', #ITEMIZED LIST
    'ClILIST',
    'OpLITEM', #LIST ITEM
    'ClLITEM',
    'OpINTAB', #INFORMAL TABLE
    'ClINTAB',
    'OpTGROUP',
    'ClTGROUP',
    'OpHEAD',
    'ClHEAD',
    'OpFOOT',
    'ClFOOT',
    'OpBODY',
    'ClBODY',
    'OpROW',
    'ClROW',
    'OpENTRY',
    'ClENTRY',
    'OpLINK',
    'ClLINK',
]

#tokens especiales
def t_ignore_tab(t):
    r'\t'

t_ignore_blank= '\s'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Definicion de la expresion regular del tag del dockbook
def t_DOCTYPE(t):
    r'<!DOCTYPE article>'
    print("DOCKBOOK")
    return t 

#Definicion de la expresion regular de Abrir articulo
def t_OpART(t):
    r'<article>'
    print("<article>")
    return t 

#Definicion de la expresion regular de Cerrar articulo
def t_ClART(t):
    r'</article>'
    print("</article>")
    return t 

#Definicion de la expresion regular de Abrir section
def t_OpSECT(t):
    r'<section>'
    print("<section>")
    return t 

#Definicion de la expresion regular de Cerrar section
def t_ClSECT(t):
    r'</section>'
    print("</section>")
    return t 

#Definicion de la expresion regular de Abrir simlpesection
def t_OpSSECT(t):
    r'<simplesect>'
    print("<simplesect>")
    return t 

#Definicion de la expresion regular de Abrir simplesection
def t_ClSSECT(t):
    r'</simplesec>'
    print("</simplesect>")
    return t 

#Definicion de la expresion regular de Abrir info
def t_OpINFO(t):
    r'<info>'
    print("<info>")
    return t 

#Definicion de la expresion regular de Cerrar info
def t_ClINFO(t):
    r'</info>'
    print("</info>")
    return t 

#Definicion de la expresion regular de Abrir abstract
def t_OpABST(t):
    r'<abstract>'
    print("<abstract>")
    return t 

#Definicion de la expresion regular de Cerrar abstract
def t_ClABST(t):
    r'</abstract>'
    print("</abstract>")
    return t 

#Definicion de la expresion regular de Abrir address
def t_OpADD(t):
    r'<address>'
    print("<address>")
    return t 

#Definicion de la expresion regular de Cerrar address
def t_ClADD(t):
    r'</address>'
    print("</address>")
    return t 

#Definicion de la expresion regular de Abrir author
def t_OpAUTHOR(t):
    r'<author>'
    print("<author>")
    return t 

#Definicion de la expresion regular de Cerrar author
def t_ClAUTHOR(t):
    r'</author>'
    print("</author>")
    return t 

#Definicion de la expresion regular de Abrir copyright
def t_OpCOPY(t):
    r'<copyright>'
    print("<copyright>")
    return t 

#Definicion de la expresion regular de Cerrar copyright
def t_ClCOPY(t):
    r'</copyright>'
    print("</copyright>")
    return t

#Definicion de la expresion regular de Abrir title
def t_OpTIT(t):
    r'<title>'
    print("<title>")
    return t 

#Definicion de la expresion regular de Cerrar title
def t_ClTIT(t):
    r'</title>'
    print("</title>")
    return t

#Definicion de la expresion regular de Abrir simpara
def t_OpSPARA(t):
    r'<simpara>'
    print("<simpara>")
    return t 

#Definicion de la expresion regular de Cerrar simpara
def t_ClSPARA(t):
    r'</simpara>'
    print("</simpara>")
    return t

#Definicion de la expresion regular de Abrir emphasis
def t_OpEMPH(t):
    r'<emphasis>'
    print("<emphasis>")
    return t 

#Definicion de la expresion regular de Cerrar emphasis
def t_ClEMPH(t):
    r'</emphasis>'
    print("</emphasis>")
    return t

#Definicion de la expresion regular de Abrir comment
def t_OpCOM(t):
    r'<comment>'
    print("<comment>")
    return t 

#Definicion de la expresion regular de Cerrar comment
def t_ClCOM(t):
    r'</comment>'
    print("</comment>")
    return t

#Definicion de la expresion regular de Abrir para
def t_OpPARA(t):
    r'<para>'
    print("<para>")
    return t 

#Definicion de la expresion regular de Cerrar para
def t_ClPARA(t):
    r'</para>'
    print("</para>")
    return t

#Definicion de la expresion regular de Abrir firstname
def t_OpFNAME(t):
    r'<firstname>'
    print("<firstname>")
    return t 

#Definicion de la expresion regular de Cerrar firstname
def t_ClFNAME(t):
    r'</firstname>'
    print("</firstname>")
    return t

#Definicion de la expresion regular de Abrir surname
def t_OpSNAME(t):
    r'<surname>'
    print("<surname>")
    return t 

#Definicion de la expresion regular de Cerrar surname
def t_ClSMANE(t):
    r'</surname>'
    print("</surname>")
    return t

#Definicion de la expresion regular de Abrir street
def t_OpSTREET(t):
    r'<street>'
    print("<street>")
    return t 

#Definicion de la expresion regular de Cerrar street
def t_ClSTREET(t):
    r'</street>'
    print("</street>")
    return t

#Definicion de la expresion regular de Abrir city
def t_OpCITY(t):
    r'<city>'
    print("<city>")
    return t 

#Definicion de la expresion regular de Cerrar city
def t_ClCITY(t):
    r'</city>'
    print("</city>")
    return t

#Definicion de la expresion regular de Abrir state
def t_OpSTATE(t):
    r'<state>'
    print("<state>")
    return t 

#Definicion de la expresion regular de Cerrar state
def t_ClSTATE(t):
    r'</state>'
    print("</state>")
    return t

#Definicion de la expresion regular de Abrir phone
def t_OpPHONE(t):
    r'<phone>'
    print("<phone>")
    return t 

#Definicion de la expresion regular de Cerrar phone
def t_ClPHONE(t):
    r'</phone>'
    print("</phone>")
    return t

#Definicion de la expresion regular de Abrir email
def t_OpEMAIL(t):
    r'<email>'
    print("<email>")
    return t 

#Definicion de la expresion regular de Cerrar email
def t_ClEMAIL(t):
    r'</email>'
    print("</email>")
    return t

#Definicion de la expresion regular de Abrir date
def t_OpDATE(t):
    r'<date>'
    print("<date>")
    return t 

#Definicion de la expresion regular de Cerrar date
def t_ClDATE(t):
    r'</date>'
    print("</date>")
    return t

#Definicion de la expresion regular de Abrir year
def t_OpYEAR(t):
    r'<year>'
    print("<year>")
    return t 

#Definicion de la expresion regular de Cerrar year
def t_ClYEAR(t):
    r'</year>'
    print("</year>")
    return t

#Definicion de la expresion regular de Abrir holder
def t_OpHOLDER(t):
    r'<holder>'
    print("<holder>")
    return t 

#Definicion de la expresion regular de Cerrar holder
def t_ClHOLDER(t):
    r'</holder>'
    print("</holder>")
    return t

#Definicion de la expresion regular de Abrir mediaobject
def t_OpMOBJ(t):
    r'<mediaobject>'
    print("<mediaobject>")
    return t 

#Definicion de la expresion regular de Cerrar mediaobject
def t_ClMOBJ(t):
    r'</mediaobject>'
    print("</mediaobject>")
    return t

#Definicion de la expresion regular de Abrir videoobject
def t_OpVOBJ(t):
    r'<videoobject>'
    print("<videoobject>")
    return t 

#Definicion de la expresion regular de Cerrar videoobject
def t_ClVOBJ(t):
    r'</videoobject>'
    print("</videoobject>")
    return t

#Definición de 'VIDAT', 'VFORM' PENDIENTE

#Definicion de la expresion regular de Abrir imageobject
def t_OpIMOBJ(t):
    r'<imageobject>'
    print("<imageobject>")
    return t 

#Definicion de la expresion regular de Cerrar imageobject
def t_ClIMOBJ(t):
    r'</imageobject>'
    print("</imageobject>")
    return t

#Definición de 'IMDATA', 'IMFORM' PENDIENTE

#Definicion de la expresion regular de Abrir itemizedlist
def t_OpILIST(t):
    r'<itemizedlist>'
    print("<itemizedlist>")
    return t 

#Definicion de la expresion regular de Cerrar itemizedlist
def t_ClILIST(t):
    r'</itemizedlist>'
    print("</itemizedlist>")
    return t

#Definicion de la expresion regular de Abrir listitem
def t_OpLITEM(t):
    r'<listitem>'
    print("<listitem>")
    return t 

#Definicion de la expresion regular de Cerrar listitem
def t_ClLITEM(t):
    r'</listitem>'
    print("</listitem>")
    return t

#Definicion de la expresion regular de Abrir informaltable
def t_OpINTAB(t):
    r'<informaltable>'
    print("<informaltable>")
    return t 

#Definicion de la expresion regular de Cerrar informaltable
def t_ClINTAB(t):
    r'</informaltable>'
    print("</informaltable>")
    return t

#Definicion de la expresion regular de Abrir tgroup
def t_OpTGROUP(t):
    r'<tgroup>'
    print("<tgroup>")
    return t 

#Definicion de la expresion regular de Cerrar tgroup
def t_ClGROUP(t):
    r'</tgroup>'
    print("</tgroup>")
    return t

#Definicion de la expresion regular de Abrir thead
def t_OpHEAD(t):
    r'<thead>'
    print("<thead>")
    return t 

#Definicion de la expresion regular de Cerrar thead
def t_ClHEAD(t):
    r'</thead>'
    print("</thead>")
    return t

#Definicion de la expresion regular de Abrir tfoot
def t_OpFOOT(t):
    r'<tfoot>'
    print("<tfoot>")
    return t 

#Definicion de la expresion regular de Cerrar tfoot
def t_ClFOOT(t):
    r'</tfoot>'
    print("</tfoot>")
    return t

#Definicion de la expresion regular de Abrir tbody
def t_OpBODY(t):
    r'<tbody>'
    print("<tbody>")
    return t 

#Definicion de la expresion regular de Cerrar tbody
def t_ClBODY(t):
    r'</tbody>'
    print("</tbody>")
    return t

#Definicion de la expresion regular de Abrir row
def t_OpROW(t):
    r'<row>'
    print("<row>")
    return t 

#Definicion de la expresion regular de Cerrar row
def t_ClROW(t):
    r'</row>'
    print("</row>")
    return t

#Definicion de la expresion regular de Abrir entry
def t_OpENTRY(t):
    r'<entry>'
    print("<entry>")
    return t 

#Definicion de la expresion regular de Cerrar entry
def t_ClENTRY(t):
    r'</entry>'
    print("</entry>")
    return t

#Definicion de la expresion regular de link PENDIENTE


#Definicion de la expresion regular de un texto
def t_TEXTO(t):
    r'([0-9]*[a-zA-Z ,.;#:&?+/()_-][0-9]*[a-zA-Z ,.;#:&?+/()_-]*[0-9]*)'
    if t.value.upper() in tokens:
        t.value = t.value.upper()
        t.type= t.value
    print("TEXTO")
    return t

#Definicion de la expresion regular de un numero
def t_NUMERO(t):
    r'[0-9][0-9]*'
    print("NUMERO")
    return t

def t_error(t):
    print("Error lexico en la linea", str(t.lineno))
    t.lexer.skip(1)


print ("Hola este es el analizador Lexico")
print ("Ingrese manualmente el codigo")
cad = input('')


analizador = lex.lex()

analizador.input(cad)

print("\nLista de tokens\n")

while True:
 	tok = analizador.token()
 	if not tok : break
print(tok)