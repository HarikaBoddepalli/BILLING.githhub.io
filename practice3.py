from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality Part

def clear():

     concealersEntry.delete(0,END)
     facecreamsEntry.delete(0,END)
     mascarasEntry.delete(0,END)
     hairspraysEntry.delete(0,END)
     lipglossesEntry.delete(0,END)
     bathsoapsEntry.delete(0,END)
     mirrorsEntry.delete(0,END)
     combsEntry.delete(0,END)
     perfumesEntry.delete(0,END)

     meatEntry.delete(0,END)
     grainsEntry.delete(0,END)
     oilEntry.delete(0,END)
     dairyEntry.delete(0,END)
     produceEntry.delete(0,END)
     condimentsEntry.delete(0,END)
     snacksEntry.delete(0,END)
     beveragesEntry.delete(0,END)
     frozenEntry.delete(0,END)

     sareesEntry.delete(0,END)
     kurtasEntry.delete(0,END)
     jeansEntry.delete(0,END)
     shirtsEntry.delete(0,END)
     joggersEntry.delete(0,END)
     shawlsEntry.delete(0,END)
     sweatersEntry.delete(0,END)
     shoesEntry.delete(0,END)
     walletsEntry.delete(0,END)

     ovensEntry.delete(0,END)
     fansEntry.delete(0,END)
     kettlesEntry.delete(0,END)
     lampsEntry.delete(0,END)
     televisionsEntry.delete(0,END)
     stovesEntry.delete(0,END)
     purifiersEntry.delete(0,END)
     heatersEntry.delete(0,END)
     blendersEntry.delete(0,END)

     kneepadsEntry.delete(0,END)
     glovesEntry.delete(0,END)
     netsEntry.delete(0,END)
     batsEntry.delete(0,END)
     helmetsEntry.delete(0,END)
     racquetsEntry.delete(0,END)
     volleyballsEntry.delete(0,END)
     wicketsEntry.delete(0,END)
     frisbeesEntry.delete(0,END)

     concealersEntry.insert(0,0)
     facecreamsEntry.insert(0,0)
     mascarasEntry.insert(0,0)
     hairspraysEntry.insert(0,0)
     lipglossesEntry.insert(0,0)
     bathsoapsEntry.insert(0,0)
     mirrorsEntry.insert(0,0)
     combsEntry.insert(0,0)
     perfumesEntry.insert(0,0)

     meatEntry.insert(0,0)
     grainsEntry.insert(0,0)
     oilEntry.insert(0,0)
     dairyEntry.insert(0,0)
     produceEntry.insert(0,0)
     condimentsEntry.insert(0,0)
     snacksEntry.insert(0,0)
     beveragesEntry.insert(0,0)
     frozenEntry.insert(0,0)

     sareesEntry.insert(0,0)
     kurtasEntry.insert(0,0)
     jeansEntry.insert(0,0)
     shirtsEntry.insert(0,0)
     joggersEntry.insert(0,0)
     shawlsEntry.insert(0,0)
     sweatersEntry.insert(0,0)
     shoesEntry.insert(0,0)
     walletsEntry.insert(0,0)

     ovensEntry.insert(0,0)
     fansEntry.insert(0,0)
     kettlesEntry.insert(0,0)
     lampsEntry.insert(0,0)
     televisionsEntry.insert(0,0)
     stovesEntry.insert(0,0)
     purifiersEntry.insert(0,0)
     heatersEntry.insert(0,0)
     blendersEntry.insert(0,0)

     kneepadsEntry.insert(0,0)
     glovesEntry.insert(0,0)
     netsEntry.insert(0,0)
     batsEntry.insert(0,0)
     helmetsEntry.insert(0,0)
     racquetsEntry.insert(0,0)
     volleyballsEntry.insert(0,0)
     wicketsEntry.insert(0,0)
     frisbeesEntry.insert(0,0)

     cosmetictaxEntry.delete(0,END)
     grocerytaxEntry.delete(0,END)
     clothestaxEntry.delete(0,END)
     appliancestaxEntry.delete(0,END)
     sportsgoodstaxEntry.delete(0,END)

     cosmeticpriceEntry.delete(0,END)
     grocerypriceEntry.delete(0,END)
     clothespriceEntry.delete(0,END)
     appliancespriceEntry.delete(0,END)
     sportsgoodspriceEntry.delete(0,END)

     nameEntry.delete(0,END)
     phoneEntry.delete(0,END)
     billnumberEntry.delete(0,END)

     textarea.delete(1.0,END)

     
