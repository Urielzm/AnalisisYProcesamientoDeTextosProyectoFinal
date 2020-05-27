# Importa los metodos a trabajar desde NLTK:
import nltk
# stopwords = palabras reservadas.
from nltk.corpus import stopwords

# word_tokenize = valorizador de palabras.
# sent_tokenize = valorizador de oraciones.
from nltk.tokenize import word_tokenize, sent_tokenize

# Descarga de metodos debido a que stopwords y tokenize
#   no se podían usar sin ellos.

#nltk.download('stopwords')
#nltk.download('punkt')


# Se crean 2 arreglos y 1 variable:

# arreglo 1) - SW - configura el método de entrada o 
#idioma en el que se 
# van a trabajar las palabras en el metodo words de 
#stopwords, en este caso, Español.
SW = set(stopwords.words("spanish"))


# text para definir el texto a resumir.
text = """Información Taxonómica

Las diez especies que componen actualmente el género Sus se localizan principalmente en Asia, aunque el jabalí euroasiático, Sus scrofa, la especie más abundante, muestra un área de distribución histórica más amplia, que incluye Europa y el norte de África. El estudio taxonómico de la especie es complejo por la variación de caracteres debido fundamentalmente a la domesticación.

Descripción

Muestra la máxima altura en la región de las extremidades anteriores; el cuello es poco aparente, las orejas son pequeñas y se mantienen erguidas.

Las dimensiones son muy variables; en Europa la corpulencia aumenta hacia el este, observándose los menores tamaños en el sur de la Península Ibérica y los mayores en los Cárpatos.

Medidas corporales de ejemplares adultos del Montseny (Cataluña), CC: 133,0-148,0 cm (machos), 118,0-137,0 cm (hembras); C: 17,5-24,0 cm (machos), 13,0-20,0 cm (hembras); CR: 72,0-85,5 cm (machos), 71,0-73,0 cm (hembras); Ps: 60-118 kg (machos), 40-65 kg (hembras).

Fórmula dentaria: 3.1.4.3/3.1.4.3. Caninos de puntas agudas y ángulos cortantes.

Posee un marcado dimorfismo sexual, los machos son más corpulentos y presentan los caninos más desarrollados. Al nacer, y hasta los cuatro o cinco meses, se denominan rayones y presentan una coloración pardo clara con 11 líneas longitudinales más oscuras. Posteriormente mudan pasando a tener una coloración uniforme pardo rojiza y se denominan bermejos, hasta la siguiente muda que ocurre entre los 10 y 12 meses, cuando adquieren el pelaje de adultos, que es pardo grisáceo, con extremidades y orejas más oscuras, prácticamente negras.

La especie muestra politipismo cromosómico. Número de cromosomas (2n) = 38, 37 ó 36

El jabalí es el primo salvaje del cerdo doméstico. Es un animal vigoroso, de cuerpo grueso y redondo, cabeza grande y alargada terminada en largo y estrecho hocico, la jeta. Tiene las orejas grandes, enhiestas y de forma triangular. El cuerpo del jabalí está cubierto de pelo. Esta pelambre, compuesta por las cerdas -pelos largos y gruesos- y la borra -pelusa compacta y apelmazada-, presenta bastantes variaciones de color, aunque con predominio del pardo oscuro. Hay ejemplares que presentan un color grisáceo uniforme y otros que tiran más hacia el castaño rojizo. Es característico en el jabalí una franja estrecha de pelo erizable que recorre la nuca y parte del lomo.

No es fácil distinguir el jabalí de la jabalina en una observación de campo. Generalmente la hembra tiene la jeta más alargada, aunque este rasgo no es definitivo. El macho posee dos colmillos que crecen continuamente, de aspecto curvado hacia atrás y que sobresalen de los labios, se llaman defensas o navajas. Las defensas de la hembra no son visibles por fuera de los labios, ya que tienen un tamaño menor.

Distribución

La distribución natural de la especie abarca Europa, Asia y el norte de África y ha sido introducida en el continente americano, Australia, Nueva Zelanda y en diversas islas del Pacífico. En Europa el jabalí ha experimentado durante las últimas décadas una intensa expansión, ampliando su límite de distribución septentrional hasta superar los 65º N y recolonizando zonas de las que se había extinguido, como Inglaterra, Finlandia o Suecia.
Está presente en toda la Península Ibérica. Siendo la zona centro una de las que mayor densidad de jabalíes posee. """

