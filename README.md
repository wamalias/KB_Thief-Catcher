# ETS_KBA_Thief-Catcher

## Group Member

| NRP        | Name                                   |
| ---------- | -------------------------------------- |
| 5025211006 | Wardatul Amalia Safitri                |
| 5025211029 | Melanie Sayyidina Sabrina Refman       |
| 5025211254 | Yusna Millaturrosyidah                 |

## Daftar Isi

- [Latar Belakang](#Latar-Belakang)
- [Metode yang digunakan](#Metode-yang-digunakan)
- [Cara Kerja](#Cara-Kerja)

## Latar Belakang
Alasan memilih topik ini adalah karena project ini menggunakan algoritma `A* Search` yang merupakan salah satu dari penerapan Informed Search, seperti yang telah dipelajari pada beberapa pertemuan sebelumnya. Maka dari itu kami mencoba untuk mengimplementasikannya kedalam game yang bernama Thief Catcher. Dimana dalam game ini nantinya akan dilakukan pencarian rute terpendek dari start ke goals dengan optimal.

## Metode yang digunakan
`A* Search` merupakan algoritma yang menggabungkan pendekatan heuristik dan actual cost untuk menemukan rute terpendek. Algoritma ini menggunakan nilai `f(n) = g(n) + h(n)`, di mana `g(n)` adalah biaya aktual dari node awal ke node n dan `h(n)` adalah heuristik dari node n ke node tujuan. Pada setiap langkah, algoritma akan memilih node berikutnya dengan nilai `f(n)` terkecil. Dalam game ini nilai `g(n)` diambil dari jumlah kotak antar kotak hint, sedangkan nilai `h(n)` diambil dari manhattan distance

## Cara Kerja 
Game ini dibuat untuk mencari jalan bagi detektif ke tempat dimana pencuri berada. Jadi player akan membantu detektif menemukan jalan yang benar dengan menelusuri jalur kotak-kotak yang ada pada layar.  Disni player juga dapat meminta hint untuk menemukan potongan jalur tercepat untuk dilalui. Jalur tercepat ditentukan dengan metode A*. Hint tersebut akan berisi sebuah teka-taki/riddle. Jika player dapat memecahkan teka-teki/riddle tersebut, maka player akan bisa mendapatkan hint. Jika player sudah menemukan jalur yang tepat, jalur yang dilalui user akan ditandai dengan warna hijau. Jika player sudah menemukan jalurnya sampai akhir dengan waktu di bawah 10 menit, maka player pun bisa menang.
