from tkinter import *
from tkinter import ttk
w  = Tk()
ntb = ttk.Notebook(w)
ntb.pack()
w.geometry('950x430+100+300')
w.title('clavie')
w.configure(bg = 'black')
w.resizable(False , False)
#########################################
#this part for programming
#########################################
def clicka(  ):
    tx.insert( INSERT , 'a')
def clickb(   ):
    tx.insert( INSERT ,'b' )
def clickc( ):
    tx.insert( INSERT ,'c' )
def clickd(   ):
    tx.insert( INSERT ,'d' )
def clicke(   ):
    tx.insert( INSERT ,'e' )
def clickf(   ):
    tx.insert( INSERT , 'f')
def clickg(   ):
    tx.insert( INSERT ,'g' )
def clickh(   ):
    tx.insert( INSERT ,'h' )
def clicki(   ):
    tx.insert( INSERT , 'i')
def clickj(   ):
    tx.insert( INSERT , 'j' )
def clickk(  ):
    tx.insert( INSERT , 'k')
def clickl(   ):
    tx.insert( INSERT , 'l' )
def clickm(  ):
    tx.insert( INSERT ,'m' )
def clickn(  ):
    tx.insert( INSERT ,'n' )
def click(   ):
    tx.insert( INSERT , 'o')
def clicko(  ):
    tx.insert( INSERT ,'o' )
def clickp():
    tx.insert(INSERT , 'p')

def clickpk():
    tx.insert(INSERT , 'k')

def clickr():
    tx.insert(INSERT , 'r')

def clicks():
    tx.insert(INSERT , 's')

def clickt():
    tx.insert(INSERT , 't')

def clicku():
    tx.insert(INSERT , 'u')

def clickv():
    tx.insert(INSERT , 'v')

def clickw():
    tx.insert(INSERT , 'w')

def clickx():
    tx.insert(INSERT , 'x')

def clicky():
    tx.insert(INSERT , 'y')

def clickz():
    tx.insert(INSERT , 'z')

def clickà():
    tx.insert(INSERT , 'à')

def clické():
    tx.insert(INSERT , 'é')

def clickè():
    tx.insert(INSERT , 'è')

def clicksa():
    tx.insert (INSERT , ' ' )
    
def click1():
    tx.insert (INSERT , '1' )

def click2():
    tx.insert (INSERT , '2' )

def click3():
    tx.insert (INSERT , '3' )

def click4():
    tx.insert (INSERT , '4' )

def click5():
    tx.insert (INSERT , '5' )

def click6():
    tx.insert (INSERT , '6' )

def click7():
    tx.insert (INSERT , '7' )

def click8():
    tx.insert (INSERT , '8' )

def click9():
    tx.insert (INSERT , '9' )

def click0():
    tx.insert (INSERT , '0' )

def clickplu():
    tx.insert (INSERT , '+' )

def clickmoi():
    tx.insert (INSERT , '-' )


def clicks1():
    tx.insert (INSERT , '(' )

def clicks2():
    tx.insert (INSERT , ')' )

def clicks3():
    tx.insert (INSERT , '#' )

def clicks4():
    tx.insert (INSERT , "'" )

def clicks5():
    tx.insert (INSERT , '!' )

def clicks6():
    tx.insert (INSERT , '?' )

def clicks7():
    tx.insert (INSERT , ',' )

def clicks8():
    tx.insert (INSERT , ';' )

def clicks9():
    tx.insert (INSERT , '%' )


class bu:   
    def but(self , a , b , var  , cmd):
        bt = Button(fm1, text = var ,command = cmd,
                    bd = 5 , relief = 'groove' , width = 5,
                    bg = 'grey' )
        bt.place(x = a , y  = b )
    
    
    

        

#########################################
#this part for desighn 
#########################################


# tx.insert( INSERT ,'hakim')
fm1 = Frame(ntb , width = 950 , height = 430 ,bg = 'black')
fm1.place( x =122 , y = 544)
ntb.add(fm1 , text = 'français')

