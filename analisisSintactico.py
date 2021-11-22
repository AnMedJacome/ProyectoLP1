import ply.yacc as yacc
from analisisLexico import tokens

# OTRAS FUNCIONES Y VARIABLES DE APOYO PARA EJECUCIÓN DEL PRGRAMA
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

def comparison(operador, p_valor, s_valor):
    condicion1 = p_valor not in booleanos
    condicion2 = s_valor not in booleanos
    if condicion1 and condicion2 and (operador != '==' or operador != '!='):
        if operador == '>':
            return p_valor > s_valor
        elif operador == '<':
            return p_valor < s_valor
        elif operador == '>=':
            return p_valor > s_valor
        elif operador == '<=':
            return p_valor < s_valor
    if operador == '==':
        return p_valor == s_valor
    elif operador == '!=':
        return p_valor != s_valor

def logic_comparison(operador, p_valor, s_valor):
    if operador == '&&':
        return p_valor and s_valor
    elif operador == '||':
        return p_valor or s_valor

def negative_logic_comparison(p_valor):
    return not p_valor

def verificar_datos_cmp(first_value, second_value, operador):
    if type(first_value) != type(second_value):
        if not isinstance(first_value, str) and not isinstance(second_value, str):
            return comparison(operador, first_value, second_value)
        else:
            print("[!] No puede comparar un String con un Numero (Entero o Flotante)")
            raise SyntaxError
    else:
        return comparison(operador, first_value, second_value)

def dic_insertion(f_elem, s_elem, t_elem, variable):
    if f_elem == "updateValue":
        value = s_elem
        value = value if not value.isdigit() else (int(value) if value.find(".") == -1 else float(value))
        key = t_elem
        key = key if not key.isdigit() else (int(key) if key.find(".") == -1 else float(key))
        if variable not in variables:
            print("[!] Variable anteriormente no definida")
            raise SyntaxError
        elif isinstance(variable, dict):
            print("[!] La variable no es un diccionario")
            raise SyntaxError
        variables[variable][key] = value
        return variables[variable]

def dic_remove(f_elem, s_elem, variable):
    if f_elem == "removeValue":
        key = s_elem
        key = key if not key.isdigit() else (int(key) if key.find(".") == -1 else float(key))
        if variable not in variables:
            print("[!] Variable anteriormente no definida")
            raise SyntaxError
        elif isinstance(variable, dict):
            print("[!] La variable no es un diccionario")
            raise SyntaxError
        return variables[variable].pop(key)

def arr_insertion(f_elem, s_elem, t_elem, variable):
    if f_elem == "insert":
        value = s_elem
        value = value if not value.isdigit() else (int(value) if value.find(".") == -1 else float(value))
        if not t_elem.isdigit():
            print("[!] El indice debe ser un número")
            raise SyntaxError
        if variable not in variables:
            print("[!] Variable anteriormente no definida")
            raise SyntaxError
        elif isinstance(variable, dict):
            print("[!] La variable no es un diccionario")
            raise SyntaxError
        variables[variable].insert(int(t_elem), value)
        return variables[variable]

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

