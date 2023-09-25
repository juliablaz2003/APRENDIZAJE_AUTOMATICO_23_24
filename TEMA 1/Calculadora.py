class Calculadora:  # se define la clase calculadora
    def __init__(self, x=0, y=0): # si no me pasas ningun valor coge automaticamente 0 para x e y, este es el constructor
        self._x = x
        self._y = y
        
    # Métodos Setter para x e y
    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
        
    # Métodos Getter para x e y
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

# Métodos para las operaciones básicas
    def suma(self):
        return self._x + self._y
    
    def resta(self):
        return self._x - self._y
    
    def multiplicacion(self):
        return self._x * self._y
    
    def division(self):
        if self._y == 0:
            return "Error: División por cero"
        return self._x / self._y


if __name__ == "__main__":
    # Ejemplo de uso
    calc = Calculadora(10, 5)  # Se crea un objeto calculadora con x=10 y y=5, llamo a la clase calculadora
    
    print("x:", calc.get_x())  # Se imprime el valor de x=10
    print("y:", calc.get_y())  # Se imprime el valor de y=5

    # Tambien se puede llamar directamente al atributo
    print("x:", calc._x)  # Se imprime el valor de x
    print("y:", calc._y)  # Se imprime el valor de y
    
    print("Suma:", calc.suma())  # Se imprime el resultado de la suma 10+5=15
    print("Resta:", calc.resta())  # Se imprime el resultado de la resta 10-5=5
    print("Multiplicación:", calc.multiplicacion())  # Se imprime el resultado de la multiplicación 10*5=50
    print("División:", calc.division())  # Se imprime el resultado de la división
    
    # Cambiar valores de x e y usando los métodos Setter
    calc.set_x(20)  # Se cambia el valor de x a 20
    calc.set_y(0)  # Se cambia el valor de y a 0
    
    print("\nValores Actualizados")
    print("x:", calc.get_x())  # Se imprime el nuevo valor de x
    print("y:", calc.get_y())  # Se imprime el nuevo valor de y
    print("División con nuevos valores:", calc.division())  # Se intenintenta realizar una división por cero
