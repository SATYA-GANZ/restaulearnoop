import random as r

class dapur:
    def __init__(self, nama, deskripsi, harga, category, available):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.category = category
        self.available = available
        self.menu = []
    
    def create_menu(self):
        self.menu = []
        self.menu.append(dapur("Ayam Goreng", "Ayam goreng tepung", 10000, "Makanan", True))
        self.menu.append(dapur("Nasi Goreng", "Nasi goreng biasa", 15000, "Makanan", True))
        self.menu.append(dapur("Es Teh", "Es teh manis", 5000, "Minuman", True))
        self.menu.append(dapur("Es Jeruk", "Es jeruk manis", 6000, "Minuman", True))
        return self.menu
    
    def update_menu(self):
        up = input("Masukkan nama menu yang ingin diubah: ")

        for i in self.menu:
            if i.nama == up:
                i.nama = input("masukkan nama baru : ")
                i.deskripsi = input("masukkan deskripsi baru : ")
                i.harga = input("harga : ")
                i.category = input("category : ")
                i.available = input("available : ") if i.available == True else False
                print("Menu berhasil diubah")
                self.show_menu()
                break

    def delete_menu(self):
        delMenu = input("masukkan nama yang ingin dihapus : ")

        for b in self.menu:
            if b.nama == delMenu:
                self.menu.remove(b)
                print("Menu berhasil dihapus")
                self.show_menu()

    def stok_menu(self):
        stok = input("masukkan nama menu yang ingin diubah stoknya : ")
        for i in self.menu:
            if stok == i.nama:
             loc = input("mau diubah jadi available atau tidak? : ")

             if loc == "ya":
                i.available = True
                print("Stok berhasil diubah")
                self.show_menu()
             else:
                i.available = False
                self.show_menu()

    def show_menu(self):
        for i in self.menu:
            print(f"{i.nama} - {i.deskripsi} - {i.harga} - {i.category} - {i.available}")

class Kasir:
    def __init__(self, orderID, no_meja, status, total):
        self.orderID = orderID
        self.no_meja = no_meja
        self.status = status
        self.total = total
        self.order = []
    
    def create_order(self):
    no_meja = int(input("Masukkan nomor meja: "))
    
    # Inisialisasi total dan list pesanan
    total = 0
    pesanan = []
    
    while True:
            print("menu yang tersediia")
            for i in self.daftar_menu:
                if i.available:
                print(f"menu  : {i.nama}, harga :  {i.harga}")
              
              pesanan  = input("masukkan nama makanan yang ingin dipesan : ")
              jumlah = int(input("masukkan jumlah makanan"))
              
              dipesan = None
              for i in self.daftar_menu:
                  if pesananan == i.nama and i.available:
                      i.nama = dipesan
                  elif dipesan is None:
                      print("makanan tidak ditemukan")
              if jumlah <= 0:
                  print("tidak jadi memesan")
                  continue
              except ValueError:
                  print("kesalahan value program restart")
                  continue
                  
            subtotal = dipesan.harga * jumlah
            total = subtotal
            pesanan.append({
               "menu dipesan":dipesan.nama,
               "harga":harga,
               "total":total
            })
            
        if pesanan:
        self.orderID = order_id
        self.no_meja = no_meja
        self.status = "Proses"
        self.total = total
        self.order = pesanan
        
        print("\n=== Ringkasan Pesanan ===")
        print(f"Order ID: {self.orderID}")
        print(f"Nomor Meja: {self.no_meja}")
        print("\nMenu yang dipesan:")
        for item in self.order:
            print(f"- {item['menu']} (x{item['jumlah']}) - Rp {item['subtotal']}")
        print(f"\nTotal: Rp {self.total}")
        return True
    else:
        print("Tidak ada item yang dipesan!")
        return False

resto = dapur("Default Nama", "Default Deskripsi", 0, "Default Category", False)
resto.create_menu()
resto.show_menu()
resto.stok_menu()
