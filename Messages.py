import discord

Secondarytemplate = "* 1 Aquí puedes ver los comandos;* \n\n '**9Ayuda**'\n Este comando resume el bot, incluye acceso a su repositorio. \n\n '**9Origen**'\n Este comando resume los orígenes del cambio climático \n\n '**9Gravedad**'\n Resumen estadístico sobre la gravedad del cambio climático \n\n '**9Mapa**'\n Un mapa textual y visual sobre las emisiones mundiales \n\n '**9Goals**'\n Sobre la UN (United Nations y como se planea terminal el cambio climático, junto con el sufrimiento global. "
ComandoAyudaEmbed = {
    "title": "<:2366_Loading_Pixels:1493429649311666277>   __**Nine es un bot de Discord**__ sobre del cambio climatico",
    "description": "■□□ \n Nine busca ser *informativo*, dando información y estadísticas sobre el estado actual del mundo \n —— \n ■■□ \n Para elaborar, Nine contiene un número de comandos introduciendo el porque, como, y efectos del cambio climático, junto con actualizaciones de su solución y urgencia \n —— \n ■■■ \n Debajo hay botones que contienen una guía básica al bot, y el repositorio, con el cual puedes ver su código, ya que es de *código abierto*",
    "color": 9710122,
    "footer": {"text": "-Hecho por Sol"}
}

BotonComandosEmbed = {
    "title": "<:9_:1493670642862526546> *Aquí puedes ver los comandos;*",
    "description": "\n\n '**9Ayuda**'\n Este comando resume el bot, incluye acceso a su repositorio. \n\n '**9Origen**'\n Este comando resume los orígenes del cambio climático \n\n '**9Gravedad**'\n Resumen estadístico sobre la gravedad del cambio climático \n\n '**9Ecotip**'\n Genera un Ecotip aleatorio \n\n '**9Goals**'\n Sobre la UN (United Nations y como se planea terminal el cambio climático, junto con el sufrimiento global. ",
    "color": 12524315,
    
}

OrigenComandosEmbed = {
    "title": " <:one1:1494055696180973759> El origen del cambio climatico",
    "description": " La Primera Revolucion Industrial occuriria en el siglo 17-18, en el Reino Unido. Llevando un triunfo en revolucionar la economia y produccion de energia, causaria uno de los mayores cambios en la historia hacia la tecnologia, la economia, y el trabajo. Introduciendo la maquina a vapor, la mecanizacion, y para la Segunda Revolucion industrial, el uso de la electricidad.  \n —— \n \n <:two2:1494055721849983117>  **. . .  El problema** \n Para producir energia y electricidad, se empezo a hacer uso no solo de los combustibles fosiles, pero del carbon. Al principio se minaban formas mas puras, y compactas, del carbon de buena calidad. Pero coma toman miles de años en formarse, son un recurso limitado. Y asi, se empezaron a talar arboles a grande escala para el carbon del cual las fabricas usaban, junto con la extraccion de combustible fosil, los dos cuales causan *emisiones de carbono*. Todo esto, daño el ambiente a grande escala, llevando al ***cambio climatico***\n —— ",
    "color": 12524315,
}

Oembeds = [discord.Embed(title=" <:one1:1494055696180973759> El origen del cambio climatico", description=" La Primera Revolucion Industrial occuriria en el siglo 17-18, en el Reino Unido. Llevando un triunfo en revolucionar la economia y produccion de energia, causaria uno de los mayores cambios en la historia hacia la tecnologia, la economia, y el trabajo. Introduciendo la maquina a vapor, la mecanizacion, y para la Segunda Revolucion industrial, el uso de la electricidad.  \n —— \n \n ❯❯❯❯ "),
          discord.Embed(title=" <:two2:1494055721849983117>  **. . .  El problema**", description="Para producir energia y electricidad, se empezo a hacer uso no solo de los combustibles fosiles, pero del carbon. Al principio se minaban formas mas puras, y compactas, del carbon de buena calidad. Pero coma toman miles de años en formarse, son un recurso limitado. Y asi, se empezaron a talar arboles a grande escala para el carbon del cual las fabricas usaban, junto con la extraccion de combustible fosil, los dos cuales causan *emisiones de carbono*. Todo esto, daño el ambiente a grande escala, llevando al ***cambio climatico***\n ——"),
          ]

Oembeds[0].set_image(url="https://res.cloudinary.com/aenetworks/image/upload/c_fill,ar_1.7777777777777777,w_3840,h_2160,g_auto/dpr_auto/f_auto/q_auto:eco/v1/second_industrial_revolution_gettyimages-51632462?_a=BAVMn6DY0")
Oembeds[1].set_image(url="https://res.cloudinary.com/aenetworks/image/upload/c_fill,ar_1.7777777777777777,w_3840,h_2160,g_auto/dpr_auto/f_auto/q_auto:eco/v1/second_industrial_revolution_gettyimages-51632462?_a=BAVMn6DY0")

