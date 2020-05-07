#BASE DE DATOS

artistas_nombre = ["Post Malone", "Billie Eilish", "Ariana Grande", "Ed Sheeran","Bad Bunny"]
albumes = ["Album Post Malone", "Album Billie Eilish", "Album Ariana Grande", "Album Ed Sheeran","Album Bad Bunny"]

# Las listas de titulo y tiempo son del mismo tamao
post_malone_titulo = [
"Hollywood's Bleeding","Saint-Tropez","Enemies","Allergic","A Thousand Bad Times","Circles","Die for Me","On the Road","Take What You Want","I'm Gonna Be","Staring at the Sun","Sunflower","Internet","Goodbyes","Myself","I Know","Wow"]
post_malone_duracion = [
"2:36","2:30","3:16","2:36","3:41","3:34","4:05","3:38","3:49","3:20","2:48","2:38","2:03","2:56","2:38","2:21","2:29"]

billie_eilish_album_titulo = [
"!!!!!!","Bad Guy","Xanny","You Should See Me in a Crown","All the Good Girls Go to Hell","Wish You Were Gay","When the Party's Over","8","My Strange Addiction","Bury a Friend","Ilomilo","Listen Before I Go","I Love You","Goodbye"]
billie_eilish_album_duracion = [
"0:14","3:14","4:04","3:01","2:49","3:42","3:16","2:53","3:00","3:13","2:36","4:00","4:52","1:59"]

ariana_grande_titulo = [
"Imagine","Needy","NASA","Bloodline","Fake Smile","Make Up","Ghostin","In My Head","7 Rings","Thank U, Next","Break Up With Your Girlfriend, I'm Bored"]
ariana_grande_duracion = [
"3:32","2:51","3:02","3:36","3:28","4:27","2:21","4:31","3:42","2:59","3:27"]

ed_sheeran_titulo = [
"Beautiful People","South of the Border","Cross Me","Take Me Back to London","Best Part of Me","I Don't Care","Antisocial","Remember the Name","Feels","Put It All on Me","Nothing on You","I Don't Want Your Money","1000 Nights","Way to Break My Heart","Blow"]
ed_sheeran_duracion = [
"3:17","3:24","3:26","3:09","4:03","3:39","2:41","3:27","2:30","3:17","3:20","3:24","3:32","3:10","3:29"]

bad_bunny_titulo = [
"Si veo a tu mamá","La difícil","Pero ya no","La santa","Yo perreo sola","Bichiyal","Soliá","La zona","Que malo","Vete","Ignorantes","A tu merced","Una vez","Safaera","25/8","Está cabrón ser yo","Puesto pa' guerrial","P FKN R","Hablamos mañana","<3"]
bad_bunny_duracion = [
"2:50","2:43","2:40","3:26","2:52","3:16","2:39","2:16","2:47","3:12","3:30","2:55","3:52","4:55","4:03","3:47","3:10","4:18","4:00","2:37"]




#Funcion para ordenar la lista y recuperar el indice de cada item en la lista original
#el parámetro ¨criterio¨ determina si la funcion entrega la lista ordenada o entrega los indices
def ordenar_lista(lista, indice):
    lista_ordenada = sorted(lista)
    index_original = sorted(range(len(lista)), key=lambda k:lista[k])
    if indice==True:
        return index_original
    else:
        return lista_ordenada


#Creamos un array para los tres tipos de orden que usaremos
ordenar_por = {"orden disco", "orden alfabetico", "orden duraciones"}

for caso in ordenar_por:
    print("--------------------------------------------")
    print("ORENADAS SEGUN: ", caso.upper())
    print("--------------------------------------------")

    #asignar artista y duracion a variables comunes, iterando en la lista "artistas nombres"
    for x in range(len(artistas_nombre)):
        if x==0:
            artista = post_malone_titulo
            duraciones = post_malone_duracion
        if x==1:
            artista = billie_eilish_album_titulo
            duraciones = billie_eilish_album_duracion
        if x==2:
            artista = ariana_grande_titulo
            duraciones = ariana_grande_duracion
        if x==3:
            artista = ed_sheeran_titulo
            duraciones = ed_sheeran_duracion
        if x==4:
            artista = bad_bunny_titulo
            duraciones = bad_bunny_duracion

        #imprimir informacion, cada caso a la vez
        if caso == "orden disco":
            print("ARTISTA: ", artistas_nombre[x].upper(), " ----------")
            for i in range(len(artista)):
                print(albumes[x], end=" - ")
                print(artista[i], end=" - ")
                print(duraciones[i])
        if caso == "orden alfabetico":
            print("ARTISTA: ", artistas_nombre[x].upper(), " ----------")
            canciones_ordenadas = ordenar_lista(artista, False)
            indice_original = ordenar_lista(artista, True)
            for i in range(len(artista)):
                print(albumes[x], end=" - ")
                print(canciones_ordenadas[i], end=" - ")
                print(duraciones[indice_original[i]])
        if caso == "orden duraciones":
            print("ARTISTA: ", artistas_nombre[x].upper(), " ----------")
            duraciones_ordenadas = ordenar_lista(duraciones, False)
            indice_original = ordenar_lista(duraciones, True)
            for i in range(len(artista)):
                print(albumes[x], end=" - ")
                print(artista[indice_original[i]], end=" - ")
                print(duraciones_ordenadas[i])
        print(" ")
