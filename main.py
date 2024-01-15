from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Système de Gestion de Facturation')
root.geometry('1280x720')
bg_color = '#2D9290'

# =====================variables===================
stock_initial = {'Beignets': {'id': 1, 'quantity': 5}, 'Vin': {'id': 2, 'quantity': 5}, 'Riz': {'id': 3, 'quantity': 5}, 'Lait': {'id': 4, 'quantity': 5}}
stock_actuel = {item: {'id': stock_initial[item]['id'], 'quantity': stock_initial[item]['quantity']} for item in stock_initial}
Beignets = IntVar()
Vin = IntVar()
Riz = IntVar()
Gal = IntVar()
Total = IntVar()

cb = StringVar()
cw = StringVar()
cr = StringVar()
cg = StringVar()
cout_total = StringVar()

# ===========Fonctions===============
def update_stock():
    # Obtenez les quantités vendues
    b_sold = Beignets.get()
    w_sold = Vin.get()
    r_sold = Riz.get()
    g_sold = Gal.get()

    # Vérifiez si la quantité vendue est supérieure au stock
    if b_sold > stock_actuel['Beignets']['quantity'] or w_sold > stock_actuel['Vin']['quantity'] or r_sold > stock_actuel['Riz']['quantity'] or g_sold > stock_actuel['Lait']['quantity']:
        messagebox.showerror('Erreur de stock', 'La quantité vendue est supérieure au stock disponible.')
        return

    # Vérifiez si le stock est égal à zéro
    if stock_actuel['Beignets']['quantity'] == 0 or stock_actuel['Vin']['quantity'] == 0 or stock_actuel['Riz']['quantity'] == 0 or stock_actuel['Lait']['quantity'] == 0:
        messagebox.showerror('Stock épuisé', 'Le stock est épuisé. Impossible de vendre.')
        return

    # Mettez à jour le stock
    stock_actuel['Beignets']['quantity'] -= b_sold
    stock_actuel['Vin']['quantity'] -= w_sold
    stock_actuel['Riz']['quantity'] -= r_sold
    stock_actuel['Lait']['quantity'] -= g_sold

    # Mettez à jour les labels affichant le stock actuel
    stock_beignets_label.config(text=f' {stock_actuel["Beignets"]["quantity"]}')
    stock_Vin_label.config(text=f' {stock_actuel["Vin"]["quantity"]}')
    stock_Riz_label.config(text=f' {stock_actuel["Riz"]["quantity"]}')
    stock_Lait_label.config(text=f' {stock_actuel["Lait"]["quantity"]}')

def total():
    if Beignets.get() == 0 and Vin.get() == 0 and Riz.get() == 0 and Gal.get() == 0:
        messagebox.showwarning('Erreur', 'Veuillez sélectionner une quantité svp')
    else:
        b = Beignets.get()
        w = Vin.get()
        r = Riz.get()
        g = Gal.get()

        t = float(b * 1.89 + w * 8.99 + r * 2.10 + g * 4.50)
        Total.set(b + w + r + g)
        cout_total.set(str(round(t, 2)) + ' FCFA')

        cb.set(str(round(b * 1.89, 2)) + ' FCFA')
        cw.set(str(round(w * 8.99, 2)) + ' FCFA')
        cr.set(str(round(r * 2.10, 2)) + ' FCFA')
        cg.set(str(round(g * 4.50, 2)) + ' FCFA')

def reinitialiser():
    # Réinitialiser les quantités
    Beignets.set(0)
    Vin.set(0)
    Riz.set(0)
    Gal.set(0)
    Total.set(0)

    # Réinitialiser les coûts
    cb.set('')
    cw.set('')
    cr.set('')
    cg.set('')
    cout_total.set('')

    # Réinitialiser le stock aux valeurs initiales
    for item in stock_initial:
        stock_actuel[item]['quantity'] = stock_initial[item]['quantity']

def facture():
    b = Beignets.get()
    w = Vin.get()
    r = Riz.get()
    g = Gal.get()

    # Vérifiez si la quantité vendue est supérieure au stock
    if b > stock_actuel['Beignets']['quantity'] or w > stock_actuel['Vin']['quantity'] or r > stock_actuel['Riz']['quantity'] or g > stock_actuel['Lait']['quantity']:
        messagebox.showerror('Erreur de stock', 'La quantité vendue est supérieure au stock disponible. Génération de facture impossible.')
        return 0
    else:
        stock_actuel['Beignets']['quantity'] -= b
        stock_actuel['Vin']['quantity'] -= w
        stock_actuel['Riz']['quantity'] -= r
        stock_actuel['Lait']['quantity'] -= g
    update_stock()  # Mettons à jour le stock en fonction des quantités avant la génération de la facture

    textarea.delete(1.0, END)
    textarea.insert(END, ' Articles\t\tQuantitée(s)      \tCoûts\n')
    textarea.insert(END, f'\nBeignets\t\t{b}\t  {cb.get()}')
    textarea.insert(END, f'\n\nVin\t\t{w}\t  {cw.get()}')
    textarea.insert(END, f'\n\nRiz\t\t{r}\t  {cr.get()}')
    textarea.insert(END, f'\n\nLait\t\t{g}\t  {cg.get()}')
    textarea.insert(END, f"\n\n================================")
    textarea.insert(END, f'\nPrix Total\t\t{Total.get()}\t{cout_total.get()}')
    textarea.insert(END, f"\n================================")
    textarea.insert(END, f"\n================================")

def quitter():
    if messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ?'):
        root.destroy()

