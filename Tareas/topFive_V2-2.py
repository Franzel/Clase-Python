#BASE DE DATOS
# Las listas de titulo y tiempo son del mismo tamao
post_malone_titulo = [
"Hollywood's Bleeding","Saint-Tropez","Enemies","Allergic","A Thousand Bad Times","Circles","Die for Me","On the Road","Take What You Want","I'm Gonna Be","Staring at the Sun","Sunflower","Internet","Goodbyes","Myself","I Know","Wow"]
post_malone_duracion = [
"2:36","2:30","3:16","2:36","3:41","3:34","4:05","3:38","3:49","3:20","2:48","2:38","2:03","2:56","2:38","2:21","2:29"]

billie_eilish_titulo = [
"!!!!!!","Bad Guy","Xanny","You Should See Me in a Crown","All the Good Girls Go to Hell","Wish You Were Gay","When the Party's Over","8","My Strange Addiction","Bury a Friend","Ilomilo","Listen Before I Go","I Love You","Goodbye"]
billie_eilish_duracion = [
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



artistas_nombre = ["Post Malone", "Billie Eilish", "Ariana Grande", "Ed Sheeran","Bad Bunny"]
albumes = ["Album Post Malone", "Album Billie Eilish", "Album Ariana Grande", "Album Ed Sheeran","Album Bad Bunny"]
titulos = [post_malone_titulo, billie_eilish_titulo, ariana_grande_titulo, ed_sheeran_titulo, bad_bunny_titulo]
duraciones = [post_malone_duracion, billie_eilish_duracion, ariana_grande_duracion, ed_sheeran_duracion, bad_bunny_duracion]
criterios = ["ORDEN DISCO", "ALFABETO", "DURACIONES"]

listaCanciones = []
topFive = []

#Funcion para ordenar segun criterio elegido
def sortList (lista, orden):
    if orden == "ALFABETO":
        lista.sort(key=lambda lista:lista[1])
    if orden == "DURACIONES":
        lista.sort(key=lambda lista:lista[2])
    return lista


for c in criterios:
    print("SEGÚN", c)
    for i in range(len(albumes)):               #repetiremos segun la lista de 'albumes'
        esteAlbumTemas = titulos[i]             #guardar todos los temas de este album
        esteAlbumDuraciones = duraciones[i]     #guardar todas las duraciones de este album

        for j in range(len(esteAlbumTemas)):                                    #para cada tema
            cancion = (albumes[i], esteAlbumTemas[j], esteAlbumDuraciones[j])   #guardamos info de album,nombre y duracion
            listaCanciones.append(cancion)                                      #guardamos en una lista nueva
        for j in range(len(listaCanciones)):
            listaCanciones = sortList(listaCanciones, c)                        #ordenamos la lista segun el criterio elegido
            if j == 0:
                topFive.append(listaCanciones[j])   #y guardamos el primer tema en la lista de topFive
        listaCanciones.clear()      #limpiamos para que no se acumule

    topFive = sortList(topFive, c)      #ordenamos ahora los 5 de la lista segun el criterio, nuevamente
    for i in range(len(topFive)):
        for j in topFive[i]:
            print(" -", j, end="")      #imprimimos uno a uno
        print("")
    topFive.clear()     #limpiamos para no acumular
