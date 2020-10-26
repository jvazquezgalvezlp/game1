import random
import string
mystery_word = [ "abeja", "abejorro", "ajolote", "albatros", "alce", "almeja", "anguila", "antilope", "ardilla", "armadillo", "avestruz", "avispa", "aguila", "babosa", "babuino", "ballena", "barbo", "barracuda", "bisonte", "buitre", "burro", "bufalo", "buho", "caballo", "cabra", "cachalote", "caiman", "calamar", "camaleon", "camaron", "camello", "cangrejo", "canguro", "caracol", "castor", "cebra", "cerdo", "chacal", "chimpance", "chinchilla", "ciempies", "ciervo", "cisne", "cobaya", "cocodrilo", "conejo", "coyote", "cucaracha", "delfin", "dodo", "elefante", "emu", "erizo", "escarabajo", "escorpion", "facochero", "faisan", "flamenco", "foca", "gallina", "gamba", "ganso", "garza", "gato", "gorila", "gorrion", "grulla", "guepardo", "halcon", "hiena", "hipopotamo", "hormiga", "huron", "hamster", "iguana", "impala", "jabali", "jaguar", "jirafa", "kiwi", "koala", "lagarto", "langosta", "lechuza", "leopardo", "leon", "libelula", "liebre", "lince", "llama", "lobo", "loro", "lemur", "manati", "mandril", "mangosta", "mantarraya", "mapache", "mariposa", "mariquita", "medusa", "milpies", "mirlo", "mofeta", "mono", "morsa", "mosca", "mula", "murcielago", "musaraña", "nutria", "ñu", "ocelote", "orangutan", "orca", "ornitorringo", "oruga", "ostra", "oveja", "pantera", "pelicano", "percebe", "perezoso", "periquito", "piraña", "polilla", "puercoespin", "pulpo", "rinoceronte", "ruiseñor", "salamandra", "saltamontes", "sepia", "serpiente", "suricato", "tejon", "termita", "tiburon", "tigre", "tortuga", "tucan", "urraca", "wombat", "zapatero"]

word = random.choice(mystery_word)
def hangman():
    alpabet = (set(string.ascii_uppercase))
    word_letters = set(word) #letras en la palabra de mystery_word
    used_letters = set() #letras usadas por el jugador

    chances = 6

    while len(word_letters) > 0 and chances > 0:
        #letras usadas
        print("Te quedan", chances, "oportunidades, y ya has usado estas letras: ', '".join(used_letters))

        # Cual es la palabra (escondida)
        word_list = [letter if letter in used_letters else "_"for letter in word]
        print("Palabra actual: ", "".join(word_list))

        letra_propuesta = input("Letra a probar: ").upper() #letra insertada por el jugador

        if letra_propuesta in alphabet:
            used_letters.append(letra_propuesta)
            if letra_propuesta in word_letters:
                word_letters.remove(letra_propuesta)
            else:
                chances = chances - 1  #Quita una oportunidad
        elif letra_propuesta in used_letters:
            print("Esta letra ya ha sido usada, prueba con otra.")
        else:
            print("No he podido reconocer esta letra")

    if chances == 0:
        print("GAME OVER" "Mucha suerte para la próxima partida" "La palabra era :" ,word,)
    else:
        print("¡Enhorabuena!, has logrado escapar de la horca")
hangman()