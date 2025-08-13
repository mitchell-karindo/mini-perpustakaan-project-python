class perpustakaan:
  #isi/daftar buku
    def __init__(self):
        self.books = {
            "dia adalah ibuku" : True,
            "cepat ipa" : True,
            "matematika" : False,
            "olahraga" : True
        }
        self.members = []
        self.borrowed_books = {}
   #mendisplay buku yang tersedia
    def display_books(self):
        print("\nbuku yang tersedia:")
        for book, available in self.books.items():
            status = "tersedia" if available else "tidak tersedia"
            print(f"{book}: {status}")
        print()
    #perintah meminjam buku dan perintah kembali jika bukan anggota
    def borrow_book(self, member_name):
        if member_name not in self.members:
            print("kamu bukan anggota,silahkan daftar yaa")
            return
        self.display_books()
        book_name = input("masukkan judul yang mau kamu pinjam: ").strip()
        if book_name in self.books and self.books[book_name]:
            self.books[book_name] = False
            self.borrowed_books[book_name] = member_name
            print("kamu telah meminjam buku,harap dikembalikan sesuai waktu" )
        else:
            print("maaf,buku ini sedang dipinjam. ")
     #perintah mengembalikan buku
    def return_book(self, member_name):
        book_name = input("masukkan judul buku yang ingin dikembalikan").strip()
        if book_name in self.borrowed_books and self.borrowed_books[book_name] == member_name:
            self.books[book_name] = True
            del self.borrowed_books[book_name]
            print(f"terimakasih telah mengembalikan buku '{book_name}' . ")
        else:
            print("kamu tidak pinjam buku itu. ")

    def check_return_status(self, member_name):
        print("buku yang kamu pinjam: ")
        borrowed_by_member = [book for book , member in self.borrowed_books.items() if member == member_name]
        if borrowed_by_member:
            for book in borrowed_by_member:
                print(f'. {book}')
        else:
            print("kamu belum meminjam buku satupun. ")
        print()
      #perintah menambahkan anggota
    def add_member(self):
        name = input("masukkan nama kamu untuk mendaftar sebagai anggota: ").strip()
        if name not in self.members:
            self.members.append(name)
            print(f"selamat datang di perpustakaan, {name}!")
        else:
            print("kamu sudah menjadi anggota")

def main():
    library = perpustakaan()
    print("halo, selamat datang di perpustakaan")

    while True:
        print("\nmenu: ")
        print("1. daftar buku")
        print("2. pinjam buku")
        print("3. kembalikan buku")
        print("4. buku yang saya pinjam")
        print("5. registrasi anggota")
        print("6. keluar")

        choice = input("pilih menu: ").strip()

        if choice == '1' :
            library.display_books()
        elif choice == '2' :
            name = input("masukkan nama kamu: ").strip()
            library.borrow_book(name)
        elif choice == '3' :
            name = input("masukkan nama kamu: ").strip()
            library.return_book(name)
        elif choice == '4' :
            name = input("masukkan nama kamu: ").strip()
            library.check_return_status(name)
        elif choice == '5' :
            library.add_member()
        elif choice == '6' :
            print("terimakasih, bye bye !")
            break
        else:
            print("pilihan tidak valid,coba lagi.")

if __name__ == "__main__":
    main()


