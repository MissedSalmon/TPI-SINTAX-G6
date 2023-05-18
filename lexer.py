import ply.lex as lex
import sys
import re
import codecs
import os


#definimos una lista con los tokens a utilizar
tokens=[
    'TEXTO',
    'NUMERO',
    'DOCTYPE',
    'AART', #Apertura - ARTICLE
    'CART', #Cierre - ARTICLE
    'ASECT', #SECTION
    'CSECT',
    'ASSECT', #simplesection
    'CSSECT',
    'AINFO', 
    'CINFO',
    'AABST',
    'CABST',
    'AADD',    
    'CADD',
    'ACOPY',
    'CCOPY',
    'ATIT',
    'CTIT',
    'ASPARA',
    'CSPARA',
    'AEMPH',
    'CEMPH',
    'ACOM',
    'CCOM',   
    'APARA',
    'CPARA',
    'AFNAME',
    'CFNAME',
    'ASNAME',
    'CSMANE',
    'ASTREET',
    'CSTREET',
    'ACITY',
    'CCITY',
    'ASTATE',
    'CSTATE',
    'APHONE',
    'CPHONE',
    'AEMAIL',
    'CEMAIL',
    'ADATE',
    'CDATE',
    'AYEAR',
    'CYEAR',
    'AHOLDER',
    'CHOLDER',
    'AMOBJ', #MEDIA OBJECT
    'CMOBJ',
    'AVOBJ', #VIDEO  OBJECT
    'CVOBJ',
    'VIDAT', #VIDEO DATA
    'VFORM', #VIDEO FORMATO
    'AIMOBJ', #IMAGEN OBJECT
    'CIMOBJ',
    'IMDATA', #IMAGEN DATA
    'IMFORM', #IMAGEN FORMAT
    'AILIST', #ITEMIZED LIST
    'CILIST',
    'ALITEM', #LIST ITEM
    'CLITEM',
    'AINTAB', #INFORMAL TABLE
    'CINTAB',
    'ATGROUP',
    'CTGROUP',
    'AHEAD',
    'CHEAD',
    'AFOOT',
    'CFOOT',
    'ABODY',
    'CBODY',
    'AROW',
    'CROW',
    'AENTRY',
    'CENTRY',
    'ALINK',
    'CLINK',
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
def t_AART(t):
    r'<article>'
    print("<article>")
    return t 

#Definicion de la expresion regular de cerrar articulo
def t_CART(t):
    r'</article>'
    print("</article>")
    return t 

#Definicion de la expresion regular de Abrir section
def t_ASECT(t):
    r'<section>'
    print("<section>")
    return t 

#Definicion de la expresion regular de section section
def t_CSECT(t):
    r'</section>'
    print("</section>")
    return t 

#Definicion de la expresion regular de Abrir simlpesection
def t_ASSECT(t):
    r'<simplesect>'
    print("<simplesect>")
    return t 

#Definicion de la expresion regular de Abrir simplesection
def t_ASECT(t):
    r'</simplesec>'
    print("</simplesect>")
    return t 



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

