class Cuenta:
  def __init__(self, nombre, cantidad=0):
    self.nombre=nombre
    self.cantidad=cantidad
  def mostrar(self):
    print("Titular Cuenta:",self.nombre)
    print("Saldo actual $", self.cantidad,)
  def ingresar(self, cantidad):
    self.cantidad = self.cantidad + cantidad
  def retirar(self, cantidad):
   if (cantidad > 0):
    self.cantidad = self.cantidad - cantidad
    print("Extraccion $",cantidad )
    print("Saldo actualizado $", self.cantidad)
cuenta=Cuenta("Juank", 5000)
cuenta.ingresar(3000)
cuenta.mostrar()
cuenta.retirar(10000)