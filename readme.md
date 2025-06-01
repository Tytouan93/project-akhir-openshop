# Proyek Akhir: OpenShop RESTful API

## Rating Submission Anda

Checklist ✅ Terpenuhi RESTful API dapat menyimpan data produk  
Checklist ✅ Terpenuhi RESTful API dapat menampilkan data produk  
Checklist ✅ Terpenuhi RESTful API dapat mengubah data produk  
Checklist ✅ Terpenuhi RESTful API dapat menghapus data produk  
Checklist ✅ Terpenuhi RESTful API dapat mencari data produk  

## Rekap Penilaian

Kriteria 1 : Advanced  
Kriteria 2 : Advanced  
Kriteria 3 : Advanced  
Kriteria 4 : Basic  
Kriteria 5 : Advanced  

**Nilai Akhir : 3.6 (Bintang 4)**

## Catatan Reviewer

Pada method `delete()` di `ProductDetailUpdateDeleteView`, sistem masih menggunakan **hard delete**:
```python
     def delete(self, request, pk):
     product = self.get_object(pk)
     if not product:
         return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

     product.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
```
Sementara itu, pada **model `Product` belum terdapat field `is_deleted`** untuk mendukung penerapan **soft delete**.
Akibatnya, kriteria penghapusan data belum sepenuhnya memenuhi standar `Advanced`.
Untuk meningkatkan menjadi **soft delete**, berikut saran perbaikannya:
- Tambahkan field `is_deleted = models.BooleanField(default=False)` pada model `Product`.
- Ganti `.delete()` menjadi update: `product.is_deleted = True; product.save()`.
- Sesuaikan semua query `Product.objects.all()` menjadi `Product.objects.filter(is_deleted=False)` agar hanya menampilkan produk yang belum dihapus.
Dengan ini, sistem akan lebih aman karena data tidak benar-benar terhapus dari basis data.
Semangat terus dalam meningkatkan kualitas API-mu! 💪

 ---
 ## 🚀 Cara Clone & Menjalankan Project Ini
 
 Ikuti langkah-langkah berikut untuk menyalin dan menjalankan project ini di lingkungan lokal Anda.
 
 ### 1. Clone Repository
 Jalankan perintah berikut di terminal:
 
 ```bash
 git clone https://github.com/username/project-akhir-openshop.git
 cd project-akhir-openshop
 ```
 
 > Gantilah `username` dengan nama akun GitHub Anda jika sudah melakukan fork.
 
 ### 2. Instalasi Dependensi
 Pastikan Anda menggunakan Python 3.10 atau versi yang direkomendasikan oleh Dicoding.
 
 ```bash
 pip install pipenv
 pipenv install
 ```
 
 ### 3. Aktivasi Virtual Environment
 
 ```bash
 pipenv shell
 ```
 
 ### 4. Migrasi Database
 
 ```bash
 python manage.py migrate
 ```
 
 ### 5. Menjalankan Server
 
 ```bash
 python manage.py runserver
 ```
 
 Server akan berjalan di `http://127.0.0.1:8000/`
 
 ---
 ✅ Sekarang Anda dapat mulai menggunakan RESTful API untuk fitur CRUD produk!
 
 Jika Anda ingin menguji dengan Postman, Anda bisa impor collection dari tugas submission Dicoding atau membuat request manual ke endpoint seperti:
 
 - `GET /products/`
 - `POST /products/`
 - `PUT /products/<uuid>/`
 - `DELETE /products/<uuid>/`

 
 ---
 ⚠️ **Catatan Penting**
 - Repository ini dibuat untuk keperluan **belajar pribadi** dan dokumentasi hasil pengerjaan proyek.
 - **DILARANG KERAS** melakukan **plagiarisme** atau **mengirimkan ulang** repository ini sebagai submission proyek akhir Anda di platform Dicoding.
 - Tindakan tersebut merupakan **pelanggaran terhadap peraturan Dicoding** dan dapat dikenakan **sanksi tegas**, termasuk diskualifikasi atau pemblokiran akun.
 - Jadilah pembelajar yang jujur dan bertanggung jawab.
 - Gunakan repository ini sebagai referensi untuk **belajar dan mengembangkan proyek versi Anda sendiri**.