def send_email():
     def send_gmail():
          try:
               ob=smtplib.SMTP('smtp.gmail.com',587)
               ob.starttls()
               ob.login(senderEntry.get(),passwordEntry.get())
               message=email_textarea.get(1.0,END)
               ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
               ob.quit()
               messagebox.showinfo('Success','Bill is Successfully sent via Email',parent=root1)
               root1.destroy()
          except:
               messagebox.showerror('Error','Something went wrong, please try again',parent=root1)
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is Empty')
     else:
          root1=Toplevel()
          root1.grab_set()
          root1.title('Send Gmail')
          root1.resizable(0,0)

     senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
     senderFrame.grid(row=0,column=0,padx=40,pady=20)

     senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
     senderLabel.grid(row=0,column=0,padx=10,pady=8)

     senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
     senderEntry.grid(row=0,column=1,padx=10,pady=8)

     passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
     passwordLabel.grid(row=1,column=0,padx=10,pady=8)

     passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
     passwordEntry.grid(row=1,column=1,padx=10,pady=8)

     recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
     recipientFrame.grid(row=1,column=0,padx=40,pady=20)

     recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
     recieverLabel.grid(row=0,column=0,padx=10,pady=8)

     recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
     recieverEntry.grid(row=0,column=1,padx=10,pady=8)

     messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
     messageLabel.grid(row=1,column=0,padx=10,pady=8)

     email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
     email_textarea.grid(row=2,column=0,columnspan=2)
     email_textarea.delete(1.0,END)
     email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

     

     sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
     sendButton.grid(row=2,column=0,pady=20)

     
     


     root1.config(bg='gray20')
     root1.mainloop()

def print_bill():
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is Empty')
     else:
          file=tempfile.mktemp('.txt')
          open(file,'w').write(textarea.get(1.0,END))
          os.startfile(file,'print')
          
