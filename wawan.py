from fpdf import FPDF
import os

cond = True
def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=20)
    # Settingan font dan size disini
    print("""
    ##########################
    ### Ez Data Wawancara  ###
    ##########################
    """)

    NimAnda = int(input("Masukkan nim kamu : "))
    Nama    = str(input("Nama              : "))
    Nim     = int(input("NIM               : "))
    Jurusan = str(input("Jurusan           : "))
    Unik    = str(input("Keunikan          : "))
    Fi      = str(input("First Impression  : "))
    # Input datanya

    pdf.multi_cell(200,10,txt = "Nama : %s" %Nama)
    pdf.multi_cell(200,10,txt = "Nim : %d" %Nim)
    pdf.multi_cell(200,10,txt = "Jurusan : %s" %Jurusan)
    pdf.multi_cell(200,10,txt = "Keunikan : %s" %Unik)
    pdf.multi_cell(200,10,txt = "First Impression : %s" %Fi)
    # Prosesnya

    out = str(NimAnda)+"_"+str(Nim)+".pdf"
    pdf.output(out)
    # Hasilnya
    print("Proses telah berhasil ! ")
    print("Apakah anda mau mengulanginya lagi?")
    opt = str(input("Yes/Apapun : "))
    if opt.upper == "YES":
        True
    else:
        False
    return opt

main()

if cond == True:
    os.system('cls')
    main()
else:
    os.system('cls')


