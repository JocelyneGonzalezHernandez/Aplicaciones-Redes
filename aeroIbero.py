
import math
import datetime
import heapq

# Definición de las clases
class Ciudad:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Ruta:
    def __init__(self, origen, destino, tipo_viaje, distancia, tiempo, costo):
        self.origen = origen
        self.destino = destino
        self.tipo_viaje = tipo_viaje
        self.distancia = distancia
        self.tiempo = tiempo
        self.costo = costo

class Reservacion:
    def __init__(self, origen, destino, fecha, nombre_pasajero, fecha_nacimiento, nacionalidad, raza, telefono, correo):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.nombre_pasajero = nombre_pasajero
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.raza = raza
        self.telefono = telefono
        self.correo = correo
        self.numero_cliente = self.generar_numero_cliente()
        self.numero_vuelo = self.generar_numero_vuelo()
        self.salas_espera = self.asignar_sala_espera()
        self.puertas_embarque = self.asignar_puerta_embarque()
        self.costo = self.calcular_costo()
        self.tiempo = self.calcular_tiempo()

    def generar_numero_cliente(self):
        return hash(self.nombre_pasajero + self.telefono)

    def generar_numero_vuelo(self):
        now = datetime.datetime.now()
        return f"VUELO-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}"

    def asignar_sala_espera(self):
        if ciudades[self.origen].tipo == "Importante" or ciudades[self.destino].tipo == "Importante":
            return "Sala A"
        else:
            return "Sala B"

    def asignar_puerta_embarque(self):
        if ciudades[self.origen].tipo == "Importante" or ciudades[self.destino].tipo == "Importante":
            return "Puerta 1"
        else:
            return "Puerta 2"

    def calcular_costo(self):
        return graph[self.origen][self.destino][2]

    def calcular_tiempo(self):
        return graph[self.origen][self.destino][1]

    def generar_pase_abordar(self):
        pase_abordar = {
            'Aeropuerto': self.origen,
            'Sala de espera': self.salas_espera,
            'Puerta de embarque': self.puertas_embarque,
            'Hora': 'Por determinar',
            'Fecha': self.fecha,
            'Origen': self.origen,
            'Destino': self.destino,
            'Ruta': f'{self.origen} - {self.destino}',
            'Número de vuelo': self.numero_vuelo,
            'Nombre del pasajero': self.nombre_pasajero,
            'Raza': self.raza,
            'Nacionalidad': self.nacionalidad,
            'Precio del viaje': self.costo,
            'Tiempo estimado del viaje': self.tiempo
        }
        return pase_abordar

# Función para mostrar las opciones de ruta
def mostrar_opciones_ruta(origen, destino):
    distancias, tiempos, costos = dijkstra(graph, origen)
    distancia_optima = distancias[destino]
    tiempo_optimo = tiempos[destino]
    costo_optimo = costos[destino]

    print("Opciones de Ruta:")
    print(f"1. Ruta más corta por distancia: {distancia_optima} Km")
    print(f"2. Ruta óptima por tiempo: {tiempo_optimo} Hrs")
    print(f"3. Ruta más económica por precio: ${costo_optimo}")

