Comandos de git:


CLONAR UN REPO, solo ingreso al lugar de mi pc donde quiero clonar el repo y allí en la terminal uso:

git clone git clone https://github.com/tu-usuario/tu-repo.git  (El link de mi repositorio que quiero descargar)
ls     ---> para comprobar que se descargó

git remote -v       ---> Para comprobar la conexión remota a ese repositorio






UNA VEZ CLONADO, DEBO CONFIRMAR BIEN Y REVISAR QUE ESTOY EN EL USUARIO QUE QUIERO PARA SUBIR MIS CAMBIOS A GIT

git config --list    ---> PAra ver qué usuario y correo hay en mi git



SI EL NOMBRE O CORREO NO SON LOS QUE DESEO, PUEDO CAMBIARLOS ASÍ:

git config user.name "Tu Nombre" ---> Para cambiar el nombre o crearlo
git config user.email "tu-correo@ejemplo.com"   ---> Para cambiar el correo, o crearlo



SI ME ANDA PIDIENDO EL PIN CADA VEZ QUE REQUIERA UN CAMBIO:
git config credential.helper store  ---> Se asegura de guardar el pin


git add .
git commit -m"mensaje cualquiera"
git push


REPOR DEL PROFE: https://github.com/orimarselasirg/buclesAndFunction/blob/main/M1S2/Ejercicios_Funciones_avanzadas.md 
