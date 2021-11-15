import ply.lex as lex

#List of reserved words
reserved = {
    # ESTRUCTURAS DE CONTROL
    ## Andres Medina
    'while': 'WHILE',
    'repeat': "REPEAT",

    ##Alejandra Cotrina

    ## Natalia Mawyin
    'if': 'IF',
    'else': 'ELSE',

    # DATOS PRIMITIVOS
    ## Andres Medina
    'Int': 'INT',
    'Double': 'DOUBLER',

    ##

    ## Natalia Mawyin
    'Bool': 'BOOL',
    'String': 'STRING',

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
    'Protocol': 'PROTOCOLR',
    'Self': 'SELFR',
    'Type': 'TYPE',
    'as': 'AS',
    'associativity': 'ASSOCIATIVITY',
    'break': 'BREAK',
    'case': 'CASE',
    'catch': 'CATCH',
    'continue': 'CONTINUE',
    'convenience': 'CONVENIENCE',
    'default': 'DEFAULT',

    ##

    ## Natalia Mawyin
    'precedencegroup': 'PRECEDENCEGROUP',
    'some': 'SOME',
    'throws': 'THROWS',
    'var': 'VAR',
    'prefix': 'PREFIX',
    'required': 'REQUIRED',
    'static': 'STATIC',
    'true': 'TRUE',
    'weak': 'WEAK',
    'private': 'PRIVATE',
    'rethrows': 'RETHROWS',
    'struct': 'STRUCT',
    'try': 'TRY',
    'where': 'WHERE',
    'protocol': 'PROTOCOL',
    'return': 'RETURN',
    'subscript': 'SUBSCRIPT',
    'typealias': 'TYPEALIAS',
    'precedence': 'PRECEDENCE',
    'public': 'PUBLIC',
    'self': 'SELF',
    'throw': 'THROW',
    'unowned': 'UNOWNED',
    'willSet': 'WILLSET',
    'final': 'FINAL',
    'right': 'RIGHT',
    'get': 'GET',
    'switch': 'SWITCH',
    'set': 'SET',
    'super': 'SUPER',
    'left': 'LEFT',
    'class': 'CLASS',

}

# List of token names.
tokens = (
    # SIMBOLOS ESPECIALES
    ## Andres Medina
    'NULO',
    'BACKSLASH',
    'TABULACION',

    ##

    ## Natalia Mawyin
    'COMILLA_D',
    'UNICODE',
    'ALMOHADILLA',

    # OPERADORES MATEMATICOS
    ## Andres Medina
    'ADICION',
    'RESTA',
    
    
    ## Natalia Mawyin
    'INCREMENTO',
    'DECREMENTO',

    # OPERADORES DE ASIGNACIÓN
    ## Andres Medina
    'ASIGNACION',
    'ASIGNACION_ADICION',

    ##

    ## Natalia Mawyin
    'ASIGNACION_DIVISION',
    'ASIGNACION_MODULO',

    # OPERADORES DE COMPARACIÓN
    ## Andres Medina
    'MENOR_IGUAL',
    'IGUAL',

    ##
    
    
    ## Natalia Mawyin
    'MENOR',
    'MAYOR_IGUAL',

    # DATOS PRIMITIVOS
    ## Andres Medina
    'INTEGER',
    'DOUBLE',

    ##

    ## Natalia Mawyin
    'CADENA',
    'BOOLEAN',
    
    # COMPONENTES
    ## Andres Medina
    'DOS_PUNTOS',
    'I_LLAVE',
    'D_LLAVE',

    ##

     ## Natalia Mawyin
    'INTERROGACION',
    'I_PARENTESIS',
    'D_PARENTESIS',

    # OPERADORES LÓGICOS
    ## Andres Medina
    'AND',
    ##

    ## Natalia Mawyin
    'NOT',
    
    
    # OTROS OPERADORES
    ## Andres Medina
    'RANGE'
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

## Alejandra Cotrina 
t_SALTO_LINEA = r'\n'
t_RETORNO__DE_CARRO = r'\\r'
t_COMILLA_SIMPLE = r'\\\''

t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'

t_ASIGNACION_RESTA = r'-='
t_ASIGNACION_MULTI = r'\*='

t_DIFERENTE = r'!='
t_MAYOR = r'>'

t_SLASH = r'/'
t_I_CORCHETE = r'\['
t_D_CORCHETE = r'\]'

t_OR = r'\|\|'

t_FLOAT = r'-?\d+\.\d{1,6}'

t_NIL_COALESCING = r'\?\?'

## Natalia Mawyin

t_COMILLA_D= r'\"'
t_UNICODE= r'u{[0-9a-fA-F]{1,8}}'
t_ALMOHADILLA= r'\#'

t_INCREMENTO= r"\+\+"
t_DECREMENTO= r"--"

t_ASIGNACION_DIVISION= r"/="
t_ASIGNACION_MODULO= r"%="

t_MENOR= r"<"
t_MAYOR_IGUAL= r">="

t_CADENA= r'("[^"]*"|\'[^\']*\')'

t_INTERROGACION= r'\?'
t_I_PARENTESIS= r'\('
t_D_PARENTESIS= r'\)'

t_NOT= r"!"

def t_BOOLEAN(t):
    r"(true|false)"
    return t

## Andres Medina

def t_COMMENTARY(t):
    r'/\*(.|\n)*\*/'
    pass

##Alejandra Cotrina 
def t_VARIABLE(t):
    r'[a-z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t 

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