Gembed = [discord.Embed(title="<:Leaf:1498462507994583060> La gravedad del *cambio climatico* \n", description="Al cambio climatico se le considera una crisis *acelerada*, y la cual se vuelve progresivamente peor y mas rapida con forma no se soluciona.  \n —— \n \n  \n Los *gases de efecto invernadero* causan calentamiento global -> Lleva a sequías, incendios forestales, lluvias extremas, entre otros eventos climáticos extremos -> Tanto el calentamiento como los eventos climáticos llevan al colapso de ecosistemas, lo cual cada vez es más difícil de reparar (con forma colapsan los sensibles ecosistemas, se vuelve casi imposible reparar las específicas condiciones en las que existen)\n\n \n ❯❯❯❯ "),
          discord.Embed(title=". . .  Algunos datos \n", description="***Las emisiones de CO₂ han aumentado por un 70%*** \n ***Un 60% de la pérdida de hielo vinculada a la crisis climática*** \n  ***Perdidas del ecosistema hasta 1000 veces mas rapida*** \n \n ❯❯❯❯"),
        discord.Embed(title="Daños irreversibles y viciosos", description="***Derretimiento del permafrost - Gases de metano liberados - Gases de infesto invernadero se acumulan - Llevan a más derretimiento*** \n \n Algunos otros ejemplos: Corales, niveles del mar, extinción (totalmente irreversible). "),
          ]

Gembed[0].set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Change_in_Average_Temperature_With_Fahrenheit.svg/330px-Change_in_Average_Temperature_With_Fahrenheit.svg.png")

EcotipD = [
    "## --> Random ecotip \n\n Asegurate de areglar goteras en tu hogar, o de reciclar el agua",

    "## --> Random ecotip \n\n No uses objetos desechables de plastico (bolsas, encendedores, botellas, cubiertos de un solo uso)",

    "## --> Random ecotip \n\n Asegurate de apagar todos tus objetos electronicos, y usarlos lo mas eficiente que sea posible. Esto tambien ahorra dinero!",

    "## --> Random ecotip \n\n Objetos como ropas, utensilios y decorativos aun usables/en buena calidad, deberian ser donados",

    "## --> Random ecotip \n\n Riega cuando el sol no esta pegando directamente, previene malgastar agua por la evaporacion",

    "## --> Random ecotip \n\n En muchos lugares, hay zonas donde puedes llevar basura para que se recicle, en vez de ser desechada",

    "## --> Random ecotip \n\n Dona a tus grupos locales de reciclaje, limpieza, o ayudalos si no tienes dinero",

    "## --> Random ecotip \n\n Comparte con otros ecotips y informacion sobre el cambio climatico",

    "## --> Random ecotip \n\n Ayuda a causas de replantacion forestal o, similarmente, recuperacion de ecosistemas (que cada pais suele tener alguno)",

    "## --> Random ecotip \n\n No te dejes consumir por trends! El consumo innecesario lleva a mucho malgasto, especialmente objetos baratos y no biodegradables",
]

GoalsComandosEmbed = {
    "title": "<:clover4:1498553110648328313>  La meta de la UN \n ",
    "description": "La UN (*United Nations*) contiene un protocolo de metas sostenibles y realistas, para solucionar los problemas del mundo. \n \n La meta numero 13, es aquella de 'accion climatica' La cual se divide en varias acciones; \n \n ### ***Energias renovables*** \n Algo que no se ha mencionado, es que la *tercera revolucion industrial* llevia a la creacion de la energia nuclear, la cual se considera, por mucho, la mas eficiente y bio-amigable forma de produccion de energia. Aunque aqui tambien se incluyen otros metodos como los paneles de luz solar, turbinas de viento, etc. \n ### ***Adaptacion***\n Una de las prevenciones de catastrofes climaticas, es adoptar sistemas que prevengan daños por los cambios que ya han pasado (como las tormentas extremas y sequias) instalando sistemas seguros que prevengan muertes en estas situaciones. \n ### ***Financias*** \n la UN ya ha planeado poner por lo menos $300 billones de dolares anuales en fundar investigaciones, tecnologias, y soluciones al cambio climatico. \n \n \n ***Tambien, se puede contribuir personalmente a la solucion*** ˅˅˅",
    "color": 8954742,
   "image": {
    "url": "https://i.ibb.co/212N3Yt6/Screenshot-2026-04-27-225752.png"
   }
}
