jarak = {
    'A': [('D', 250), ('E', 100), ('F', 450)],
    'B': [('C', 100)],
    'C': [('B', 100), ('G', 150)],
    'D': [('A', 250), ('E', 150), ('K', 200)],
    'E': [('A', 100),('D', 150) ],
    'F': [('A', 450), ('I', 350), ('J', 150), ('O', 350)],
    'G': [('C', 150), ('P', 250)],
    'H': [('L', 150), ('M', 100), ('I', 100)], 
    'I': [('F', 350), ('H', 100), ('J', 200)],
    'J': [('I', 200), ('F', 150), ('O', 200)],
    'K': [('D', 200), ('L', 100), ('S', 250)],
    'L': [('H', 150), ('K', 100)],
    'M': [('H', 100), ('N', 100), ('Q', 200)],
    'N': [('M', 100), ('Q', 100)],
    'O': [('F', 350), ('J', 200), ('P', 100), ('R', 100)],
    'P': [('O', 100), ('G', 250), ('U', 300)],
    'Q': [('M', 200), ('N', 100), ('T', 100)],
    'R': [('T', 500), ('U', 100), ('O', 100)],
    'S': [('K', 250)],
    'T': [('Q', 100), ('R', 500)],
    'U': [('R', 100), ('P', 300)]
} 

class peta:
    #Inisiasi sesuai set jarak yang sudah ditentukan
    def __init__(kotakab, jarak):
        kotakab.jarak = jarak
    
    #Fungsi untuk memanggil kota-kota yang terhubung
    def cabang(kotakab, val):
        return kotakab.jarak[val]
    
    def heur(kotakab, val):
        heuristik = {
            'A' : 700,
            'B' : 200,
            'C' : 100,
            'D' : 950,
            'E' : 800,
            'F' : 450,
            'G' : 250,
            'H' : 900,
            'I' : 800,
            'J' : 600,
            'K' : 1150,
            'L' : 1050,
            'M' : 1000,
            'N' : 900,
            'O' : 600,
            'P' : 500,
            'Q' : 1000,
            'R' : 700,
            'S' : 1400,
            'T' : 1100,
            'U' : 800
        }
        return heuristik[val]
    
    def A_star(kotakab, start, finish):
        #Set untuk menyimpan kota yang diexpand. Dimulai dari kota yang menjadi titik start
        rute = set([start])
        #Set untuk menyimpan kota yang dilalui
        past = set([]) 
        kota = {}   
        kota[start] = 0 
        parrent = {}
        parrent[start] = start #Inisialisasi parent start dengan dirinya sendiri
        
        while len(rute) > 0:
            #Inisialisasi variabel k sebelum menyimpan kota yang dipilih
            k = None
            
            #Memilih kota mana yang akan dipilih dari kota-kota yang diexpand
            for i in rute:
                #Perbandingannya menggunakan fungsi heuristik + jarak untuk setiap kota dari titik awal yang sudah dilalui
                if k == None or kota[i] + kotakab.heur(i) < kota[k] + kotakab.heur(k):
                    k = i
            
            #Jika tidak ada kota yang bisa dipilih   
            if k == None:
                print('Rute tidak tersedia')
                return None
            
            #jika k sama dengan kota tujuan
            if k == finish:
                #Membuat list untuk menyimpan final rute
                final_rute = []
                
                #Menabahkan kota yang sudah dilalui ke final rute dengan urutan terbalik
                while parrent[k] != k:
                    final_rute.append(k)
                    k = parrent[k]
                
                #Menambahkan kota titik awal ke final rute
                final_rute.append(start)
                #Membalik urutan kota di final rute agar menjadi urutan yang baik
                final_rute.reverse()
                print('Rute A* Search: {}'.format(final_rute))
                return final_rute
            
            #Menentukan kota yang akan diexpand selanjutnya
            for (j, weight) in kotakab.cabang(k):
                if j not in rute and j not in past:
                    rute.add(j)
                    parrent[j] = k
                    kota[j] = kota[k] + weight #Menghitung total jarak yang sudah dilalui dari kota awal hingga kota j
                else:
                    #Update total jarak dengan nilai yang lebih kecil (jika ada)
                    if kota[j] > kota[k] + weight:
                        kota[j] = kota[k] + weight
                        parrent[j] = k #Update parent
                        if j in past:
                            past.remove(j)
                            rute.add(j)
            
            #Menghapus kota yang dilalui dari kota yang diexpand agar tidak dipilih kembali
            rute.remove(k)
            #Menambahkan kota yang sudah dilalui ke set past
            past.add(k) 
        
        #Jika tidak ada rute yang memenuhi
        print('Rute tidak tesedia')
        return None
    
class Branch (object) :  
    def __init__(self, index, heur):
        self.index = index
        self.heur = heur
        Nodes.append(self)

Nodes = []

def append(x, y, index):
    Branch(index, x+y)
    
    #for Node in Nodes :
    #    print(Node.index, Node.heur)
    #print("\n\n")
    
def check(path) :
    start = '#'
    for branch in Nodes :
        if(branch.index == path) :
            start = branch
            
    print(start.index, start.heur)
    
def find() :
    graph = peta(jarak)
    graph.A_star('S', 'C')