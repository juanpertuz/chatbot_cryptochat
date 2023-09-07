import spacy
# Se importa la biblioteca SpaCy para el procesamiento de lenguaje natural.

# Cargar el modelo en español.
nlp = spacy.load("es_core_news_md")


# Se crea la función que iniciara el chatbot
def start_chatbot():
    print("Hola, soy CriptoChat")


# Se crea función para que el usuario haga preguntas.
def question_input():
    # Recibimos las preguntas del usuario y se convierte a minúsculas.
    question = input("¿Tienes una pregunta?: ").lower()
    return question


# Se crea la función donde se almacenan las posibles preguntas del usuario y sus respectivas respuestas en un
# diccionario.
def generate_response(questions):
    doc = nlp(questions)
    predefined_questions = {
        'Adios': 'Adios, vuelve pronto',
        'Como estas?': 'Estoy muy bien, gracias por preguntar.',
        'Cuál es tu nombre?': "Mi nombre es CryptoChat.",
        'Como te llamas?': "Mi nombre es CryptoChat.",
        '¿Qué son las criptomonedas?': 'Las criptomonedas son un tipo de moneda digital que utiliza la criptografía '
                                       'para asegurar sus transacciones, controlar la creación de unidades adicionales '
                                       'y verificar la transferencia de fondos. Las criptomonedas son descentralizadas,'
                                       ' lo que significa que no están controladas por ninguna entidad central, como un'
                                       ' gobierno o un banco central.',
        '¿Cómo funcionan las criptomonedas?': 'Las criptomonedas funcionan utilizando una tecnología llamada blockchain,'
                                              ' La cual es un registro distribuido que almacena información sobre todas'
                                              ' las transacciones realizadas con una criptomoneda. La cadena de bloques'
                                              ' es segura y transparente, y permite a los usuarios verificar las '
                                              'transacciones sin necesidad de confianza en una entidad central.',
        '¿Cuáles son las ventajas de las criptomonedas?': 'Las criptomonedas ofrecen una serie de ventajas sobre las '
                                                          'monedas fiduciarias tradicionales, como el dólar '
                                                          'estadounidense o el euro. Estas ventajas incluyen:\n'
                                                          'Transacciones más rápidas y baratas: Las transacciones con '
                                                          'criptomonedas suelen ser más rápidas y baratas que las '
                                                          'transacciones con monedas fiduciarias.\n'
                                                          'Mayor seguridad: Las criptomonedas utilizan la criptografía '
                                                          'para proteger sus transacciones, lo que las hace más seguras'
                                                          ' que las monedas fiduciarias.\n'
                                                          'Mayor transparencia: La cadena de bloques es un registro '
                                                          'público que almacena información sobre todas las transacciones'
                                                          ' realizadas con una criptomoneda. Esto la hace '
                                                          'más transparente que las monedas fiduciarias.\n'
                                                          'Menor riesgo de censura: Las criptomonedas son '
                                                          'descentralizadas, lo que las hace menos susceptibles a la '
                                                          'censura que las monedas fiduciarias.',
        '¿Cuáles son las desventajas de las criptomonedas?': 'Las criptomonedas también tienen algunas desventajas, '
                                                             'como:\n'
                                                             'Volatilidad: El precio de las criptomonedas es muy '
                                                             'volátil, lo que significa que puede subir o bajar '
                                                             'rápidamente.\n'
                                                             'Riesgo de fraude: Las criptomonedas han sido utilizadas '
                                                             'para el fraude y otras actividades ilegales.\n'
                                                             'Complejidad: Las criptomonedas pueden ser difíciles de '
                                                             'comprender y usar.',
        '¿Cuál es la historia de las criptomonedas?': 'La primera criptomoneda, Bitcoin, fue creada en 2009 por un '
                                                      'programador desconocido bajo el seudónimo de Satoshi Nakamoto. '
                                                      'Bitcoin fue diseñada para ser una moneda digital descentralizada'
                                                      ' que no estuviera controlada por ninguna entidad central. Desde '
                                                      'la creación de Bitcoin, se han creado muchas otras criptomonedas.'
                                                      'Algunas de las criptomonedas más populares incluyen Ethereum, '
                                                      'Litecoin, Ripple y Dogecoin.',
        '¿Cómo se puede comprar criptomonedas?': 'Las criptomonedas se pueden comprar en intercambios de criptomonedas.'
                                                 ' Los intercambios de criptomonedas son plataformas que permiten a los'
                                                 ' usuarios comprar, vender e intercambiar criptomonedas.',
        '¿Cómo se almacenan las criptomonedas?': 'Las criptomonedas se almacenan en carteras de criptomonedas. '
                                                 'Las carteras de criptomonedas son aplicaciones o dispositivos que '
                                                 'permiten a los usuarios almacenar sus claves privadas, que son '
                                                 'necesarias para acceder a sus criptomonedas.',
        '¿Cómo se gastan las criptomonedas?': 'Las criptomonedas se pueden gastar en una variedad de servicios y '
                                              'productos. Algunos de los lugares donde se pueden gastar criptomonedas '
                                              'incluyen comercios en línea, plataformas de inversión donde se pueden '
                                              'utilizar criptomonedas para invertir en una variedad de activos, como '
                                              'acciones, bonos y bienes raíces, y servicios financieros.',
        '¿Cuáles son las regulaciones sobre las criptomonedas?': 'Las regulaciones sobre las criptomonedas varían de '
                                                                 'país a país. En algunos países, las criptomonedas son'
                                                                 ' completamente legales, mientras que en otros están '
                                                                 'sujetas a restricciones, por ejemplo en los Estados '
                                                                 'Unidos, las criptomonedas están reguladas por la '
                                                                 'Comisión de Bolsa y Valores (SEC). La SEC ha emitido '
                                                                 'una serie de reglas y regulaciones que rigen la '
                                                                 'oferta y venta de criptomonedas.',
        '¿Cuál es el futuro de las criptomonedas?': 'El futuro de las criptomonedas es incierto. Algunos expertos creen'
                                                    ' que las criptomonedas se convertirán en una forma de moneda '
                                                    'dominante en el futuro, mientras que otros creen que su '
                                                    'popularidad disminuirá. En última instancia, el futuro de las '
                                                    'criptomonedas dependerá de una serie de factores, como la adopción'
                                                    ' por parte de los consumidores, la regulación gubernamental y el '
                                                    'desarrollo tecnológico.',
        '¿Qué es Ethereum?': 'Ethereum es una plataforma blockchain descentralizada que permite la creación de '
                             'aplicaciones descentralizadas (dApps). Las dApps son aplicaciones que no están '
                             'controladas por ninguna entidad central.',
        '¿Qué es un monedero (wallet) de criptomonedas?': 'Un monedero de criptomonedas es una aplicación o dispositivo'
                                                          ' que se utiliza para almacenar, enviar y recibir '
                                                          'criptomonedas. Pueden ser monederos en línea, de software, '
                                                          'de hardware o de papel.',
        '¿Cómo se asegura un monedero de criptomonedas?': 'Los monederos de criptomonedas se aseguran mediante el uso '
                                                          'de claves privadas. Mantener la clave privada segura y fuera'
                                                          ' del alcance de otros es esencial para proteger tus '
                                                          'criptomonedas.',
        '¿Qué es la minería de criptomonedas?': 'La minería de criptomonedas es el proceso de validar transacciones y '
                                                'agregarlas al libro mayor (blockchain) de una criptomoneda. Los '
                                                'mineros utilizan hardware especializado para resolver complejos '
                                                'problemas matemáticos y son recompensados con nuevas criptomonedas.',
        '¿Qué es una ICO?': 'Un ICO (Oferta Inicial de Moneda) es un evento en el que una empresa o proyecto emite su '
                            'propia criptomoneda a cambio de inversión.',
        '¿Cuál es la diferencia entre Bitcoin y Ethereum?': 'Bitcoin es principalmente una moneda digital diseñada para'
                                                            ' ser utilizada como reserva de valor o medio de '
                                                            'intercambio. Ethereum, además de ser una criptomoneda '
                                                            '(Ether - ETH), es una plataforma que permite la creación '
                                                            'de contratos inteligentes y aplicaciones descentralizadas '
                                                            '(DApps).',
        '¿Qué es un contrato inteligente (smart contract)?': 'Un contrato inteligente es un código autónomo que se '
                                                             'ejecuta en la blockchain y que automática y directamente '
                                                             'ejecuta, verifica o facilita contratos o acuerdos entre'
                                                             ' partes.',
        '¿Qué es un token?': 'Un token es una unidad de valor que existe en una blockchain. Pueden representar activos '
                             'digitales como acciones, propiedades o incluso acceso a servicios.',
        '¿Que es la blockchain?': 'La blockchain es una base de datos pública y descentralizada que registra todas las '
                                  'transacciones de una criptomoneda. Es inmutable y transparente.'
    }

    # Busca similitudes entre la pregunta del usuario y las preguntas predefinidas
    for key, value in predefined_questions.items():
        # Las preguntas predefinidas se pasan a minúsculas y se ajusta el umbral o porcentaje de similitud
        # según se necesite.
        if doc.similarity(nlp(key.lower())) > 0.70:
            return value
    # Si no se encuentra una coincidencia, proporciona una respuesta predeterminada
    return 'Lo siento, no se como responder a eso.'


# Se llama a la función que inicia el chat.
start_chatbot()
while True:
    question = question_input()  # Se le pide al usuario una pregunta.
    answer = generate_response(question)  # Se genera la respuesta a la pregunta, si se conoce.
    print(answer)
    # Si el usuario escribe la palabra 'Adios' se detiene el bucle y se cierra el chat.
    if question.lower() == 'adios':
        break
