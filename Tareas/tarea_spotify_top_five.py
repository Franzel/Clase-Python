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
"3:32","2:51","3:02","3:36","3:28","4:27","2:21","4:31","3:42","2:59","3:27","3:10"]

ed_sheeran_titulo = [
"Beautiful People","South of the Border","Cross Me","Take Me Back to London","Best Part of Me","I Don't Care","Antisocial","Remember the Name","Feels","Put It All on Me","Nothing on You","I Don't Want Your Money","1000 Nights","Way to Break My Heart","Blow"]
ed_sheeran_duracion = [
"3:17","3:24","3:26","3:09","4:03","3:39","2:41","3:27","2:30","3:17","3:20","3:24","3:32","3:10","3:29"]

bad_bunny_titulo = [
"Si veo a tu mamá","La difícil","Pero ya no","La santa","Yo perreo sola","Bichiyal","Soliá","La zona","Que malo","Vete","Ignorantes","A tu merced","Una vez","Safaera","25/8","Está cabrón ser yo","Puesto pa' guerrial","P FKN R","Hablamos mañana","<3"]
bad_bunny_duracion = [
"2:50","2:43","2:40","3:26","2:52","3:16","2:39","2:16","2:47","3:12","3:30","2:55","3:52","4:55","4:03","3:47","3:10","4:18","4:00","2:37"]

n_artistas  = len(artistas_nombre)
"""
for x in range(n_artistas):

    print("--------", artistas_nombre[x])
    #Ordenar por artista, album, cancion, duracion
    if artistas_nombre[x] == "Post Malone":
        n_canciones = len(post_malone_titulo)
        for i in range(n_canciones):
            print(albumes[x], " - ", post_malone_titulo[i], " - ", post_malone_duracion[i])
    if artistas_nombre[x] == "Billie Eilish":
        n_canciones = len(billie_eilish_album_titulo)
        for i in range(n_canciones):
            print(albumes[x], " - ", billie_eilish_album_titulo[i], " - ", billie_eilish_album_duracion[i])
    if artistas_nombre[x] == "Ariana Grande":
        n_canciones = len(ariana_grande_titulo)
        for i in range(n_canciones):
            print(albumes[x], " - ", ariana_grande_titulo[i], " - ", ariana_grande_duracion[i])
    if artistas_nombre[x] == "Ed Sheeran":
        n_canciones = len(ed_sheeran_titulo)
        for i in range(n_canciones):
            print(albumes[x], " - ", ed_sheeran_titulo[i], " - ", ed_sheeran_duracion[i])
    if artistas_nombre[x] == "Bad Bunny":
        n_canciones = len(bad_bunny_titulo)
        for i in range(n_canciones):
            print(albumes[x], " - ", bad_bunny_titulo[i], " - ", bad_bunny_duracion[i])


"""

artistas_nombre.sort()
print(artistas_nombre)

post_malone_duracion.sort()
print(post_malone_duracion)