def search_bill():
    bill_number = billnumberEntry.get().strip()
    found = False
    for i in os.listdir('bills/'):
        if i.split('.')[0].strip() == bill_number:
            f = open(f"bills/{i}", 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            found = True
            break

    if not found:
        messagebox.showerror('Error', 'Invalid Bill Number')
            

if not os.path.exists('bills'):
     os.mkdir('bills')
def save_bill():
     global billnumber
     result=messagebox.askyesno('Confirm','Do you want to save the Bill?')
     if result:
          bill_content=textarea.get(1.0,END)
          file=open(f'bills/ {billnumber}.txt','w')
          file.write(bill_content)
          file.close()
          messagebox.showinfo('Success',f'Bill Number {billnumber} is saved Successfully')
          billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
      if nameEntry.get()=='' or phoneEntry.get()=='':
          messagebox.showerror('Error','Customer Details are Required')
      elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and clothespriceEntry.get()=='' and appliancespriceEntry.get()=='' and sportsgoodspriceEntry.get()=='':
          messagebox.showerror('Error','No Products are Selected')
      else:
       textarea.delete(1.0,END)

      textarea.insert(END,'\t\t\t**Welcome Customer**\n')
      textarea.insert(END,f'\nBill Number: {billnumber}\n')
      textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
      textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
      textarea.insert(END,'\n=================================================================')
      textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
      textarea.insert(END,'\n=================================================================')
      #cosmetics section
      if concealersEntry.get()!='0':
           textarea.insert(END,f'\nConcealer\t\t\t{concealersEntry.get()}\t\t\t{concealersprice} Rs')
      if facecreamsEntry.get()!='0':
           textarea.insert(END,f'\nFacecream\t\t\t{facecreamsEntry.get()}\t\t\t{facecreamsprice} Rs')
      if mascarasEntry.get()!='0':
           textarea.insert(END,f'\nMascara\t\t\t{mascarasEntry.get()}\t\t\t{mascarasprice} Rs')
      if hairspraysEntry.get()!='0':
           textarea.insert(END,f'\nHairspray\t\t\t{hairspraysEntry.get()}\t\t\t{hairspraysprice} Rs')
      if lipglossesEntry.get()!='0':
           textarea.insert(END,f'\nLipgloss\t\t\t{lipglossesEntry.get()}\t\t\t{lipglossesprice} Rs')
      if bathsoapsEntry.get()!='0':
           textarea.insert(END,f'\nBathsoap\t\t\t{bathsoapsEntry.get()}\t\t\t{bathsoapsprice} Rs')
      if mirrorsEntry.get()!='0':
           textarea.insert(END,f'\nMirror\t\t\t{mirrorsEntry.get()}\t\t\t{mirrorsprice} Rs')
      if combsEntry.get()!='0':
           textarea.insert(END,f'\nComb\t\t\t{combsEntry.get()}\t\t\t{combsprice} Rs')
      if perfumesEntry.get()!='0':
           textarea.insert(END,f'\nPerfume\t\t\t{perfumesEntry.get()}\t\t\t{perfumesprice} Rs')
      #groceries section
      if meatEntry.get()!='0':
           textarea.insert(END,f'\nMeat\t\t\t{meatEntry.get()}\t\t\t{meatprice} Rs')
      if grainsEntry.get()!='0':
           textarea.insert(END,f'\nGrains\t\t\t{grainsEntry.get()}\t\t\t{grainsprice} Rs')
      if oilEntry.get()!='0':
           textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
      if dairyEntry.get()!='0':
           textarea.insert(END,f'\nDairy\t\t\t{dairyEntry.get()}\t\t\t{dairyprice} Rs')
      if produceEntry.get()!='0':
           textarea.insert(END,f'\nProduce\t\t\t{produceEntry.get()}\t\t\t{produceprice} Rs')
      if condimentsEntry.get()!='0':
           textarea.insert(END,f'\nCondiments\t\t\t{condimentsEntry.get()}\t\t\t{condimentsprice} Rs')
      if snacksEntry.get()!='0':
           textarea.insert(END,f'\nSnack\t\t\t{snacksEntry.get()}\t\t\t{snacksprice} Rs')
      if beveragesEntry.get()!='0':
           textarea.insert(END,f'\nBeverage\t\t\t{beveragesEntry.get()}\t\t\t{beveragesprice} Rs')
      if frozenEntry.get()!='0':
           textarea.insert(END,f'\nFrozen\t\t\t{frozenEntry.get()}\t\t\t{frozenprice} Rs')
      #clothing section
      if sareesEntry.get()!='0':
           textarea.insert(END,f'\nSaree\t\t\t{sareesEntry.get()}\t\t\t{sareesprice} Rs')
      if kurtasEntry.get()!='0':
           textarea.insert(END,f'\nKurta\t\t\t{kurtasEntry.get()}\t\t\t{kurtasprice} Rs')
      if jeansEntry.get()!='0':
           textarea.insert(END,f'\nJean\t\t\t{jeansEntry.get()}\t\t\t{jeansprice} Rs')
      if shirtsEntry.get()!='0':
           textarea.insert(END,f'\nShirt\t\t\t{shirtsEntry.get()}\t\t\t{shirtsprice} Rs')
      if joggersEntry.get()!='0':
           textarea.insert(END,f'\nJogger\t\t\t{joggersEntry.get()}\t\t\t{joggersprice} Rs')
      if shawlsEntry.get()!='0':
           textarea.insert(END,f'\nShawl\t\t\t{shawlsEntry.get()}\t\t\t{shawlsprice} Rs')
      if sweatersEntry.get()!='0':
           textarea.insert(END,f'\nSweater\t\t\t{sweatersEntry.get()}\t\t\t{sweatersprice} Rs')
      if shoesEntry.get()!='0':
           textarea.insert(END,f'\nShoes\t\t\t{shoesEntry.get()}\t\t\t{shoesprice} Rs')
      if walletsEntry.get()!='0':
           textarea.insert(END,f'\nWallet\t\t\t{walletsEntry.get()}\t\t\t{walletsprice} Rs')
      #appliances section
      if ovensEntry.get()!='0':
           textarea.insert(END,f'\nOven\t\t\t{ovensEntry.get()}\t\t\t{ovensprice} Rs')
      if fansEntry.get()!='0':
           textarea.insert(END,f'\nFan\t\t\t{fansEntry.get()}\t\t\t{fansprice} Rs')
      if kettlesEntry.get()!='0':
           textarea.insert(END,f'\nKettle\t\t\t{kettlesEntry.get()}\t\t\t{kettlesprice} Rs')
      if lampsEntry.get()!='0':
           textarea.insert(END,f'\nLamp\t\t\t{lampsEntry.get()}\t\t\t{lampsprice} Rs')
      if televisionsEntry.get()!='0':
           textarea.insert(END,f'\nTelevision\t\t\t{televisionsEntry.get()}\t\t\t{televisionsprice} Rs')
      if stovesEntry.get()!='0':
           textarea.insert(END,f'\nStove\t\t\t{stovesEntry.get()}\t\t\t{stovesprice} Rs')
      if purifiersEntry.get()!='0':
           textarea.insert(END,f'\nPurifier\t\t\t{purifiersEntry.get()}\t\t\t{purifiersprice} Rs')
      if heatersEntry.get()!='0':
           textarea.insert(END,f'\nHeater\t\t\t{heatersEntry.get()}\t\t\t{heatersprice} Rs')
      if blendersEntry.get()!='0':
           textarea.insert(END,f'\nBlender\t\t\t{blendersEntry.get()}\t\t\t{blendersprice} Rs')
      #sportsgoods section
      if kneepadsEntry.get()!='0':
           textarea.insert(END,f'\nKneepad\t\t\t{kneepadsEntry.get()}\t\t\t{kneepadsprice} Rs')
      if glovesEntry.get()!='0':
           textarea.insert(END,f'\nGlove\t\t\t{glovesEntry.get()}\t\t\t{glovesprice} Rs')
      if netsEntry.get()!='0':
           textarea.insert(END,f'\nNet\t\t\t{netsEntry.get()}\t\t\t{netsprice} Rs')
      if batsEntry.get()!='0':
           textarea.insert(END,f'\nBat\t\t\t{batsEntry.get()}\t\t\t{batsprice} Rs')
      if helmetsEntry.get()!='0':
           textarea.insert(END,f'\nHelmet\t\t\t{helmetsEntry.get()}\t\t\t{helmetsprice} Rs')
      if racquetsEntry.get()!='0':
           textarea.insert(END,f'\nRacquet\t\t\t{racquetsEntry.get()}\t\t\t{racquetsprice} Rs')
      if volleyballsEntry.get()!='0':
           textarea.insert(END,f'\nVolleyball\t\t\t{volleyballsEntry.get()}\t\t\t{volleyballsprice} Rs')
      if wicketsEntry.get()!='0':
           textarea.insert(END,f'\nWicket\t\t\t{wicketsEntry.get()}\t\t\t{wicketsprice} Rs')
      if frisbeesEntry.get()!='0':
           textarea.insert(END,f'\nFrisbee\t\t\t{frisbeesEntry.get()}\t\t\t{frisbeesprice} Rs')
      textarea.insert(END,'\n-----------------------------------------------------------------')


      if cosmetictaxEntry.get()!='0.0 Rs':
           textarea.insert(END,f'\nCosmetic Tax\t\t\t {cosmetictaxEntry.get()}')
      if grocerytaxEntry.get()!='0.0 Rs':
           textarea.insert(END,f'\nGrocery Tax\t\t\t {grocerytaxEntry.get()}')
      if clothestaxEntry.get()!='0.0 Rs':
           textarea.insert(END,f'\nClothing Tax\t\t\t {clothestaxEntry.get()}')
      if appliancestaxEntry.get()!='0.0 Rs':
           textarea.insert(END,f'\nAppliance Tax\t\t\t {appliancestaxEntry.get()}')
      if sportsgoodstaxEntry.get()!='0.0 Rs':
           textarea.insert(END,f'\nSportsgoods Tax\t\t\t {sportsgoodstaxEntry.get()}')
      textarea.insert(END,f'\n\nTotal Bill\t\t\t {totalbill}')
      textarea.insert(END,'\n-----------------------------------------------------------------')
      save_bill()
        
      
def total():
   global concealersprice,facecreamsprice,mascarasprice,hairspraysprice,lipglossesprice,bathsoapsprice,mirrorsprice,combsprice,perfumesprice
   global meatprice,grainsprice,oilprice,dairyprice,produceprice,condimentsprice,snacksprice,beveragesprice,frozenprice
   global sareesprice,kurtasprice,jeansprice,shirtsprice,joggersprice,shawlsprice,sweatersprice,shoesprice,walletsprice
   global ovensprice,fansprice,kettlesprice,lampsprice,televisionsprice,stovesprice,purifiersprice,heatersprice,blendersprice
   global kneepadsprice,glovesprice,netsprice,batsprice,helmetsprice,racquetsprice,volleyballsprice,wicketsprice,frisbeesprice
   global totalbill
   #Cosmetics price collection 
   concealersprice=int(concealersEntry.get())*300
   facecreamsprice=int(facecreamsEntry.get())*200
   mascarasprice=int(mascarasEntry.get())*400
   hairspraysprice=int(hairspraysEntry.get())*200
   lipglossesprice=int(lipglossesEntry.get())*300
   bathsoapsprice=int(bathsoapsEntry.get())*50
   mirrorsprice=int(mirrorsEntry.get())*50
   combsprice=int(combsEntry.get())*60
   perfumesprice=int(perfumesEntry.get())*500

   totalcosmeticsprice=concealersprice+facecreamsprice+mascarasprice+hairspraysprice+lipglossesprice+bathsoapsprice+mirrorsprice+combsprice+perfumesprice
   cosmeticpriceEntry.delete(0,END)
   cosmeticpriceEntry.insert(0,str(totalcosmeticsprice) +'Rs')
   cosmetictax=totalcosmeticsprice*0.18
   cosmetictaxEntry.delete(0,END)
   cosmetictaxEntry.insert(0,str(cosmetictax) + ' Rs')

   #Groceries price collection
   meatprice=int(meatEntry.get())*300
   grainsprice=int(grainsEntry.get())*1200
   oilprice=int(oilEntry.get())*400
   dairyprice=int(dairyEntry.get())*70
   produceprice=int(produceEntry.get())*100
   condimentsprice=int(condimentsEntry.get())*50
   snacksprice=int(snacksEntry.get())*60
   beveragesprice=int(beveragesEntry.get())*50
   frozenprice=int(frozenEntry.get())*985

   totalgroceriesprice=meatprice+grainsprice+oilprice+dairyprice+produceprice+condimentsprice+snacksprice+beveragesprice+frozenprice
   grocerypriceEntry.delete(0,END)
   grocerypriceEntry.insert(0,str(totalgroceriesprice) +' Rs')
   grocerytax=totalgroceriesprice*0.05
   grocerytaxEntry.delete(0,END)
   grocerytaxEntry.insert(0,str(grocerytax) + ' Rs')

   #Clothes Price Collection
   sareesprice=int(sareesEntry.get())*900
   kurtasprice=int(kurtasEntry.get())*1000
   jeansprice=int(jeansEntry.get())*2000
   shirtsprice=int(shirtsEntry.get())*800
   joggersprice=int(joggersEntry.get())*600
   shawlsprice=int(shawlsEntry.get())*300
   sweatersprice=int(sweatersEntry.get())*1300
   shoesprice=int(shoesEntry.get())*965
   walletsprice=int(walletsEntry.get())*600

   totalclothesprice=sareesprice+kurtasprice+jeansprice+shirtsprice+joggersprice+shawlsprice+sweatersprice+shoesprice+walletsprice
   clothespriceEntry.delete(0,END)
   clothespriceEntry.insert(0,str(totalclothesprice) +'Rs')
   clothestax=totalclothesprice*0.13
   clothestaxEntry.delete(0,END)
   clothestaxEntry.insert(0,str(clothestax) + ' Rs')

   #Appliances Price Collection
   ovensprice=int(ovensEntry.get())*5000
   fansprice=int(fansEntry.get())*1500
   kettlesprice=int(kettlesEntry.get())*1200
   lampsprice=int(lampsEntry.get())*1200
   televisionsprice=int(televisionsEntry.get())*20000
   stovesprice=int(stovesEntry.get())*3000
   purifiersprice=int(purifiersEntry.get())*8500
   heatersprice=int(heatersEntry.get())*4000
   blendersprice=int(blendersEntry.get())*3000

   totalappliancesprice=ovensprice+fansprice+kettlesprice+lampsprice+televisionsprice+stovesprice+purifiersprice+heatersprice+blendersprice
   appliancespriceEntry.delete(0,END)
   appliancespriceEntry.insert(0,str(totalappliancesprice) + 'Rs')
   appliancetax=totalappliancesprice*0.06
   appliancestaxEntry.delete(0,END)
   appliancestaxEntry.insert(0,str(appliancetax) + ' Rs')

   #Sports Goods
   kneepadsprice=int(kneepadsEntry.get())*1657
   glovesprice=int(glovesEntry.get())*1100
   netsprice=int(netsEntry.get())*760
   batsprice=int(batsEntry.get())*500
   helmetsprice=int(helmetsEntry.get())*2500
   racquetsprice=int(racquetsEntry.get())*587
   volleyballsprice=int(volleyballsEntry.get())*1000
   wicketsprice=int(wicketsEntry.get())*1500
   frisbeesprice=int(frisbeesEntry.get())*35

   totalsportsgoodsprice=kneepadsprice+glovesprice+netsprice+batsprice+helmetsprice+racquetsprice+volleyballsprice+wicketsprice+frisbeesprice
   sportsgoodspriceEntry.delete(0,END)
   sportsgoodspriceEntry.insert(0,str(totalsportsgoodsprice) + 'Rs')
   sportsgoodstax=totalsportsgoodsprice*0.12
   sportsgoodstaxEntry.delete(0,END)
   sportsgoodstaxEntry.insert(0,str(sportsgoodstax) + ' Rs')

   totalbill=totalcosmeticsprice+totalgroceriesprice+totalclothesprice+totalappliancesprice+totalsportsgoodsprice+cosmetictax+grocerytax+clothestax+appliancetax+sportsgoodstax


#GUI Part
root=Tk()
root.title('Retail Billing System')
root.geometry('1910x1200')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=55)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=50)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=55,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=50)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=55,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=50)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=55,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

