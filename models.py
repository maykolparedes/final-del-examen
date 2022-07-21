class Producto:
    def __init__(self, codigo, nombre, precio): 
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return "{};{};{}\n".format(
            self.codigo, self.nombre, self.precio
        )
class Usuario:
    # atributos
    def __init__(
        self, dni, password, nombres_apellidos, direccion, telefono, email
    ):
        self.dni = dni
        self.password = password
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    # metodos
    def __str__(self):
        return "{};{};{};{};{};{}\n".format(
            self.dni,
            self.password,
            self.nombres_apellidos,
            self.direccion,
            self.telefono,
            self.email,
        )
class Registro:
    def __init__(self, tipo_comb, n_venta,n_documento,razon_s,producto,precio,cantidad,total):
        self.tipo_comb = tipo_comb
        self.n_venta = n_venta
        self.n_documento = n_documento
        self.razon_s = razon_s
        #self.establecimiento = establecimiento
        #self.tipo_m = tipo_m
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.total = total

    def __str__(self):
        return "{};{};{};{};{};{};{};{}\n".format(
            self.tipo_comb,self.n_venta,self.n_documento,self.razon_s,self.producto,self.precio,self.cantidad,self.total  
        )