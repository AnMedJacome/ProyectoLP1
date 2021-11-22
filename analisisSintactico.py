

# OTRAS FUNCIONES Y VARIABLES DE APOYO PARA EJECUCIÓN DEL PROGRAMA
variables = {}
booleanos = ("true", "false")

precedence = (
    ('left', 'ADICION', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

def ver_string(s):
    return s.find('"') != -1 or s.find("'") != -1

def oparation_number(operador, p_valor, s_valor):
    if operador == '+':
        return p_valor + s_valor
    if operador == '-':
        return p_valor - s_valor
    elif operador == '*':
        return p_valor * s_valor
    elif operador == '/':
        return p_valor / s_valor
    elif operador == '%':
        return p_valor % s_valor

def operation(operador, p_valor, s_valor):
    p_valor = str(p_valor)
    s_valor = str(s_valor)
    if (p_valor.isdigit() and s_valor.isdigit()):
        p_valor = int(p_valor)
        s_valor = int(s_valor)
        return oparation_number(operador, p_valor, s_valor)
    else:
        if operador != '+':
            return
        elif p_valor.find("[") != -1 and s_valor.find("[") != -1:
            p_valor = p_valor.lstrip("]")
            s_valor = s_valor.rstrip("[")
        else:
            p_valor = p_valor.strip("\"")
            s_valor = s_valor.strip("\"")
        return p_valor + s_valor

# PARSEO
def p_swift(p):
    '''swift : instrucciones
             | instrucciones swift
             | funcion
             | funcion swift
             | objeto
             | objeto swift
             | importar_lib
             | importar_lib swift
             | enum_type'''
    p[0] = p[1]

def p_instrucciones(p):
    '''instrucciones : estructura
                     | llamadaFunc
                     | asignacion
                     | resultado_inc_dec
                     | resultado
                     | diccionario_insercion
                     | diccionario_remover
                     | array_change'''
    p[0] = p[1]

def p_varias_instrucciones(p):
    '''varias_instrucciones : instrucciones
                            | instrucciones varias_instrucciones'''
    p[0] = p[1]
   
  
# LIBRERIAS

def p_importar_lib(p):
    'importar_lib : IMPORT OBJECT_TYPE'

# CONTROL DE ACCESO

def p_access_control(p):
    '''access_control : PUBLIC
                      | INTERNAL
                      | FILEPRIVATE
                      | PRIVATE
                      | STATIC
                      | '''

# DATOS

def p_factor_num(p):
    '''factor : INTEGER
              | DOUBLE
              | FLOAT'''
    p[0] = p[1]

def p_factor_var(p):
    'factor : VARIABLE'
    p[0] = p[1]

def p_valor(p):
    '''valor : CADENA
             | factor
             | BOOLEAN
             | array'''
    p[0] = p[1]

def p_valor_estructuras(p):
    '''valorEstructurado : diccionario
                         | conjunto'''
    p[0] = p[1]

def p_valores(p):
    '''valores : valor
               | valorEstructurado'''
    p[0] = p[1]

def p_tipo_datos(p):
    '''tipoDato : INT
                | DOUBLER
                | FLOATR
                | STRING
                | BOOL
                | ANY
                | I_CORCHETE OBJECT_TYPE D_CORCHETE
                | OBJECT_TYPE'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2] + p[3]
   
 
# OPERADORES MATEMÁTICOS

def p_expression_operation(p):
    'resultado : expression operacion expression'
    var1 = p[3]
    var2 = p[1]
    # Esta condicion es para asignar el valor de la variable almacenada
    if var1 in booleanos or var2 in booleanos:
        return
    if var1 in variables:
        var1 = variables[var1]
    if var2 in variables:
        var2 = variables[var2]
    p[0] = operation(p[2], var2, var1)

def p_expression_operationIncDec(p):
    'resultado_inc_dec : VARIABLE operacion_aum'
    variable = p[1]
    # Esta condicion es para asignar el valor de la variable almacenada
    if variable in variables:
        variable = variables[variable]
    if not variable.isdigit():
        return
    variable = int(variable) if variable.find(".") == -1 else float(variable)
    if p[2] == '++':
        variables[p[1]] = variable + 1
    elif p[2] == '--':
        variables[p[1]] = variable - 1

def p_operacion(p):
    '''operacion : ADICION
                 | RESTA
                 | MULTIPLICACION
                 | DIVISION
                 | MODULO'''
    p[0] = p[1]

def p_operacion_aum(p):
    '''operacion_aum : INCREMENTO
                     | DECREMENTO'''
    p[0] = p[1]

def p_expression_term(p):
    '''expression : valor
                  | resultado
                  | I_PARENTESIS resultado D_PARENTESIS'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# ESTRUCTURA (STRUCT / CLASS)

def p_object_type(p):
    'objeto : objeto_sc OBJECT_TYPE I_LLAVE cuerpoObjeto D_LLAVE'

def p_object_declaration(p):
    '''objeto_sc : access_control STRUCT
                 | access_control CLASS'''

def p_object_body(p):
    '''cuerpoObjeto : instruccionesObjeto
                    | instruccionesObjeto cuerpoObjeto'''

def p_object_instructions(p):
    '''instruccionesObjeto : metodoObjeto
                           | asignacionInicial'''

def p_object_method(p):
    '''metodoObjeto : CLASS funcion
                    | access_control funcion
                    | MUTATING funcion'''
    
    
# OPERADORES LOGICOS

def p_op_logico(p):
    '''operadorLogico : AND
                      | OR'''
    p[0] = p[1]
