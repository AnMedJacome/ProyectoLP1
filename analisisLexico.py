import ply.lex as lex

#List of reserved words
reserved = {
    # ESTRUCTURAS DE CONTROL
    ## Andres Medina
    'while': 'WHILE',
    'repeat': "REPEAT",

    ##

    ##


    # DATOS PRIMITIVOS
    ## Andres Medina
    'Int': 'INT',
    'Double': 'DOUBLER',

    ##

    ##


    # PALABRAS RESERVADAS
    ## Andres Medina
    '#available': 'NS_AVAILABLE',
    '#colorLiteral': 'NS_COLORLITERAL',
    '#column': 'COLUMN',
    '#dsohandle': 'NS_DSOHANDLE',
    '#else': 'NS_ELSE',
    '#elseif': 'NS_ELSEIF',
    '#endif': 'NS_ENDIF',
    '#error': 'NS_ERROR',
    '#file': 'NS_FILE',
    '#fileID': 'NS_FILEID',
    '#fileLiteral': 'NS_FILELITERAL',
    '#filePath': 'NS_FILEPATH',
    '#function': 'NS_FUNCTION',
    '#if': 'NS_IF',
    '#imageLiteral': 'NS_IMAGELITERAL',
    '#keyPath': 'NS_KEYPATH',
    '#line': 'NS_LINE',
    '#selector': 'NS_SELECTOR',
    '#sourceLocation': 'NS_SOURCELOCATION',
    '#warning': 'NS_WARNING',
    'Any': 'ANY',
    'Protocol': 'PROTOCOL',
    'Self': 'SELF',
    'Type': 'TYPE',
    'as': 'AS',
    'associativity': 'ASSOCIATIVITY',
    'break': 'BREAK',
    'case': 'CASE',
    'catch': 'CATCH',
    'continue': 'CONTINUE',
    'convenience': 'CONVENIENCE',
    'default': 'DEFAULT'

    ##

    ##

}

# List of token names.
tokens = (
    # SIMBOLOS ESPECIALES
    ## Andres Medina
    'NULO',
    'BACKSLASH',
    'TABULACION',

    ##

    ##

    # OPERADORES MATEMATICOS
    ## Andres Medina
    'ADICION',
    'RESTA',

    # OPERADORES DE ASIGNACIÓN
    ## Andres Medina
    'ASIGNACION',
    'ASIGNACION_ADICION',

    ##

    ##

    # OPERADORES DE COMPARACIÓN
    ## Andres Medina
    'MENOR_IGUAL',
    'IGUAL',

    ##

    ##

    # DATOS PRIMITIVOS
    ## Andres Medina
    'INTEGER',
    'DOUBLE',

    ##

    ##

    # COMPONENTES
    ## Andres Medina
    'DOS_PUNTOS',
    'I_LLAVE',
    'D_LLAVE',

    ##

     ##

    # OPERADORES LÓGICOS
    ## Andres Medina
    'AND',
    ##

    ##

    # OTROS OPERADORES
    ## Andres Medina
    'RANGE'
    ##

    ##


         ) + tuple(reserved.values())

# Regular expression rules for simple tokens

## Andres Medina
t_NULO = r'\0'
t_BACKSLASH = r'\\\\'
t_TABULACION = r'\t'

t_ADICION = r'\+'
t_RESTA = r'-'

t_ASIGNACION = r'='
t_ASIGNACION_ADICION = r'\+='

t_MENOR_IGUAL = r'<='
t_IGUAL = r'=='

t_DOS_PUNTOS = r':'
t_I_LLAVE = r'{'
t_D_LLAVE = r'}'

t_INTEGER = r'-?([0-9]{1,10}|2[0-1][0-9]{1,8})'
t_DOUBLE = r'-?\d+\.\d{1,15}'

t_AND = r'&&'

t_RANGE = r'(\.\.\.|\.\.<)'

def t_COMMENTARY(t):
    r'/\*(.|\n)*\*/'
    pass

##

##


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test
data = '''
\\\\ Algoritmo Insertion sort
/*
 * Ordenamiento de menor a mayor
 * Recibe un arreglo y el número de elementos que contiene el mismo
 */
func insertionSort<T: Comparable>(arreglo: [T], n: Int) -> [T] {
  var arregloOrdenado = arreglo
  for index in 1..<n {
    while position > 0 && arregloOrdenado[position - 1] > value {
        arregloOrdenado[position] = arregloOrdenado[position - 1]
        position -= 1
      }
  }
  return arregloOrdenado
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