# METODO DE LECTURA

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
               | valorEstructurado
               | array_get'''
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

# ASIGNACIONES

def p_asignacion_inicial(p):
    '''asignacionInicial : encabezado_asignacion VARIABLE asignacion_descripcion
                         | VARIABLE asignacion_descripcion'''
    if p[2] not in variables:
        if len(p) == 4:
            variables[p[2]] = p[3]
        else:
            variables[p[1]] = p[2]
    else:
        print("[!] Variable anteriormente definida")
        raise SyntaxError

def p_encabezado_variable(p):
    '''encabezado_asignacion : VAR
                             | LET'''
    p[0] = p[1]

def p_asignacion_descripcion(p):
    '''asignacion_descripcion :  ASIGNACION expression
                              |  asignacion_tipo ASIGNACION expression
                              |  asignacion_tipo'''
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 4:
        p[0] = p[3]


def p_asignacion_tipo(p):
    '''asignacion_tipo :  DOS_PUNTOS tipoDato
                        | DOS_PUNTOS tipoDato OPCIONAL'''


def p_asignacion_matematica(p):
    'asignacionMatematica : VARIABLE asignacion_operacion factor'
    if p[1] not in variables:
        print("[!] Variable \"{}\" no definida anteriormente".format(p[1]))
        raise SyntaxError
    var1 = variables[p[1]]
    if not var1.isdigit():
        print("[!] Valor de la variable \"{}\" no es un número".format(p[1]))
        raise SyntaxError
    var2 = p[3]
    if var2 in variables:
        var2 = variables[var2]
        if not var2.isdigit():
            print("[!] Valor de la variable \"{}\" no es un número".format(p[3]))
            raise SyntaxError
    elif not var2.isdigit():
        print("[!] El valor \"{}\" no es un número".format(p[3]))
        raise SyntaxError
    var1 = int(var1) if var1.find(".") == -1 else float(var1)
    var2 = int(var2) if var2.find(".") == -1 else float(var2)
    operador = p[2]
    if operador == '+=':
        variables[p[1]] = var1 + var2
    elif operador == '-=':
        variables[p[1]] = var1 - var2
    elif operador == '*=':
        variables[p[1]] = var1 * var2
    elif operador == '/=':
        variables[p[1]] = var1 / var2
    elif operador == '%=':
        variables[p[1]] = var1 % var2
    p[0] = variables[p[1]]

def p_asignacion_operacion(p):
    '''asignacion_operacion : ASIGNACION_ADICION
                            | ASIGNACION_RESTA
                            | ASIGNACION_MULTI
                            | ASIGNACION_DIVISION
                            | ASIGNACION_MODULO'''
    p[0] = p[1]

def p_asignacion(p):
    '''asignacion : asignacionInicial
                  | asignacionMatematica
                  | asignacion_dic'''
    p[0] = p[1]

def p_cuerpo(p):
    '''cuerpo : I_LLAVE varias_instrucciones D_LLAVE
              | I_LLAVE D_LLAVE'''

def p_cuerpo_func(p):
    'cuerpoFunc : I_LLAVE varias_instrucciones RETURN valor D_LLAVE'
    p[0] = p[4]

# FUNCIONES Y MÉTODOS DE INSTANCIA

def p_parametros_metodo(p):
    'parametrosMetodo : I_PARENTESIS parametros D_PARENTESIS'
    p[0] = p[1] + p[2] + p[3]

def p_parametros(p):
    '''parametros : VARIABLE DOS_PUNTOS tipoDato
                  | VARIABLE DOS_PUNTOS tipoDato COMA parametros
                  | VARIABLE DOS_PUNTOS tipoDato ASIGNACION valores
                  | VARIABLE DOS_PUNTOS tipoDato ASIGNACION valores COMA parametros
                  | '''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    elif len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    else:
        p[0] = ""


def p_enviar_parametros(p):
    '''enviar_parametros : VARIABLE DOS_PUNTOS valores
                         | valores
                         | VARIABLE DOS_PUNTOS valores COMA enviar_parametros
                         | valores COMA enviar_parametros
                         | '''
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 4 and p[2] == ':':
        p[0] = p[3]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    elif len(p) == 6:
        p[0] = p[3] + p[4] + p[5]
    else:
        p[0] = ""

def p_recibir_parametros(p):
    'recibir_parametros : I_PARENTESIS enviar_parametros D_PARENTESIS'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_llamada_func(p):
    'llamadaFunc : VARIABLE recibir_parametros'
    if p[1] == "removeValue":
        p[0] = (p[1], p[2].strip("()"))
    elif p[1] == "print":
        print(p[2].strip("()"))
        p[0] = p[2]
    elif p[1] == "updateValue" and p[1] == "insert":
        values = p[2].strip("()").split(",")
        p[0] = (p[1], values[0], values[1])
    else:
        p[0] = p[1] + p[2]

def p_funcion(p):
    '''funcion : FUNC VARIABLE cuerpo_fun_meth
               | FUNC VARIABLE tipoDatoComp_parametrizado cuerpo_fun_meth'''

def p_body_fm(p):
    '''cuerpo_fun_meth : parametrosMetodo cuerpo
                       | parametrosMetodo RETURN_ARROW tipoDato cuerpoFunc
                       | parametrosMetodo THROWS RETURN_ARROW tipoDato cuerpoFunc'''

def p_retorno(p):
    '''retorno : tipoDato
               | I_PARENTESIS tipoDato COMA retorno D_PARENTESIS'''

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


# ENUM
def p_enum(p):
    '''enum_type : access_control ENUM OBJECT_TYPE I_LLAVE enum_body D_LLAVE'''

def p_enum_body(p):
    '''enum_body : CASE VARIABLE
                | CASE VARIABLE enum_type'''

# ESTRUCTURAS DE CONTROL (IF, WHILE, FOR)
def p_estructura(p):
    '''estructura : estructura_while
                  | estructura_if
                  | estructura_for
                  | estructura_switch'''

def p_estructura_while(p):
    '''estructura_while : REPEAT cuerpo WHILE condiciones
                        | WHILE condiciones cuerpo'''
    if len(p) == 5:
        p[0] = p[4]
    if len(p) == 4:
        p[0] = p[2]

def p_estructura_if(p):
    '''estructura_if : IF condiciones cuerpo
                     | estructura_if ELSEIF condiciones cuerpo
                     | estructura_if ELSE cuerpo'''
    if len(p) == 5:
        p[0] = p[3]
    if len(p) == 4:
        p[0] = p[2]

def p_estructura_for(p):
    '''estructura_for : FOR VARIABLE IN INTEGER RANGE INTEGER cuerpo
                      | FOR VARIABLE IN INTEGER RANGE VARIABLE cuerpo
                      | FOR VARIABLE IN array cuerpo
                      | FOR VARIABLE IN array cuerpo WHERE condiciones
                      | FOR CASE LET VARIABLE OPCIONAL IN array cuerpo
                      | FOR CASE LET VARIABLE AS tipoDato IN array cuerpo'''

def p_estructura_switch(p):
    'estructura_switch : SWITCH I_PARENTESIS VARIABLE D_PARENTESIS I_LLAVE casos DEFAULT varias_instrucciones D_LLAVE'

def p_switch_cases(p):
    '''casos : CASE valor DOS_PUNTOS varias_instrucciones
             | CASE valor DOS_PUNTOS varias_instrucciones casos'''

def p_condiciones(p):
    '''condiciones : condiciones_cmp
                   | NOT condiciones_cmp'''
    if len(p) == 3:
        p[0] = negative_logic_comparison(p[2])
    else:
        p[0] = p[1]

def p_condiciones_cmp(p):
    '''condiciones_cmp : condicion
                       | condicion operadorLogico condiciones_cmp'''
    if len(p) == 4:
        p[0] = logic_comparison(p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_condicion(p):
    '''condicion : valor comparador valor
                 | I_PARENTESIS valor comparador valor D_PARENTESIS'''
    if len(p) == 4:
        first_value = p[1] if not p[1].isdigit() else (int(p[1]) if p[1].find('.') == -1 else float(p[1]))
        second_value = p[3] if not p[3].isdigit() else (int(p[3]) if p[3].find('.') == -1 else float(p[3]))
        p[0] = verificar_datos_cmp(first_value, second_value, p[2])
    else:
        first_value = p[2] if not p[2].isdigit() else (int(p[2]) if p[2].find('.') == -1 else float(p[2]))
        second_value = p[4] if not p[4].isdigit() else (int(p[4]) if p[4].find('.') == -1 else float(p[4]))
        p[0] = verificar_datos_cmp(first_value, second_value, p[3])

# ESTRUCTURAS DE DATOS
def p_array(p):
    'array : encabezado_asignacion VARIABLE DOS_PUNTOS I_CORCHETE tipoDato D_CORCHETE ASIGNACION I_CORCHETE arr_elementos D_CORCHETE'
    if p[2] in variables:
        print("[!] Variable anteriormente no definida")
        raise SyntaxError
    if p[9].find(",") != -1:
        variables[p[2]] = p[9].split(",")
    else:
        variables[p[2]] = list(p[9])
    p[0] = variables[p[2]]

def p_arr_elementos(p):
    '''arr_elementos : valores
                     | valores COMA arr_elementos
                     | '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = ""