fm2 = Frame(ntb ,bg = 'black')
ntb.add (fm2 , text = 'arabe')

tx = Text (fm1 ,width = 113  , height = 10 , wrap = 'word'  )
tx.place( x = 20 , y = 20  )

b1 = bu()
b1.but( 30 , 200 , 'a' , clicka )

b2 = bu()
b2.but( 90 , 200 , 'b' , clickb )

b3 = bu()
b3.but( 150 ,200 , 'c', clickc )

b4 = bu()
b4.but(210 , 200 , 'd' , clickd)

b5 = bu()
b5.but(270 ,200 , 'e' , clicke)

b6 = bu()
b6.but(330 ,200 , 'f' , clickf )

b6 = bu()
b6.but(390 ,200 , 'g' , clickg )

b6 = bu()
b6.but(450 ,200 , 'h' , clickh )

b6 = bu()
b6.but(510 ,200 , 'i' , clicki )

b6 = bu()
b6.but(570 ,200 , 'j' , clickj )

b6 = bu()
b6.but(630 ,200 , 'k' , clickk )

b6 = bu()
b6.but(690 ,200 , 'l' , clickl )

b6 = bu()
b6.but(750 ,200 , 'm' , clickm )

b6 = bu()
b6.but(810 ,200 , 'n' , clickn )

b6 = bu()
b6.but(870 ,200 , 'o' , clicko )

b6 = bu()
b6.but(60 ,240 , 'p' , clickp )

b6 = bu()
b6.but(120 ,240 , 'k' , clickk )

b6 = bu()
b6.but(180 ,240 , 'r' , clickr )

b6 = bu()
b6.but(240 ,240 , 's' , clicks )

b6 = bu()
b6.but(300 ,240 , 't' , clickt )

b6 = bu()
b6.but(360 ,240 , 'u' , clicku )

b6 = bu()
b6.but(420 ,240 , 'v' , clickv )

b6 = bu()
b6.but(480 ,240 , 'w' , clickw )

b6 = bu()
b6.but(540 ,240 , 'x' , clickx )

b6 = bu()
b6.but(600 ,240 , 'y' , clicky )

b6 = bu()
b6.but(660 ,240 , 'z' , clickz )

b6 = bu()
b6.but(720 ,240 , 'à' , clickà )

b6 = bu()
b6.but(780 ,240 , 'é' , clické )

b6 = bu()
b6.but(840 ,240 , 'è' , clickè )


btsa = Button(fm1, text = 'space ' , command = clicksa , width = 100 , bg = 'grey' ) 
btsa.place(x = 100 , y = 280 )

b6 = bu()
b6.but(130 ,320 , '1' , click1 )

b6 = bu()
b6.but(190 ,320 , '2' , click2 )

b6 = bu()
b6.but(250 ,320 , '3' , click3 )

b6 = bu()
b6.but(310 ,320 , '4' , click4 )

b6 = bu()
b6.but(370 ,320 , '5' , click5 )

b6 = bu()
b6.but(430 ,320 , '6' , click6 )

b6 = bu()
b6.but(490 ,320 , '7' , click7 )

b6 = bu()
b6.but(550 ,320 , '8' , click8 )

b6 = bu()
b6.but(610 ,320 , '9' , click9 )

b6 = bu()
b6.but(670 ,320 , '0' , click0 )

b6 = bu()
b6.but(730 ,320 , '+' , clickplu )

b6 = bu()
b6.but(700 ,360 , '-' , clickmoi )

b6 = bu()
b6.but(160 ,360 , '(' , clicks1 )

b6 = bu()
b6.but(220 ,360 , ')' , clicks2 )

b6 = bu()
b6.but(280 ,360 , '#' , clicks3 )

b6 = bu()
b6.but(340 ,360 , "'" , clicks4 )

b6 = bu()
b6.but(400 ,360 , '!' , clicks5 )

b6 = bu()
b6.but(460 ,360 , '?' , clicks6 )

b6 = bu()
b6.but(520 ,360 , ',' , clicks7 )

