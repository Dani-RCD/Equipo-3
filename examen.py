from abc import ABC, abstractmethod

# Excepción personalizada
class CustomException(Exception):
    pass

# Clase base para empleados
class EmpleadoD15(ABC):
    def __init__(self, RFC, Apellidos, Nombres):
        self.RFC = RFC
        self.apellidos = Apellidos
        self.nombres = Nombres
    
    @abstractmethod
    def calcular_sueldo_neto(self):
        pass

    def mostrar_informacion(self):
        return f"RFC: {self.RFC}, Apellidos: {self.apellidos}, Nombres: {self.nombres}"

# Clase para el empleado vendedor
class EmpleadoVendedorD15(EmpleadoD15):
    def __init__(self, RFC, Apellidos, Nombres, Monto_vendido, Tasa_comision):
        super().__init__(RFC, Apellidos, Nombres)
        self.monto_vendido = Monto_vendido
        self.tasa_comision = Tasa_comision

    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision

    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return 0.05 * ingresos
        else:
            return 0.10 * ingresos

    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return 0.11 * ingresos
        else:
            return 0.15 * ingresos

    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        sueldo_neto = ingresos + bonificacion - descuento
        
        if sueldo_neto < 150:
            raise CustomException("El salario es menor que 150")
        
        return sueldo_neto

# Clase para el empleado permanente
class EmpleadoPermanenteD15(EmpleadoD15):
    def __init__(self, RFC, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(RFC, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.numero_seguro_social = numero_seguro_social

    def calcular_descuento_seguro(self):
        return 0.11 * self.sueldo_base

    def calcular_sueldo_neto(self):
        descuento = self.calcular_descuento_seguro()
        sueldo_neto = self.sueldo_base - descuento
        
        if sueldo_neto < 150:
            raise CustomException("El salario neto es menor que 150")
        
        return sueldo_neto

# Función para ingresar los datos del vendedor
def ingresar_datos_vendedor():
    RFC = input("Ingrese su RFC: ")
    Apellidos = input("Ingrese sus apellidos: ")
    Nombres = input("Ingrese su nombre: ")
    Monto_vendido = float(input("Ingrese el monto vendido: "))
    Tasa_comision = float(input("Ingrese la tasa de comisión (0.10..): "))
    
    vendedor = EmpleadoVendedorD15(RFC, Apellidos, Nombres, Monto_vendido, Tasa_comision)
    return vendedor

# Función para ingresar los datos del empleado permanente
def ingresar_datos_permanente():
    RFC = input("Ingrese su RFC: ")
    Apellidos = input("Ingrese sus apellidos: ")
    Nombres = input("Ingrese su nombre: ")
    Sueldo_base = float(input("Ingrese el sueldo base: "))
    Numero_seguro_social = input("Ingrese el número de seguro social: ")
    
    permanente = EmpleadoPermanenteD15(RFC, Apellidos, Nombres, Sueldo_base, Numero_seguro_social)
    return permanente

# Función principal para manejar la interacción con el usuario
def main():
    try:
        print("Seleccione el tipo de empleado:")
        print("1. Empleado Vendedor")
        print("2. Empleado Permanente")
        opcion = int(input("Ingrese su opción (1 o 2): "))

        if opcion == 1:
            vendedor = ingresar_datos_vendedor()
            print(vendedor.mostrar_informacion())
            print(f"Sueldo neto del vendedor: {vendedor.calcular_sueldo_neto()}")

        elif opcion == 2:
            permanente = ingresar_datos_permanente()
            print(permanente.mostrar_informacion())
            print(f"Sueldo neto del empleado permanente: {permanente.calcular_sueldo_neto()}")

        else:
            print("Error: Ingrese el número 1 o 2.")

    except CustomException as e:
        print(e)

    except ValueError:
        print("Error: Ingrese datos correctamente.")

# Iniciar el programa
if __name__ == "__main__":
    main()
