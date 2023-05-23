class peta:
    #Inisiasi sesuai set jarak yang sudah ditentukan
    def __init__(kotakab, jarak):
        kotakab.jarak = jarak
    
    #Fungsi untuk memanggil kota-kota yang terhubung
    def cabang(kotakab, val):
        return kotakab.jarak[val]
    
    def heur(kotakab, val):
        return Heur[val]
    
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
                #final_rute.append(start)
                #Membalik urutan kota di final rute agar menjadi urutan yang baik
                final_rute.reverse()
                #print('Rute A* Search: {}'.format(final_rute))
                for (n, j, weight) in kotakab.cabang(start):
                    if j == final_rute[0] :
                        return n
                    
                return final_rute
            
            #Menentukan kota yang akan diexpand selanjutnya
            for (n, j, weight) in kotakab.cabang(k):
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

Nodes = []
Heur = {}

def append(x, y, index):
    Nodes.append(index)
    Heur[index] = x + y
    
def find(start, finish) :
    graph = peta(Mgraph)
    next = graph.A_star(start, finish)
    return next
    
pos = []    
map = []
Mgraph = {}
    
def draw(sign) :
    map.append(sign)
    
def roadMap() :
    i  = 0
    for element in Nodes :
        temp = []
        
        #Search left branch
        i = map.index(element) - 1
        sign = 'l'
        distance_l = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_l += 1
            if(map[i] == '1') :
                sign = 'l'
            elif(map[i] == '2') :
                sign = 'u'
            elif(map[i] == '3') :
                sign = 'd'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                tpl = (1, map[i], distance_l*50)
                temp.append(tpl)
                #roadMap(map[i])
                sign = 'f'
        
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'f') : i = 0
    
        
        #Search top branch
        i = map.index(element) - 20
        sign = 'u'
        distance_u = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_u += 1
            if(map[i] == '1') :
                sign = 'l'
            elif(map[i] == '2') :
                sign = 'u'
            elif(map[i] == '3') :
                sign = 'r'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                tpl = (2, map[i], distance_u*50)
                temp.append(tpl)
                #roadMap(map[i])
                sign = 'f'
            
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0
        
        #Search right branch
        i = map.index(element) + 1
        sign = 'r'
        distance_r = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_r += 1
            if(map[i] == '1') :
                sign = 'd'
            elif(map[i] == '2') :
                sign = 'r'
            elif(map[i] == '3') :
                sign = 'r'
            elif(map[i] == '4') :
                sign = 'u'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                tpl = (3, map[i], distance_r*50)
                temp.append(tpl)
                sign = 'f'
            
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0

        #Search bottom branch
        i = map.index(element) + 20
        sign = 'd'
        distance_d = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_d += 1
            if(map[i] == '1') :
                sign = 'd'
            elif(map[i] == '2') :
                sign = 'r'
            elif(map[i] == '3') :
                sign = 'd'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                tpl = (4, map[i], distance_d*50)
                temp.append(tpl)
                sign = 'f'
            
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0
            
        Mgraph[element] = temp
     
def printG() :
    print("Graph untuk Menyatakan Actual Cost antar Node")
    for node, branch in Mgraph.items():
        print(node, branch)
    
    print("Nilai Heuristik Setiap Node")    
    for node, weight in Heur.items():
        print(node, weight)