def p_arr_change(p):
    'array_change : VARIABLE I_CORCHETE valor D_CORCHETE ASIGNACION valores'
def p_arr_get(p):
    'array_get : VARIABLE I_CORCHETE valor D_CORCHETE'

def p_array_insercion(p):
    '''array_insercion : VARIABLE PUNTO llamadaFunc'''
    # llamadaFunc debería tener almacenado una tupla con 3 elementos, el primero es el nombre de la
    # función, el segundo es el elemento a insertar, y el último es la clave donde se va a guardar
    p[0] = arr_insertion(p[3][0], p[3][1], p[3][2], p[1])

def p_dictionary(p):
    '''diccionario : I_CORCHETE tipoDato DOS_PUNTOS tipoDato D_CORCHETE
                   | DICTIONARY tipoDatoComp_parametrizado'''

def p_asignacion_diccionario(p):
    'asignacion_dic : encabezado_asignacion VARIABLE DOS_PUNTOS diccionario ASIGNACION dic_elementos'
    # SE ALMACENA EL VALOR COMO DICCIONARIO DE PYTHON PARA PODER SIMULARLO COMO EL LENGUAJE SWIFT
    if p[2] in variables:
        print("[!] Variable anteriormente definida")
        raise SyntaxError
    dic = {}
    dic_cadena = p[6].strip("[]").split(",")
    for clave in dic_cadena:
        cadena = clave.split(":")
        dic[cadena[0]] = cadena[1]
    variables[p[2]] = dic

