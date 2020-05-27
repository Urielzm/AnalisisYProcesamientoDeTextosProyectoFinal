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

# arreglo 1) - SW - configura el método de entrada o idioma en el que se 
                    # van a trabajar las palabras en el metodo words de stopwords, en este caso, Español.
SW = set(stopwords.words("english"))

# text para definir el texto a resumir.
text = """
In computing, artificial intelligence (AI), sometimes called machine intelligence, is machine-demonstrated intelligence, in contrast to natural intelligence displayed by humans and animals. Major AI textbooks define the field as the study of "smart agents" - any device that senses its environment and takes steps that maximize its chances of successfully achieving its goals. [1] Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving." As machines become increasingly capable, tasks that are considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI ​​effect. [3] A joke in Tesler's Theorem says that "AI is what has not been done yet." [4] For example, optical character recognition is often excluded from things considered AI [5], becoming a routine technology. [6] Modern machine capabilities generally classified as AI include successful understanding of human speech, [7] competing at the highest level in strategic game systems (such as chess and Go)), [8] autonomous vehicles , intelligent routing in content delivery networks and military simulations. Artificial intelligence was founded as an academic discipline in 1955, and in the years since then has experienced several waves of optimism, [9] [10] followed by disappointment and loss of funds (known as an "AI winter"), [11] [12] followed by new approaches, success, and renewed funding. [10] [13] For most of its history, AI research has been divided into subfields that often do not communicate with each other. [14] These subfields are based on technical considerations, such as particular objectives (eg "robotics" or "machine learning"), [15] the use of particular tools ("logic" or artificial neural networks), or profound philosophical differences . [16] [17] [18] Subfields have also been based on social factors (private institutions or the work of private researchers)."""

# arreglo 2) - words - almacena el texto en el método word_tokenize para 
                        # previamente darle valor.
words = word_tokenize(text)


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
print(freqTable)



# Crea una variable y un diccionario.

# Variable sentences para almacenar las oraciones a valorizar del texto.
sentences = sent_tokenize(text)

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

print(sentenceValue)

# Se crea una variable donde se almacena la suma de los valores.
sumValues = 0

# Se crea un ciclo for para evaluar la oración dentro del Diccionario de las oraciones valorizadas.
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence] # Se suma 1 al valor de la Oración en su respectiva posición
    
# Valor promedio de una oración desde un texto original
average = int(sumValues/ len(sentenceValue)) # Divide la suma de valores en la total de oraciones valorizadas.

# Se crea una variable para almacenar el resumen a imprimir.
summary = ''

# Se crea un for para recorrer las oraciones almacenadas
for sentence in sentences:
    
    #Donde si, la oración está las oraciones Valorizadas y la posición de la oración es mayor que 1.2 veces el promedio:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        
        # El resumen va a agregar un espacio más la oración que aprobó la condición.
        summary += " " + sentence

# Se imprime el resumen.
print("\n"+"\n"+summary)