import math

# ============================================================
# TALLER: FIGURAS GEOMÉTRICAS (POO EN PYTHON)
# Estudiante: Nasly
# Fecha: 6/5/26 | Hora: 11:12
# ============================================================

class FiguraGeometrica:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    @property
    def nombre(self):
        return self.__nombre

    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self):
        return f"Figura: {self.__nombre}"


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.__base = 0
        self.__altura = 0
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, valor):
        if valor > 0:
            self.__base = valor
        else:
            print(f"Error: La base {valor} no es válida. Se asigna 1.")
            self.__base = 1

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self.__altura = valor
        else:
            print(f"Error: La altura {valor} no es válida. Se asigna 1.")
            self.__altura = 1

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * (self.__base + self.__altura)

    def __str__(self):
        return f"{super().__str__()} [Base: {self.base}, Altura: {self.altura}]"


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.__radio = 0
        self.radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, valor):
        if valor > 0:
            self.__radio = valor
        else:
            print(f"Error: El radio {valor} no es válido. Se asigna 1.")
            self.__radio = 1

    def area(self):
        return math.pi * (self.__radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.__radio

    def __str__(self):
        return f"{super().__str__()} [Radio: {self.radio}]"


# ================== EJECUCIÓN ==================
if __name__ == "__main__":
    print("=" * 50)
    print("EVIDENCIA DE EJECUCIÓN - ESTUDIANTE: NASLY")
    print("FECHA: 6/5/26 | HORA: 11:12")
    print("=" * 50)

    print("\n--- RECTÁNGULO ---")
    r = Rectangulo(10, 5)
    print(r)
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())

    print("\n--- CÍRCULO ---")
    c = Circulo(7)
    print(c)
    print("Área:", round(c.area(), 2))
    print("Perímetro:", round(c.perimetro(), 2))

    print("\n--- VALIDACIÓN ---")
    error = Rectangulo(-5, 20)
    print("Base corregida:", error.base)
