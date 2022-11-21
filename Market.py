import os
import time

data_product = {
   1: "Laptop",
   2: "Mouse   ",
   3: "Keyboard",
   4: "Mousepad", 
   5: "Charger",
}
daftar_harga = {
   1: 1000000,
   2: 150000,
   3: 250000,
   4: 100000,
   5: 50000
}

dict_trx = {}
metode_pembayaran = {
   1: "Transfer Bank",
   2: "E-Wallet",
   3: "Cash On Delivery",
   4: "Kartu Kredit"
}

def loading():
    for i in range(3):
        os.system('cls')
        print('loading.')
        time.sleep(0.3)
        os.system('cls')
        print('loading..')
        time.sleep(0.3)
        os.system('cls')
        print('loading')
        time.sleep(0.3)
        os.system('cls')

def bio():
   print("=====================================================")
   nama_penerima     = input("Nama Penerima     : ")
   alamat_penerima   = input("Alamat Penerima   : ")
   nomor_telepon     = input("No Hp             : ")
   kurir_penerima    = input("Ekspedisi         : ")
   print("=====================================================")
   dict_trx = {
      "Nama penerima":nama_penerima,
      "Alamat penerima":alamat_penerima,
      "Nomor telepon":nomor_telepon,
      "Kurir penerima":kurir_penerima,
      "Product id":data_product,
   }
   print("=====================================================")
   if len (dict_trx) > 0 :
         payment(dict_trx)
   else:
      print(" Product tidak tersedia")

def payment(dict_trx):
   print("==========================Metode Pembayaran==========================")
   for i in metode_pembayaran:
      print("id :", i, "\t Metode Pembayaran : ", metode_pembayaran[i])
   pilih_metode = int(input( "Pilih Pembayaran : "))
   loading()
   os.system('cls')
   if pilih_metode in metode_pembayaran :
      print("\t\t==========List Product=========\n")
      print("Nama Penerima :  ", dict_trx["Nama penerima"])
      print("Alamat Penerima :  ", dict_trx["Alamat penerima"])
      print("Nomor telepon :  ", dict_trx["Nomor telepon"])
      print("Kurir Penerima :  ", dict_trx["Kurir penerima"])
      print("Product : ", data_product[pilih_id])
      print("Harga : ", daftar_harga[pilih_id])
      print("Metode Pembayaran : ", metode_pembayaran[pilih_metode])
      print("\n\n\t\t==========Pembayaran=========\n")
      if metode_pembayaran[pilih_metode] == "Transfer Bank":
         tf()
      elif metode_pembayaran[pilih_metode] == "E-Wallet":
         ewal()
      elif metode_pembayaran[pilih_metode] == "Cash On Delivery":
         cod()
      elif metode_pembayaran[pilih_metode] == "Kartu Kredit":
         kk()
   else:
      print("Metode pembayaran tidak tersedia")

def tf():
   print("\t\tTransfer Bank\n")
   inputPass()
   
def ewal():
   print("\t\tE-Wallet\n")
   print("1. Dana")
   print("2. Shopee Pay")
   print("3. OVO")
   print("4. Link Aja")
   menu = int(input("Pilih E-Wallet: "))
   password = 123412
   chance = 3
   if menu == 1:
      print("\t\tDana\n")
      inputPass()
   elif menu == 2:
      print("\t\tShopee Pay\n")
      inputPass()
   elif menu == 3:
      print("\t\tOVO\n")
      inputPass()
   elif menu == 4:
      print("\t\tLink Aja\n")
      inputPass()

def cod():
   loc = input("Konfirmasi detail lokasi CoD: ")
   print("Barang sedang dalam perjalanan!")

def kk():
   print("\t\tKartu Kredit\n")
   inputPass()

def inputPass():
   password = 123412
   chance = 3
   while chance >= 0:
      pw = int(input("Masukan password: "))
      if pw == password:
         print("Pembayaran berhasil!")
         break
      else:
         print("Password salah!")

os.system('cls')
print("\t =============================")
print("\t Selamat Datang di Nalz Store")
print("\t =============================")
time.sleep(1)
loading()
os.system('cls')
print("\t\t\t==========List Product=========")
for i in data_product:
   print (">", i, "\t Nama Product : ",
      data_product[i], "\t \t |Harga Product : ", daftar_harga[i])
pilih_id = int(input("Pilih Product : "))
if pilih_id in data_product : 
   pilih_beli = input("Apakah Anda yakin ? (Y/N): ")
   if pilih_beli == "y" or pilih_beli == "Y" : 
      bio()
   else : 
      pass