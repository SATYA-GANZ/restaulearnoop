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
    def __init__(self, orderID, no_meja, status, total, daftarMenu):
        self.orderID = orderID
        self.no_meja = no_meja
        self.status = status
        self.total = total
        self.order = []
        self.daftarMenu = daftarMenu
    
    def create_order(self):
     no_meja = int(input("Masukkan nomor meja: "))\

    # Inisialisasi total dan list pesanan
     total = 0
     pesankan = []

     while True:
        print("menu yang tersediia")
        for i in self.daftarMenu:
            if i.available:
                print(f"menu  : {i.nama}, harga :  {i.harga}")
          
        pesanan  = input("masukkan nama makanan yang ingin dipesan : ")
        jumlah = int(input("masukkan jumlah makanan"))
          
        dipesan = None
        for i in self.daftarMenu:
            if pesanan == i.nama and i.available:
                dipesan = i
            elif dipesan == False:
                print("makanan tidak ditemukan")
        if jumlah <= 0:
            print("tidak jadi memesan")
            continue
              
        subtotal = dipesan.harga * jumlah
        total += subtotal
        pesankan.append({
            "menu": dipesan.nama,
            "jumlah": jumlah,
            "subtotal": subtotal
        })
        
        lanjut = input("Apakah ingin memesan lagi? (ya/tidak): ")
        if lanjut.lower() != "ya":
            break
        
     if pesanan:
        self.orderID = r.randint(1000, 9999)
        self.no_meja = no_meja
        self.status = "Proses"
        self.total = total
        self.order = pesankan
    
        print("\n=== Ringkasan Pesanan ===")
        print(f"Order ID: {self.orderID}")
        print(f"Nomor Meja: {self.no_meja}")
        print("\nMenu yang dipesan:")
        for item in self.order:
            print(f"- {item['menu']} (x{item['jumlah']}) - Rp {item['subtotal']}")
        print(f"\nTotal: Rp {self.total}")
        return self.total,self.orderID,self.no_meja,self.status
        exit()
     else:
        print("Tidak ada item yang dipesan!")

    def strukBayar(self):
        return self.total,self.orderID,self.no_meja,self.status

class Payment:
    def __init__(self, orderID, total, status, no_meja):
        self.orderID = orderID
        self.total = total
        self.status = status
        self.no_meja = no_meja

    def payment_process(self):
        print("=== Pembayaran ===")
        print(f"memproses pembayaran order-ID - {self.orderID}\ndengan nomor meja {self.no_meja} \ndengan total pembayaran Rp {self.total}")
        bayar = int(input("Masukkan nominal pembayaran: "))
        if bayar > self.total:
            kembalian = bayar - self.total
            print(f"kembalian sebesar {kembalian}")
            self.status = "Paid"
        elif bayar == self.total:
            print("Pembayaran berhasil")
            self.status = "Paid"
        
        print("Rincian Pembayaran")
        print(f"Order ID: {self.orderID}\n meja: {self.no_meja}\n status: {self.status}\n total: {self.total}")
def main():
    print("=== Aplikasi Kasir ===")
    resto = dapur("Default Nama", "Default Deskripsi", 0, "Default Category", False)
    daftar_menu = resto.create_menu()
    kasir = Kasir(0, 0, "Default Status", 0, daftar_menu)
    resto.create_menu()
    #resto.show_menu()
    kasir.create_order()

    total, orderID, no_meja, status = kasir.strukBayar()
    payment = Payment(orderID, total, status, no_meja)
    payment.payment_process()
if __name__ == "__main__":
    main()