b6 = bu()
b6.but(580 ,360 , ';' , clicks8 )

b6 = bu()
b6.but(640 ,360 , '%' , clicks9 )

###########################################
#this part for arabe
###########################################
# this part for disaghn 
tx2 = Text(fm2 , width = 113 , height = 10 ,wrap = 'word' ,
            )
tx2.place( x = 20 , y = 20 )

###########################################

#this part for prgramming 
def clicka(  ):
    tx2.insert( INSERT , 'ض')
def clickb(   ):
    tx2.insert( INSERT ,'ص' )
def clickc( ):
    tx2.insert( INSERT ,'ش' )
def clickd(   ):
    tx2.insert( INSERT ,'س' )
def clicke(   ):
    tx2.insert( INSERT ,'ز' )
def clickf(   ):
    tx2.insert( INSERT , 'ر')
def clickg(   ):
    tx2.insert( INSERT ,'ذ' )
def clickh(   ):
    tx2.insert( INSERT ,'د' )
def clicki(   ):
    tx2.insert( INSERT , 'خ')
def clickj(   ):
    tx2.insert( INSERT , 'ح' )
def clickk(  ):
    tx2.insert( INSERT , 'ج')
def clickl(   ):
    tx2.insert( INSERT , 'ث' )
def clickm(  ):
    tx2.insert( INSERT ,'ت' )
def clickn(  ):
    tx2.insert( INSERT ,'ب' )
def clicko(  ):
    tx2.insert( INSERT ,'ا' )
def clickp():
    tx2.insert(INSERT , 'ء')

def clickpk():
    tx2.insert(INSERT , 'و')

def clickr():
    tx2.insert(INSERT , 'و')

def clicks():
    tx2.insert(INSERT , 'ه')

def clickt():
    tx2.insert(INSERT , 'ن')

def clicku():
    tx2.insert(INSERT , 'م')

def clickv():
    tx2.insert(INSERT , 'ل')

def clickw():
    tx2.insert(INSERT , 'ك')

def clickx():
    tx2.insert(INSERT , 'ق')

def clicky():
    tx2.insert(INSERT , 'ف')

def clickz():
    tx2.insert(INSERT , 'غ')

def clickà():
    tx2.insert(INSERT , 'ع')

def clickk1():
    tx2.insert(INSERT , 'ي')

def clické():
    tx2.insert(INSERT , 'ظ')

def clickè():
    tx2.insert(INSERT , 'ط')

def clicksa():
    tx2.insert (INSERT , ' ' )
    
def click1():
    tx2.insert (INSERT , '1' )

def click2():
    tx2.insert (INSERT , '2' )

def click3():
    tx2.insert (INSERT , '3' )

def click4():
    tx2.insert (INSERT , '4' )

def click5():
    tx2.insert (INSERT , '5' )

def click6():
    tx2.insert (INSERT , '6' )

def click7():
    tx2.insert (INSERT , '7' )

def click8():
    tx2.insert (INSERT , '8' )

def click9():
    tx2.insert (INSERT , '9' )

def click0():
    tx2.insert (INSERT , '0' )

def clickplu():
    tx2.insert (INSERT , '+' )

def clickmoi():
    tx2.insert (INSERT , '-' )


def clicks1():
    tx2.insert (INSERT , '(' )

def clicks2():
    tx2.insert (INSERT , ')' )

def clicks3():
    tx2.insert (INSERT , '#' )

def clicks4():
    tx2.insert (INSERT , "'" )

def clicks5():
    tx2.insert (INSERT , '!' )

def clicks6():
    tx2.insert (INSERT , '?' )

def clicks7():
    tx2.insert (INSERT , ',' )

def clicks8():
    tx2.insert (INSERT , ';' )

def clicks9():
    tx2.insert (INSERT , '%' )



class bu:   
    def but(self , a , b , var  , cmd):
        bt = Button(fm2, text = var ,command = cmd,
                    bd = 5 , relief = 'groove' , width = 5,
                    bg = 'grey' )
        bt.place(x = a , y  = b )





