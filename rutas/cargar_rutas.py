from .models import Ruta, Parada

def cargar_rutas_y_paradas():
    rutas = {
        "majayura": [
            "Terminal", "SAO-Cuatro Vias", "Texas", "Bomba Las Ballenas", "Portal",
            "Calle 15 con carrera 26", "Calle 14H con carrera 26", "Calle 14H-Tienda",
            "Calle 14h con carrera 36", "Calle 14H con carrera 37", "Calle 14H con carrera 39",
            "Supergiros", "Carrera 50 con calle 14H", "Carrera 50-Tienda",
            "Los deseos", "Carrera 50 con calle 15"
        ],
        "centro_coquivacoa": [
            "Estatua de Los embarradores", "Calle 7 con carrera 5", "Calle 7 con carrera 6",
            "Calle 7 con carrera 10", "Calle 7 con carrera 11", "Calle 7 con carrera 12 panadería La Fontana",
            "Carrera 15 con carrera 10", "Carrera 15 con carrera 12A", "Calle 13 con carrera 16",
            "Calle 13 con carrera 17", "Calle 13 con carrera 18A", "Calle 13 con carrera 20",
            "Carrera 20 20 con calle 14A", "Calle 14C con carrera 20", "Calle 14C con carrera 18A",
            "Carrera 18 con carrera 14D", "Carrera 18 con carrera 15"
        ],
        "marbella": [
            "Round Point", "Movistar", "Terminal", "Corona", "Iglesia Pentecostal",
            "Contraloría", "Liceo Padilla", "Carrera 20 con calle 12b", "Parque Marbella",
            "Tienda Marbella", "Calle 13b con carrera 24", "Calle 14A con carrera 26",
            "Tienda El Sol", "Parque Jorge Pérez", "Calle 14C con carrera 26",
            "Calle 14C con carrera 14", "Calle 14C con carrera 22", "Calle 14C con carrera 18"
        ],
        "calle15": [
            "Vivero", "Villa Comfamiliar", "Toyota", "Piscina de los Mendoza",
            "Round Point", "Movistar", "Terminal", "Corona", "Iglesia Pentecostal",
            "SAO-Cuatro Vias", "Texas", "Bomba Las Ballenas", "Portal de Comfamiliar",
            "Hotel Los Remedios", "La Postobón"
        ],
        "20-las_tunas": [
            "La Virgencita", "Calle 20 con carrera 7A", "Calle 20 con carrera 8", "Calle 20 con carrera 11",
            "Calle 20 con carrera 11A", "Calle 20 con carrera 12", "Calle 20 con carrera 12C",
            "Calle 20 con carrera 14", "SENA", "Carrera 15 con calle 25 esquina",
            "Lavadero Maria Mina", "Calle 28A con carrera 18", "Calle 28A con carrera 21",
            "Parque Las Tunas", "Calle 28A con carrera 26 Colegio IPC", "Calle 33 con carrera 26",
            "Calle 33 con carrera 28", "Calle 33 con carrera 32", "Gallera Quille"
        ],
        "27-37": [
            "Calle 27 con carrera 7H", "Calle 27 con carrera 8", "Calle 27 con carrera 11 Bis",
            "Calle 27 con carrera 12", "Calle 27 con carrera 12C (Parquedero)", "Calle 27 con carrera 12C 14",
            "Carrera 14 con calle 27", "Tienda La Gran Colombia", "Ferreteria La Cosecha",
            "Calle 37 con carrera 13", "Calle 37 con carrera 12C Bis", "Calle 37 con carrera 12B",
            "Calle 37 con carrera 12 (El Guarda)", "Calle 37 con carrera 11 (Los Mangos)",
            "Calle 37 con carrera 10 (La Loma)", "Calle 37 con carrera 7H"
        ],
        "dividivi": [
            "Villa Victoria", "Villa del Mar", "Dividivi", "Entrada del Minuto de Dios",
            "Mega Colegio", "Calle 53", "Calle 51", "Calle 47", "Parque de La Vida",
            "Ísimo", "D1", "La 40"
        ]
    }

    for nombre_ruta, paradas in rutas.items():
        ruta_obj, creada = Ruta.objects.get_or_create(nombre=nombre_ruta)
        for parada in paradas:
            Parada.objects.get_or_create(ruta=ruta_obj, nombre=parada)

    print("✔ Rutas y paradas cargadas exitosamente.")