concealersLabel=Label(cosmeticsFrame,text='Concealers',font=('times new roman',15,'bold'),bg='gray20',fg='white')
concealersLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

concealersEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
concealersEntry.grid(row=0,column=1,pady=9,padx=10)
concealersEntry.insert(0,0)

facecreamsLabel=Label(cosmeticsFrame,text='Face Creams',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamsLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamsEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamsEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamsEntry.insert(0,0)

mascarasLabel=Label(cosmeticsFrame,text='Mascaras',font=('times new roman',15,'bold'),bg='gray20',fg='white')
mascarasLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

mascarasEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
mascarasEntry.grid(row=2,column=1,pady=9,padx=10)
mascarasEntry.insert(0,0)

hairspraysLabel=Label(cosmeticsFrame,text='Hair Sprays',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairspraysLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairspraysEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairspraysEntry.grid(row=3,column=1,pady=9,padx=10)
hairspraysEntry.insert(0,0)

lipglossesLabel=Label(cosmeticsFrame,text='Lip Glosses',font=('times new roman',15,'bold'),bg='gray20',fg='white')
lipglossesLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

lipglossesEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
lipglossesEntry.grid(row=4,column=1,pady=9,padx=10)
lipglossesEntry.insert(0,0)

bathsoapsLabel=Label(cosmeticsFrame,text='Bath Soaps',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapsLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bathsoapsEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapsEntry.grid(row=5,column=1,pady=9,padx=10)
bathsoapsEntry.insert(0,0)

mirrorsLabel=Label(cosmeticsFrame,text='Mirrors',font=('times new roman',15,'bold'),bg='gray20',fg='white')
mirrorsLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')

mirrorsEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
mirrorsEntry.grid(row=6,column=1,pady=9,padx=10)
mirrorsEntry.insert(0,0)

combsLabel=Label(cosmeticsFrame,text='Combs',font=('times new roman',15,'bold'),bg='gray20',fg='white')
combsLabel.grid(row=7,column=0,pady=9,padx=10,sticky='w')

combsEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
combsEntry.grid(row=7,column=1,pady=9,padx=10)
combsEntry.insert(0,0)

perfumesLabel=Label(cosmeticsFrame,text='Perfumes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
perfumesLabel.grid(row=8,column=0,pady=9,padx=10,sticky='w')

perfumesEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
perfumesEntry.grid(row=8,column=1,pady=9,padx=10)
perfumesEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Groceries',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

meatLabel=Label(groceryFrame,text='Meat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
meatLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

meatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
meatEntry.grid(row=0,column=1,pady=9,padx=10)
meatEntry.insert(0,0)

grainsLabel=Label(groceryFrame,text='Grains',font=('times new roman',15,'bold'),bg='gray20',fg='white')
grainsLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grainsEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grainsEntry.grid(row=1,column=1,pady=9,padx=10)
grainsEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=2,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

dairyLabel=Label(groceryFrame,text='Dairy',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dairyLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dairyEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dairyEntry.grid(row=3,column=1,pady=9,padx=10)
dairyEntry.insert(0,0)

produceLabel=Label(groceryFrame,text='Produce',font=('times new roman',15,'bold'),bg='gray20',fg='white')
produceLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

produceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
produceEntry.grid(row=4,column=1,pady=9,padx=10)
produceEntry.insert(0,0)

condimentsLabel=Label(groceryFrame,text='Condiments',font=('times new roman',15,'bold'),bg='gray20',fg='white')
condimentsLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

condimentsEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
condimentsEntry.grid(row=5,column=1,pady=9,padx=10)
condimentsEntry.insert(0,0)

snacksLabel=Label(groceryFrame,text='Snacks',font=('times new roman',15,'bold'),bg='gray20',fg='white')
snacksLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')

snacksEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
snacksEntry.grid(row=6,column=1,pady=9,padx=10)
snacksEntry.insert(0,0)

beveragesLabel=Label(groceryFrame,text='Beverages',font=('times new roman',15,'bold'),bg='gray20',fg='white')
beveragesLabel.grid(row=7,column=0,pady=9,padx=10,sticky='w')

beveragesEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
beveragesEntry.grid(row=7,column=1,pady=9,padx=10)
beveragesEntry.insert(0,0)

frozenLabel=Label(groceryFrame,text='Frozen',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frozenLabel.grid(row=8,column=0,pady=9,padx=10,sticky='w')

frozenEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frozenEntry.grid(row=8,column=1,pady=9,padx=10)
frozenEntry.insert(0,0)


clothingFrame=LabelFrame(productsFrame,text='Clothes',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
clothingFrame.grid(row=0,column=2)

sareesLabel=Label(clothingFrame,text='Sarees',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sareesLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

sareesEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sareesEntry.grid(row=0,column=1,pady=9,padx=10)
sareesEntry.insert(0,0)

kurtasLabel=Label(clothingFrame,text='Kurtas',font=('times new roman',15,'bold'),bg='gray20',fg='white')
kurtasLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

kurtasEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
kurtasEntry.grid(row=1,column=1,pady=9,padx=10)
kurtasEntry.insert(0,0)

jeansLabel=Label(clothingFrame,text='Jeans',font=('times new roman',15,'bold'),bg='gray20',fg='white')
jeansLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

jeansEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
jeansEntry.grid(row=2,column=1,pady=9,padx=10)
jeansEntry.insert(0,0)

shirtsLabel=Label(clothingFrame,text='Shirts',font=('times new roman',15,'bold'),bg='gray20',fg='white')
shirtsLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

shirtsEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
shirtsEntry.grid(row=3,column=1,pady=9,padx=10)
shirtsEntry.insert(0,0)

joggersLabel=Label(clothingFrame,text='Joggers',font=('times new roman',15,'bold'),bg='gray20',fg='white')
joggersLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

joggersEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
joggersEntry.grid(row=4,column=1,pady=9,padx=10)
joggersEntry.insert(0,0)

shawlsLabel=Label(clothingFrame,text='Shawls',font=('times new roman',15,'bold'),bg='gray20',fg='white')
shawlsLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

shawlsEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
shawlsEntry.grid(row=5,column=1,pady=9,padx=10)
shawlsEntry.insert(0,0)

sweatersLabel=Label(clothingFrame,text='Sweaters',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sweatersLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')

sweatersEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sweatersEntry.grid(row=6,column=1,pady=9,padx=10)
sweatersEntry.insert(0,0)

shoesLabel=Label(clothingFrame,text='Shoes',font=('times new roman',15,'bold'),bg='gray20',fg='white')
shoesLabel.grid(row=7,column=0,pady=9,padx=10,sticky='w')

shoesEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
shoesEntry.grid(row=7,column=1,pady=9,padx=10)
shoesEntry.insert(0,0)

walletsLabel=Label(clothingFrame,text='Wallets',font=('times new roman',15,'bold'),bg='gray20',fg='white')
walletsLabel.grid(row=8,column=0,pady=9,padx=10,sticky='w')

walletsEntry=Entry(clothingFrame,font=('times new roman',15,'bold'),width=10,bd=5)
walletsEntry.grid(row=8,column=1,pady=9,padx=10)
walletsEntry.insert(0,0)

appliancesFrame=LabelFrame(productsFrame,text='Home Appliances',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
appliancesFrame.grid(row=0,column=3)

ovensLabel=Label(appliancesFrame,text='Ovens',font=('times new roman',15,'bold'),bg='gray20',fg='white')
ovensLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

ovensEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ovensEntry.grid(row=0,column=1,pady=9,padx=10)
ovensEntry.insert(0,0)

fansLabel=Label(appliancesFrame,text='Fans',font=('times new roman',15,'bold'),bg='gray20',fg='white')
fansLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

fansEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fansEntry.grid(row=1,column=1,pady=9,padx=10)
fansEntry.insert(0,0)

kettlesLabel=Label(appliancesFrame,text='Kettles',font=('times new roman',15,'bold'),bg='gray20',fg='white')
kettlesLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

kettlesEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
kettlesEntry.grid(row=2,column=1,pady=9,padx=10)
kettlesEntry.insert(0,0)

lampsLabel=Label(appliancesFrame,text='Lamps',font=('times new roman',15,'bold'),bg='gray20',fg='white')
lampsLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

lampsEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
lampsEntry.grid(row=3,column=1,pady=9,padx=10)
lampsEntry.insert(0,0)

televisionsLabel=Label(appliancesFrame,text='Televisions',font=('times new roman',15,'bold'),bg='gray20',fg='white')
televisionsLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

televisionsEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
televisionsEntry.grid(row=4,column=1,pady=9,padx=10)
televisionsEntry.insert(0,0)

stovesLabel=Label(appliancesFrame,text='Stoves',font=('times new roman',15,'bold'),bg='gray20',fg='white')
stovesLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

stovesEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
stovesEntry.grid(row=5,column=1,pady=9,padx=10)
stovesEntry.insert(0,0)

purifiersLabel=Label(appliancesFrame,text='Purifiers',font=('times new roman',15,'bold'),bg='gray20',fg='white')
purifiersLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')

purifiersEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
purifiersEntry.grid(row=6,column=1,pady=9,padx=10)
purifiersEntry.insert(0,0)

heatersLabel=Label(appliancesFrame,text='Heaters',font=('times new roman',15,'bold'),bg='gray20',fg='white')
heatersLabel.grid(row=7,column=0,pady=9,padx=10,sticky='w')

heatersEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
heatersEntry.grid(row=7,column=1,pady=9,padx=10)
heatersEntry.insert(0,0)

blendersLabel=Label(appliancesFrame,text='Blenders',font=('times new roman',15,'bold'),bg='gray20',fg='white')
blendersLabel.grid(row=8,column=0,pady=9,padx=10,sticky='w')

blendersEntry=Entry(appliancesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
blendersEntry.grid(row=8,column=1,pady=9,padx=10)
blendersEntry.insert(0,0)

sportsFrame=LabelFrame(productsFrame,text='Sports Goods',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
sportsFrame.grid(row=0,column=4)

kneepadsLabel=Label(sportsFrame,text='Knee Pads',font=('times new roman',15,'bold'),bg='gray20',fg='white')
kneepadsLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

kneepadsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
kneepadsEntry.grid(row=0,column=1,pady=9,padx=10)
kneepadsEntry.insert(0,0)

glovesLabel=Label(sportsFrame,text='Gloves',font=('times new roman',15,'bold'),bg='gray20',fg='white')
glovesLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

glovesEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
glovesEntry.grid(row=1,column=1,pady=9,padx=10)
glovesEntry.insert(0,0)

netsLabel=Label(sportsFrame,text='Nets',font=('times new roman',15,'bold'),bg='gray20',fg='white')
netsLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

netsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
netsEntry.grid(row=2,column=1,pady=9,padx=10)
netsEntry.insert(0,0)

batsLabel=Label(sportsFrame,text='Bats',font=('times new roman',15,'bold'),bg='gray20',fg='white')
batsLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

batsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
batsEntry.grid(row=3,column=1,pady=9,padx=10)
batsEntry.insert(0,0)

helmetsLabel=Label(sportsFrame,text='Helmets',font=('times new roman',15,'bold'),bg='gray20',fg='white')
helmetsLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

helmetsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
helmetsEntry.grid(row=4,column=1,pady=9,padx=10)
helmetsEntry.insert(0,0)

racquetsLabel=Label(sportsFrame,text='Racquets',font=('times new roman',15,'bold'),bg='gray20',fg='white')
racquetsLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

racquetsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
racquetsEntry.grid(row=5,column=1,pady=9,padx=10)
racquetsEntry.insert(0,0)

volleyballsLabel=Label(sportsFrame,text='Volley Balls',font=('times new roman',15,'bold'),bg='gray20',fg='white')
volleyballsLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')

volleyballsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
volleyballsEntry.grid(row=6,column=1,pady=9,padx=10)
volleyballsEntry.insert(0,0)

wicketsLabel=Label(sportsFrame,text='Wickets',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wicketsLabel.grid(row=7,column=0,pady=9,padx=10,sticky='w')

wicketsEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wicketsEntry.grid(row=7,column=1,pady=9,padx=10)
wicketsEntry.insert(0,0)

frisbeesLabel=Label(sportsFrame,text='Frisbees',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frisbeesLabel.grid(row=8,column=0,pady=9,padx=10,sticky='w')

frisbeesEntry=Entry(sportsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frisbeesEntry.grid(row=8,column=1,pady=9,padx=10)
frisbeesEntry.insert(0,0)

billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=5,padx=10)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=28,width=65,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetics Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=13,padx=40,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=13,padx=40)

grocerypriceLabel=Label(billmenuFrame,text='Groceries Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=11,padx=40,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=11,padx=40)

clothespriceLabel=Label(billmenuFrame,text='Clothing Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
clothespriceLabel.grid(row=2,column=0,pady=11,padx=40,sticky='w')

clothespriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
clothespriceEntry.grid(row=2,column=1,pady=11,padx=40)

appliancespriceLabel=Label(billmenuFrame,text='Appliances Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
appliancespriceLabel.grid(row=3,column=0,pady=11,padx=40,sticky='w')

appliancespriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
appliancespriceEntry.grid(row=3,column=1,pady=11,padx=40)

sportsgoodspriceLabel=Label(billmenuFrame,text='Sports Goods Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sportsgoodspriceLabel.grid(row=4,column=0,pady=11,padx=40,sticky='w')

sportsgoodspriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sportsgoodspriceEntry.grid(row=4,column=1,pady=11,padx=40)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetics Tax',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=11,padx=40,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=11,padx=40)

grocerytaxLabel=Label(billmenuFrame,text='Groceries Tax',font=('times new roman',15,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=11,padx=40,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=11,padx=40)

clothestaxLabel=Label(billmenuFrame,text='Clothing Tax',font=('times new roman',15,'bold'),bg='gray20',fg='white')
clothestaxLabel.grid(row=2,column=2,pady=11,padx=40,sticky='w')

clothestaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
clothestaxEntry.grid(row=2,column=3,pady=11,padx=40)

appliancestaxLabel=Label(billmenuFrame,text='Appliances Tax',font=('times new roman',15,'bold'),bg='gray20',fg='white')
appliancestaxLabel.grid(row=3,column=2,pady=11,padx=40,sticky='w')

appliancestaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
appliancestaxEntry.grid(row=3,column=3,pady=11,padx=40)

sportsgoodstaxLabel=Label(billmenuFrame,text='Sports Goods Tax',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sportsgoodstaxLabel.grid(row=4,column=2,pady=13,padx=40,sticky='w')

sportsgoodstaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sportsgoodstaxEntry.grid(row=4,column=3,pady=13,padx=40)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=5)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=41)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=41)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=41)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=41)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=41)




root.mainloop()