# arreglo 2) - words - almacena el texto en el método word_tokenize para 
                        # previamente darle valor.
words = word_tokenize(text)

print("TOKENIZADAS")
print(words)

# Se crea un diccionario para crear una tabla de frecuencias de las palabras.
freqTable = dict()

# Con un for se recorre el texto y se almacena en la tabla.
for word in words:
    word = word.lower() # setea las palabras en minúscula y las almacena en word.
    if word in SW: 
        continue # Si la palabra se encuentra en SW, continua con el ciclo.
    if word in freqTable: # Si la palabra ya se encuentra en la tabla frecuencia,
        freqTable[word] += 1 # Suma 1 a la posición donde se encuentra la palabra.
    else:
        freqTable[word] = 1 # Sino, la palabra en la TF va a ser igual a 1.

#Muestra la tabla de frecuencias de cada palabra.
#freqTable


print('\t\t\t********TABLA DE FRECUENCIAS ABOSULTAS*********')
print("\n")
print(freqTable)
print("\n")

#Frecuencias ponderadas.
#Se encuentra la palabra de mayor frecuencia.
ponderadas=freqTable
v=list(ponderadas.values())
m=max(v)

# Con un for se recorre el texto y se almacena en la tabla.
for word in words:
    word = word.lower() # setea las palabras en minúscula y las almacena en word.
    if word in SW: 
        continue # Si la palabra se encuentra en SW, continua con el ciclo.
    if word in ponderadas: # Si la palabra ya se encuentra en la tabla frecuencia,
        ponderadas[word] += (1/m)-1 # Suma 1 a la posición donde se encuentra la
    else:
        ponderadas[word] =(1/m)-1 # Sino, la palabra en la TF va a ser igual a 1.
#Muestra la tabla de frecuencias de cada palabra.
#freqTable
print('\t\t\t********TABLA DE FRECUENCIAS PONDERADAS*********')
print("\n")
print("Valor mayor de frecuencia de una palabra:",m)
print(ponderadas)
print("\n")


# Crea una variable y un diccionario.

# Variable sentences para almacenar las oraciones a valorizar del texto.
sentences = sent_tokenize(text)

print(sentences)

# Diccionario sentenceValue para almacenar los valores de las oraciones.
sentenceValue = dict()



#Se crea un ciclo for para recorrer las oraciones que se encuentran en el texto.
for sentence in sentences:
    # Se crea un segundo for para recorrer los items que se encuentran el la TF.
    for word, freq in freqTable.items():
        if word in sentence.lower(): # Si la palabra se encuentra en las oraciones (en minuscula)
            if sentence in sentenceValue: # Y si la oración está en el diccionario de las oraciones a valorizar.
                sentenceValue[sentence] += freq # Entonces sume 1 al número de frecuencia en la posición de la oración del sV.
            else:
                sentenceValue[sentence] = freq # Sino, que el valor de la posición de la oración sea igual a la frecuencia.

#Muestra las oraciones ya valorizadas con su respectivo puntaje.
#sentenceValue

vals=list(sentenceValue.values())
maxVal=max(vals)
minVal=min(vals)
print('\t\t\t********ORACIONES VALORIZADAS*********')
print("\n")
print(sentenceValue)
print("\n")
print("La oracion con mayor valor tiene:",maxVal, "y el menor es:",minVal)
print("\n")

# Se crea una variable donde se almacena la suma de los valores.
sumValues = 0

# Se crea un ciclo for para evaluar la oración dentro del Diccionario de las oraciones valorizadas.
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence] # Se suma 1 al valor de la Oración en su respectiva posición
 
# Valor promedio de una oración desde un texto original
average = int(sumValues/ len(sentenceValue)) # Divide la suma de valores en la total de oraciones valorizadas.
print("Promedio",average)
print("\n")
# Se crea una variable para almacenar el resumen a imprimir.
summary = ''

# Se crea un for para recorrer las oraciones almacenadas
for sentence in sentences:
    
    #Donde si, la oración está las oraciones Valorizadas y la posición de la oración es mayor que 1.2 veces el promedio:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        
        # El resumen va a agregar un espacio más la oración que aprobó la condición.
        summary += " " + sentence

# Se imprime el resumen.
print('\t\t\t*******RESUMEN******')
print("\n"+"\n"+summary)
