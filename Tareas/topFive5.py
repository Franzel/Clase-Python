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

#
def get_original_indices(lista):
    index_original = sorted(range(len(lista)), key=lambda k:lista[k])
    return index_original

case = ["disco", "alfa", "dura"]

for c in case:
    #crear las listas que guardaran los top5, segun cada caso
    top5_albumes = []
    top5_temas = []
    top5_duraciones = []

    # asignar temas y duraciones para cada disco, al iterar
    for i in range(len(albumes)):
        if i == 0:
            temas_originales = post_malone_titulo
            duraciones_originales = post_malone_duracion
        if i == 1:
            temas_originales = billie_eilish_album_titulo
            duraciones_originales = billie_eilish_album_duracion
        if i == 2:
            temas_originales = ariana_grande_titulo
            duraciones_originales = ariana_grande_duracion
        if i == 3:
            temas_originales = ed_sheeran_titulo
            duraciones_originales = ed_sheeran_duracion
        if i == 4:
            temas_originales = bad_bunny_titulo
            duraciones_originales = bad_bunny_duracion

        this_album = albumes[i]
        # CASO ORDENAR POR ORDEN DISCO
        if c=="disco":
            for j in range(len(temas_originales)):
                if j==0:
                    top5_albumes.append(this_album)
                    top5_temas.append(temas_originales[j])
                    top5_duraciones.append(duraciones_originales[j])

        # CASO ORDENAR POR ALFABETO
        if c=="alfa":
            temas_ordenados = sorted(temas_originales)
            indices_originales = get_original_indices(temas_originales)
            duraciones_ordenadas = []
            for j in range(len(indices_originales)):
                duraciones_ordenadas.append(duraciones_originales[indices_originales[j]])
                #print(this_album, " - ", temas_ordenados[j], " - ", duraciones_ordenadas[j])
                if j==0:
                    top5_albumes.append(this_album)
                    top5_temas.append(temas_ordenados[j])
                    top5_duraciones.append(duraciones_ordenadas[j])

        # CASO ORDENAR POR DURACION
        if c=="dura":
            temas_ordenados = []
            indices_originales = get_original_indices(duraciones_originales)
            duraciones_ordenadas = sorted(duraciones_originales)

            for j in range(len(indices_originales)):
                temas_ordenados.append(temas_originales[indices_originales[j]])
                #print(this_album, " - ", temas_ordenados[j], " - ", duraciones_ordenadas[j])
                if j==0:
                    top5_albumes.append(this_album)
                    top5_temas.append(temas_ordenados[j])
                    top5_duraciones.append(duraciones_ordenadas[j])

 #IMPRIMIR A LA CONSOLA
    if c == "alfa":
        print("----------------ALFABETICAMENTE")
        top5_temas_orden_final = sorted(top5_temas)
        top5_indices_originales = get_original_indices(top5_temas)
        top5_duraciones_orden_final = []
        top5_albumes_orden_final = []
        for i in range(len(top5_temas)):
            top5_albumes_orden_final.append(top5_albumes[top5_indices_originales[i]])
            top5_duraciones_orden_final.append(top5_duraciones[top5_indices_originales[i]])
            print(top5_albumes_orden_final[i], " - ",top5_temas_orden_final[i], " - ",top5_duraciones_orden_final[i])

    if c == "dura":
        print("----------------POR DURACION")
        top5_duraciones_orden_final = sorted(top5_duraciones)
        top5_indices_originales = get_original_indices(top5_duraciones)
        top5_temas_orden_final = []
        top5_albumes_orden_final = []
        for i in range(len(top5_temas)):
            top5_albumes_orden_final.append(top5_albumes[top5_indices_originales[i]])
            top5_temas_orden_final.append(top5_temas[top5_indices_originales[i]])
            print(top5_albumes_orden_final[i], " - ", top5_temas_orden_final[i], " - ", top5_duraciones_orden_final[i])
    if c == "disco":
        print("----------------POR ORDEN DISCO")
        for i in range(len(top5_temas)):
            print(top5_albumes[i], " - ", top5_temas[i], " - ", top5_duraciones[i])