# Algoritmo de Dijkstra para encontrar rutas más cortas
def dijkstra(graph, start):
    distances = {node: math.inf for node in graph}
    times = {node: math.inf for node in graph}
    costs = {node: math.inf for node in graph}
    previous_node = {node: None for node in graph}
    distances[start] = 0
    times[start] = 0
    costs[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, data in graph[current_node].items():
            distance, time, cost = data
            total_distance = distances[current_node] + distance
            total_time = times[current_node] + time
            total_cost = costs[current_node] + cost
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                times[neighbor] = total_time
                costs[neighbor] = total_cost
                previous_node[neighbor] = current_node
                heapq.heappush(queue, (total_distance, neighbor))
    
    return distances, times, costs

# Crear instancias de las ciudades y rutas con los datos proporcionados
ciudades = {
    "La Comarca": Ciudad("La Comarca", "Ordinaria"),
    "Rivendel": Ciudad("Rivendel", "Importante"),
    "Reino del Bosque": Ciudad("Reino del Bosque", "Ordinaria"),
    "Rohan": Ciudad("Rohan", "Ordinaria"),
    "Telmar": Ciudad("Telmar", "Importante"),
    "Gondor": Ciudad("Gondor", "Importante"),
    "Mordor": Ciudad("Mordor", "Ordinaria"),
    "Isengard": Ciudad("Isengard", "Ordinaria"),
    "Moria": Ciudad("Moria", "Ordinaria"),
    "Erebor": Ciudad("Erebor", "Ordinaria"),
    "Narnia": Ciudad("Narnia", "Importante"),
    "Ciudad Esmeralda": Ciudad("Ciudad Esmeralda", "Importante"),
    "Winkie": Ciudad("Winkie", "Ordinaria"),
    "Charn": Ciudad("Charn", "Ordinaria"),
    "Munchkin": Ciudad("Munchkin", "Ordinaria")
}

# Definir las rutas con los datos proporcionados
graph = {
    "La Comarca": {"Rivendel": (500.00, 1.5, 1550.00)},
    "Rivendel": {"La Comarca": (500.00, 1.5, 1850.00), "Reino del Bosque": (950.00, 2.4, 2400.00),
                 "Rohan": (550.00, 1.6, 1975.00), "Telmar": (1100.00, 5.2, 3750.00)},
    "Reino del Bosque": {"Rivendel": (950.00, 2.4, 2100.00), "Erebor": (500.00, 4.5, 2450.00)},
    "Rohan": {"Rivendel": (550.00, 1.6, 1675.00), "Isengard": (400.00, 1.3, 1300.00), "Gondor": (600.00, 1.7, 1550.00)},
    "Telmar": {"Narnia": (400.00, 1.3, 1800.00), "Rivendel": (1100.00, 5.2, 3750.00)},
    "Gondor": {"Rohan": (600.00, 1.7, 2350.00), "Erebor": (1250.00, 3.0, 4225.00), "Mordor": (450.00, 3.4, 3125.00),
               "Narnia": (550.00, 4.1, 1975.00), "Ciudad Esmeralda": (1100.00, 5.2, 4250.00)},
    "Mordor": {"Isengard": (550.00, 1.6, 1375.00), "Winkie": (600.00, 3.2, 1500.00)},
    "Isengard": {"Rohan": (400.00, 1.3, 1300.00), "Moria": (400.00, 1.3, 1100.00)},
    "Moria": {"Isengard": (400.00, 1.3, 1300.00), "Erebor": (900.00, 2.3, 2225.00)},
    "Erebor": {"Moria": (900.00, 2.3, 2000.00), "Gondor": (1250.00, 3.0, 3525.00)},
    "Narnia": {"Telmar": (400.00, 1.3, 1500.00), "Charn": (450.00, 3.4, 3125.00), "Gondor": (550.00, 4.1, 2875.00),
               "Ciudad Esmeralda": (1300.00, 5.6, 4750.00)},
    "Ciudad Esmeralda": {"Munchkin": (200.00, 0.9, 1600.00), "Winkie": (300.00, 3.1, 2250.00), "Gondor": (1100.00, 5.2, 4250.00),
                         "Narnia": (1300.00, 5.6, 4750.00)},
    "Winkie": {"Ciudad Esmeralda": (300.00, 2.1, 1950.00), "Mordor": (600.00, 3.2, 750.00), "Charn": (700.00, 3.4, 875.00)},
    "Charn": {"Narnia": (450.00, 3.4, 1225.00), "Winkie": (700.00, 3.4, 875.00)},
    "Munchkin": {"Ciudad Esmeralda": (200.00, 0.9, 1600.00)}
}

# Solicitar al usuario los detalles del viaje
nombre_origen = input("Ingrese la ciudad de origen: ")
nombre_destino = input("Ingrese la ciudad de destino: ")
fecha_viaje = input("Ingrese la fecha del viaje (DD/MM/AAAA): ")

# Mostrar opciones de ruta al usuario
if nombre_origen in graph and nombre_destino in graph:
    mostrar_opciones_ruta(nombre_origen, nombre_destino)
    
    # Obtener la opción de ruta deseada del usuario
    opcion_ruta = input("Seleccione la opción de ruta deseada (1/2/3): ")
    
    # Validar la opción de ruta
    if opcion_ruta not in ['1', '2', '3']:
        print("Opción de ruta no válida.")
    else:
        # Obtener detalles de la reservación
        nombre_pasajero = input("Ingrese su nombre: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
        nacionalidad = input("Ingrese su nacionalidad: ")
        raza = input("Ingrese su raza: ")
        telefono = input("Ingrese su número de teléfono: ")
        correo = input("Ingrese su correo electrónico: ")
        
        # Crear instancia de la reservación
        reservacion = Reservacion(nombre_origen, nombre_destino, fecha_viaje, nombre_pasajero, fecha_nacimiento, nacionalidad, raza, telefono, correo)
        
        # Generar y mostrar el pase de abordar
        pase_abordar = reservacion.generar_pase_abordar()
        print("\nPase de Abordar:")
        for key, value in pase_abordar.items():
            print(f"{key}: {value}")
else:
    print("Una o ambas ciudades no están en la lista de ciudades disponibles.")