def p_diccionario_insercion(p):
    '''diccionario_insercion : encabezado_asignacion VARIABLE ASIGNACION VARIABLE PUNTO llamadaFunc
                             | VARIABLE PUNTO llamadaFunc'''
    # llamadaFunc debería tener almacenado una tupla con 3 elementos, el primero es el nombre de la
    # función, el segundo es el elemento a insertar, y el último es la clave donde se va a guardar
    if len(p) == 4:
        p[0] = dic_insertion(p[3][0], p[3][1], p[3][2], p[1])
    else:
        p[0] = dic_insertion(p[6][0], p[6][1], p[6][2], p[2])

def p_diccionario_remover(p):
    '''diccionario_remover : VARIABLE PUNTO llamadaFunc'''
    # llamadaFunc debería tener almacenado una tupla con 2 elementos, el primero es el nombre de la
    # función, y el segundo es la clave que se va a eliminar
    p[0] = dic_remove(p[3][0], p[3][1], p[1])


def p_dic_elementos(p):
    '''dic_elementos : I_CORCHETE D_CORCHETE
                     | I_CORCHETE dic_element D_CORCHETE'''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = p[1] + p[2]

def p_dic_element(p):
    '''dic_element : valor DOS_PUNTOS valor
                   | valor DOS_PUNTOS valor COMA dic_element'''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_conjunto(p):
    '''conjunto : encabezado_asignacion VARIABLE DOS_PUNTOS SETR tipoDatoSimp_parametrizado ASIGNACION array
                | encabezado_asignacion VARIABLE DOS_PUNTOS SETR tipoDatoSimp_parametrizado I_PARENTESIS D_PARENTESIS'''

#TIPO DE DATOS PARAMETRIZADO

def p_tipo_parametrizado_comp(p):
    'tipoDatoComp_parametrizado : MENOR tipoDato DOS_PUNTOS tipoDato MAYOR'

def p_tipo_parametrizado_simp(p):
    'tipoDatoSimp_parametrizado : MENOR tipoDato MAYOR'

# OPERADORES LOGICOS

def p_op_logico(p):
    '''operadorLogico : AND
                      | OR'''
    p[0] = p[1]


# OPERADORES DE COMPARACION

def p_comparacion(p):
    '''comparador : IGUAL
                  | DIFERENTE
                  | MAYOR
                  | MENOR
                  | MAYOR_IGUAL
                  | MENOR_IGUAL'''
    p[0] = p[1]

    # Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!",p)

    # Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