b1 = bu()
b1.but( 30 , 200 , 'ض' , clicka )

b2 = bu()
b2.but( 90 , 200 , 'ص' , clickb )

b3 = bu()
b3.but( 150 ,200 , 'ش', clickc )

b4 = bu()
b4.but(210 , 200 , 'س' , clickd)

b5 = bu()
b5.but(270 ,200 , 'ز' , clicke)

b6 = bu()
b6.but(330 ,200 , 'ر' , clickf )

b6 = bu()
b6.but(390 ,200 , 'ذ' , clickg )

b6 = bu()
b6.but(450 ,200 , 'د' , clickh )

b6 = bu()
b6.but(510 ,200 , 'خ' , clicki )

b6 = bu()
b6.but(570 ,200 , 'ح' , clickj )

b6 = bu()
b6.but(630 ,200 , 'ج' , clickk )

b6 = bu()
b6.but(690 ,200 , 'ث' , clickl )

b6 = bu()
b6.but(750 ,200 , 'ت' , clickm )

b6 = bu()
b6.but(810 ,200 , 'ب' , clickn )

b6 = bu()
b6.but(870 ,200 , 'ا' , clicko )

b6 = bu()
b6.but(60 ,240 , 'ء' , clickp )

b6 = bu()
b6.but(120 ,240 , 'ي' , clickk1 )

b6 = bu()
b6.but(180 ,240 , 'و' , clickr )

b6 = bu()
b6.but(240 ,240 , 'ه' , clicks )

b6 = bu()
b6.but(300 ,240 , 'ن' , clickt )

b6 = bu()
b6.but(360 ,240 , 'م' , clicku )

b6 = bu()
b6.but(420 ,240 , 'ل' , clickv )

b6 = bu()
b6.but(480 ,240 , 'ك' , clickw )

b6 = bu()
b6.but(540 ,240 , 'ق' , clickx )

b6 = bu()
b6.but(600 ,240 , 'ف' , clicky )

b6 = bu()
b6.but(660 ,240 , 'غ' , clickz )

b6 = bu()
b6.but(720 ,240 , 'ع' , clickà )

b6 = bu()
b6.but(780 ,240 , 'ظ' , clické)  
b6 = bu()
b6.but(840 ,240 , 'ط' , clickè )


btsa = Button(fm2, text = 'مسافة ' , command = clicksa , width = 100 , bg = 'grey' ) 
btsa.place(x = 100 , y = 280 )

b6 = bu()
b6.but(130 ,320 , '1' , click1 )

b6 = bu()
b6.but(190 ,320 , '2' , click2 )

b6 = bu()
b6.but(250 ,320 , '3' , click3 )

b6 = bu()
b6.but(310 ,320 , '4' , click4 )

b6 = bu()
b6.but(370 ,320 , '5' , click5 )

b6 = bu()
b6.but(430 ,320 , '6' , click6 )

b6 = bu()
b6.but(490 ,320 , '7' , click7 )

b6 = bu()
b6.but(550 ,320 , '8' , click8 )

b6 = bu()
b6.but(610 ,320 , '9' , click9 )

b6 = bu()
b6.but(670 ,320 , '0' , click0 )

b6 = bu()
b6.but(730 ,320 , '+' , clickplu )

b6 = bu()
b6.but(700 ,360 , '-' , clickmoi )

b6 = bu()
b6.but(160 ,360 , '(' , clicks1 )

b6 = bu()
b6.but(220 ,360 , ')' , clicks2 )

b6 = bu()
b6.but(280 ,360 , '#' , clicks3 )

b6 = bu()
b6.but(340 ,360 , "'" , clicks4 )

b6 = bu()
b6.but(400 ,360 , '!' , clicks5 )

b6 = bu()
b6.but(460 ,360 , '?' , clicks6 )

b6 = bu()
b6.but(520 ,360 , ',' , clicks7 )

b6 = bu()
b6.but(580 ,360 , ';' , clicks8 )

b6 = bu()
b6.but(640 ,360 , '%' , clicks9 )
