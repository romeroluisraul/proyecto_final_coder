Integrante:

- Luis Raul Romero Avila

Información importante:

Las plantillas toman fuentes y estilos css de la nube. Por tanto, para la correcta observación de la página debe estar conectado a internet.

Video funcionamiento:

https://youtu.be/5RBgB2EFo4k

Página:
https://romeroluisraul.pythonanywhere.com

Acceso a la base de datos

    super usuario: romeroluisraul
    contraseña: #### contactar por mail ####


¿En qué consiste la página web?

La idea general del proyecto es un blog donde el autor comenta ciertas observaciones curiosas de sus viajes en ruta.

El blog tiene una home, donde se lista un breve resumen de cada uno de los posteos. Cada posteo tiene una fecha de liberación, a partir del cual pasa a estar en estado disponible para lectura. También a partir de esa fecha, los lectores podrán comentar cada una de las publicaciones e interactuar entre ellos en la sección de comentarios de cada publicación.

Para visualizar los contenidos se puede, o bien visualizar la totalidad de las publicaciones en la home, o bien filtrar los contenidos por medio de los tags o etiquetas de cada publicación. Este filtro se encuentra a lado derecho de la pagina web. Se ha programado de forma tal que cuando se cargan nuevas publicaciones, se actualicen los filtros disponibles y se resalten, pudiendo también filtrar las nuevas publicaciones.

El blog tambien tiene un sobre mí, que habla del autor y qué es lo que hace más allá de los post.

El blog implementa también registro, logeo y deslogeo de usuarios. Los lectores invitados, es decir, los lectores sin usuario registrado, pueden leer todas las publicaciones pero no pueden comentar. Solo los usuarios registrados y logeados pueden realizar comentarios. Los superusuarios pueden además crear nuevas publicaciones.

Rutas de la pagina web:

- ../about/ : que detalla la ocupación y los intereses del autor.

- ../home/ : la 'home' del blog.

Rutas de la aplicación contenido:

- ../posts/visualizar/<title>/ : la ruta de cada una de las publicaciones. El modelo tiene valores únicos de <title> por lo que no hay ambigüedad.

- ../posts/visualizar/<title>/comments : la ruta de la página de comentarios asociada a la publicación de título <title>.

- ../posts/busqueda/<tag>/ : la ruta del buscador de los posts con etiqueta <tag>

- ../posts/crear/nuevo_post/ : la ruta del formulario para crear un nuevo post. Este formulario solo esta disponible para superusuarios. En otro caso, lleva a login.

Rutas de la aplicacion autenticación:

- ../authentication/login/ : la ruta para el formulario de login. Si ya se encuentra un usuario logueado, permite hacer logout y acceder con otro usuario.

- ../authentication/logout/<destino> : la ruta para desloguearse. Si <destino> es un string vacío, redirige a la última página de contenido visitada, es decir, la home, algun post en particular, los comentarios, el buscador por tags o la pagina de información del autor. Caso contrario, redirige al destino indicado.


- ../authentication/user/bienvenido/ : una ruta implementada para dar un mensaje de bienvenida tras hacer login.

- ../authentication/singup/ : la ruta para ir al formulario de registro de nuevo usuario. Si ya se encuentra un usuario logueado, permite hacer logout y registrar un nuevo usuario.



------