title = Label(root, pady=5, text="EyangMarketplace", bd=12, bg=bg_color, fg='white', font=('times new roman', 35, 'bold'), relief=GROOVE, justify=CENTER)
title.pack(fill=X)

# ===============Details des Articles=====================
F1 = LabelFrame(root, text='Details des Articles', font=('times new romon', 18, 'bold'), fg='gold', bg=bg_color, bd=15, relief=RIDGE)
F1.place(x=5, y=90, width=950, height=500)

# =====================En-tete=================================
stk= Label(F1, text='Stock', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
stk.grid(row=0, column=0, padx=20, pady=15)

itm = Label(F1, text='Articles', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
itm.grid(row=0, column=1, padx=20, pady=15)

n = Label(F1, text='Nombre d\'articles', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
n.grid(row=0, column=2, padx=30, pady=15)

cost = Label(F1, text='Coûts', font=('Helvetic', 25, 'bold', 'underline'), fg='black', bg=bg_color)
cost.grid(row=0, column=3, padx=30, pady=15)

# ===============Articles=====================
bread = Label(F1, text='Beignets', font=('times new rommon', 20, 'bold'), fg='lawngreen', bg=bg_color)
bread.grid(row=1, column=1, padx=20, pady=15)
b_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Beignets, justify=CENTER)
b_txt.grid(row=1, column=2, padx=20, pady=15)
cb_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cb, justify=CENTER)
cb_txt.grid(row=1, column=3, padx=20, pady=15)

Vin_label = Label(F1, text='Vin', font=('times new rommon', 20, 'bold'), fg='lawngreen', bg=bg_color)
Vin_label.grid(row=2, column=1, padx=20, pady=15)
w_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Vin, justify=CENTER)
w_txt.grid(row=2, column=2, padx=20, pady=15)
cw_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cw, justify=CENTER)
cw_txt.grid(row=2, column=3, padx=20, pady=15)

Riz_label = Label(F1, text='Riz', font=('times new rommon', 20, 'bold'), fg='lawngreen', bg=bg_color)
Riz_label.grid(row=3, column=1, padx=20, pady=15)
r_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Riz, justify=CENTER)
r_txt.grid(row=3, column=2, padx=20, pady=15)
cr_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cr, justify=CENTER)
cr_txt.grid(row=3, column=3, padx=20, pady=15)

gal_label = Label(F1, text='Lait', font=('times new rommon', 20, 'bold'), fg='lawngreen', bg=bg_color)
gal_label.grid(row=4, column=1, padx=20, pady=15)
g_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Gal, justify=CENTER)
g_txt.grid(row=4, column=2, padx=20, pady=15)
cg_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cg, justify=CENTER)
cg_txt.grid(row=4, column=3, padx=20, pady=15)

t_label = Label(F1, text='Total', font=('times new rommon', 20, 'bold'), fg='lawngreen', bg=bg_color)
t_label.grid(row=5, column=1, padx=20, pady=15)
t_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=Total, justify=CENTER)
t_txt.grid(row=5, column=2, padx=20, pady=15)
totalcost_txt = Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, textvariable=cout_total, justify=CENTER)
totalcost_txt.grid(row=5, column=3, padx=20, pady=15)

stock_beignets_label = Label(F1, text=f' {stock_actuel["Beignets"]["quantity"]}', font=('times new rommon', 15, 'bold'), fg='black', bg=bg_color)
stock_beignets_label.grid(row=1, column=0, padx=20, pady=15)

stock_Vin_label = Label(F1, text=f' {stock_actuel["Vin"]["quantity"]}', font=('times new rommon', 15, 'bold'), fg='black', bg=bg_color)
stock_Vin_label.grid(row=2, column=0, padx=20, pady=15)

stock_Riz_label = Label(F1, text=f' {stock_actuel["Riz"]["quantity"]}', font=('times new rommon', 15, 'bold'), fg='black', bg=bg_color)
stock_Riz_label.grid(row=3, column=0, padx=20, pady=15)

stock_Lait_label = Label(F1, text=f' {stock_actuel["Lait"]["quantity"]}', font=('times new rommon', 15, 'bold'), fg='black', bg=bg_color)
stock_Lait_label.grid(row=4, column=0, padx=20, pady=15)

# =====================Bill area====================
F2 = Frame(root, relief=GROOVE, bd=10)
F2.place(x=960, y=90, width=320, height=500)
bill_title = Label(F2, text='Facture', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
scrol_y = Scrollbar(F2, orient=VERTICAL)
scrol_y.pack(side=RIGHT, fill=Y)
textarea = Text(F2, font='arial 15', yscrollcommand=scrol_y.set)
textarea.pack(fill=BOTH)
scrol_y.config(command=textarea.yview)

F3 = Frame(root, bg=bg_color, bd=15, relief=RIDGE)
F3.place(x=5, y=590, width=1270, height=120)

# --------------------------
btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='yellow', fg='red', width=10, command=total)
btn1.grid(row=0, column=0, padx=20, pady=10)

# --------------------------
btn2 = Button(F3, text='Facturer', font='arial 25 bold', padx=5, pady=5, bg='yellow', fg='red', width=10, command=facture)
btn2.grid(row=0, column=1, padx=10, pady=10)
# --------------------------
btn4 = Button(F3, text='Reinitialiser', font='arial 25 bold', padx=5, pady=5, bg='yellow', fg='red', width=12, command=reinitialiser)
btn4.grid(row=0, column=3, padx=10, pady=10)
# --------------------------
btn5 = Button(F3, text='Quitter', font='arial 25 bold', padx=5, pady=5, bg='yellow', fg='red', width=10, command=quitter)
btn5.grid(row=0, column=4, padx=10, pady=10)
root.mainloop()
