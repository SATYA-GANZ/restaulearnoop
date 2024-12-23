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

        pesan = input("Masukkan nama menu yang ingin dipesan : ")
        qty = int(input("Masukkan jumlah pesanan : "))
        for i in resto.menu:
            if pesan == i.nama:
                self.order.append(i)
                print("Pesanan berhasil ditambahkan")
                break
        r1 = r.randint(1, 15)
        self.order = []
        self.order.append(Kasir(r1, r1, "Done", 25000))
        self.order.append(Kasir(r1, 2, "Done", 30000))
        self.order.append(Kasir(3, 3, "Done", 10000))
        self.order.append(Kasir(4, 4, "Done", 15000))
        return self.order

resto = dapur("Default Nama", "Default Deskripsi", 0, "Default Category", False)
resto.create_menu()
resto.show_menu()
resto.stok_menu()
