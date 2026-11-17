Declaración de uso de inteligencia artificial

Herramienta utilizada: GitHub Copilot.

Uso general: La IA se usó como apoyo en el desarrollo del proyecto. Se empleó para mejorar el diseño de las plantillas, implementar validaciones y reorganizar la estructura de archivos.

Prompt 1: "Quiero reorganizar las plantillas de mi proyecto. Crea un archivo base.html con lo común de todas las páginas (head, navegación, footer) y un bloque para el contenido, y haz que las demás plantillas lo extiendan. Mueve todos los estilos a estilo.css, elimina referencias a Bootstrap y mantén el diseño de tienda de cómics. No toques modelos ni vistas, y no ejecutes pruebas ni migraciones".

El código se veía desordenado al haber estilos dentro de las plantillas, todas compartían el mismo header y footer, por lo cual, con la creación del archivo base y la reestructuración hecha por la IA sin cambiar el contenido íntegro, el código se ve más legible y entendible.

Prompt 2: "Quiero que el código de cada reserva se genere solo y que el usuario no tenga que escribirlo. Antes de hacer cambios, dame una idea de cómo podría ser el formato del código. Tiene que tener máximo 10 caracteres porque así está en mi modelo y no puede repetirse entre reservas".

Antes de esta automatización, el código se ingresaba manualmente, lo que no era muy eficiente. La IA sugirió usar un módulo llamado "secrets", que comúnmente se usa para contraseñas, lo implementé de manera que generara un código hexadecimal de forma automática en mayúsculas cada vez que se realiza una reserva.

Prompt 3: "Ayúdame a mejorar el formato del RUT en el formulario. Primero, que solo acepte números y que tenga entre 8 y 9 caracteres, como un RUT chileno real. Si el usuario ingresa algo distinto, que el formulario muestre un mensaje de error claro y no guarde la reserva. Segundo, que en el comprobante el RUT se vea con puntos y guion, por ejemplo, si ingreso 123456789, aparezca como 12.345.678-9. Avísame si conviene usar CharField o IntegerField para este campo y por qué".

Fue muy útil para validar el formato del RUT, había confusión al inicio entre si usar CharField o IntegerField para representarlo. Finalmente, se optó por Charfield, porque algunos RUT ocupan la letra K y la IA ocupó RegexValidator para que el formulario cumpliera con el formato correcto. Luego se implementaron más validaciones, como no solo usar números, sino también usar la letra K como dígito al final.

Prompt 4: "Quiero que mi vista de reserva responda con error 404 cuando el cómic no existe o no está disponible. Mi ruta es reservar/int:id_comic/, así que si pongo en el navegador reservar/7 y ese cómic no está creado, tiene que mostrar 404. Lo mismo si el cómic existe, pero tiene disponible en falso. No cambies la lógica del stock ni del formulario".

El ingresar en la URL el ID de un cómic inexistente provocaba errores de lógica. Para solucionar esto, la IA usó "get_object_or_404", que busca un objeto en la base de datos con las condiciones indicadas. Si lo encuentra, lo devuelve para que la vista siga funcionando con normalidad. Si no existe, lanza automáticamente una respuesta 404. Así el sistema responde de forma controlada, de modo que no se puede reservar algo que no está, aunque alguien escriba la URL a mano. Al pedir que no se tocara el stock ni el formulario, el cambio quedó acotado a la vista y no afectó las reglas ya implementadas.