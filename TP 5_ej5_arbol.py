
#! Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic
#! Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

#! a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
#! que indica si es un héroe o un villano, True y False respectivamente;

#! b. listar los villanos ordenados alfabéticamente;

#! c. mostrar todos los superhéroes que empiezan con C;

#! d. determinar cuántos superhéroes hay el árbol;

#! e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#! encontrarlo en el árbol y modificar su nombre;

#! f. listar los superhéroes ordenados de manera descendente;

#! g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y
#! otro a los villanos, luego resolver las siguiente tareas:
#! I. determinar cuántos nodos tiene cada árbol;
#! II. realizar un barrido ordenado alfabéticamente de cada árbol.

from arbol_avl import BinaryTree

class AVLTreeMarvel(BinaryTree):
    
    # Punto b: Listar villanos en orden alfabético
    def listar_villanos(self):
        """Recorre el árbol en orden y muestra los nombres de los villanos (is_hero == False)"""
        print("Villanos ordenados alfabéticamente:")
        self.inorden_villanos()  # Utiliza el método ya definido para hacer un recorrido inorden

    # Punto c: Mostrar superhéroes que empiezan con C
    def mostrar_superheroes_con_C(self):
        """Muestra todos los superhéroes cuyo nombre comienza con la letra 'C'"""
        print("Superhéroes que comienzan con 'C':")
        self.inorden_superheros_start_with('C')  # Usa el método ya definido para el barrido

    # Punto d: Contar superhéroes en el árbol
    def contar_superheroes(self):
        """Cuenta la cantidad de nodos en el árbol que representan superhéroes (is_hero == True)"""
        num_heroes = self.contar_super_heroes()  # Cuenta héroes usando el método que ya tienes
        print(f"Cantidad de superhéroes en el árbol: {num_heroes}")

    # Punto e: Modificar el nombre de Doctor Strange
    def modificar_doctor_strange(self):
        """Realiza una búsqueda aproximada para encontrar a Doctor Strange y corregir su nombre"""
        nodo_strange = self.search("Strange")  # Realiza una búsqueda de "Strange"
        if nodo_strange is not None:  # Si encuentra algo
            print(f"Doctor Strange encontrado: {nodo_strange.value}, modificando su nombre...")
            nodo_strange.value = "Doctor Strange"  # Modifica el nombre al correcto
        else:
            print("Doctor Strange no encontrado")

    # Punto f: Listar superhéroes en orden descendente
    def listar_superheroes_descendente(self):
        """Muestra todos los superhéroes ordenados de manera descendente usando un recorrido inverso"""
        def __inorden_descendente(root):
            if root is not None:
                __inorden_descendente(root.right)  # Recorre primero el subárbol derecho
                if root.other_value.get('is_hero') is True:  # Si es héroe, lo imprime
                    print(root.value)
                __inorden_descendente(root.left)  # Luego recorre el subárbol izquierdo
        if self.root is not None:
            print("Superhéroes en orden descendente:")
            __inorden_descendente(self.root)

    # Punto g: Generar bosque (un árbol de héroes y otro de villanos)
    def generar_bosque(self):
        """Genera dos árboles separados: uno para héroes y otro para villanos"""
        arbol_heroes = BinaryTree()  # Árbol para los héroes
        arbol_villanos = BinaryTree()  # Árbol para los villanos

        def __separar_arboles(root):
            """Función recursiva para separar héroes y villanos en diferentes árboles"""
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    # Si el nodo es un héroe, lo insertamos en el árbol de héroes
                    arbol_heroes.insert_node(root.value, root.other_value)
                else:
                    # Si es villano, lo insertamos en el árbol de villanos
                    arbol_villanos.insert_node(root.value, root.other_value)
                # Llamada recursiva para continuar recorriendo
                __separar_arboles(root.left)
                __separar_arboles(root.right)

        # Llamada inicial para empezar la separación
        __separar_arboles(self.root)

        # I. Contar nodos de cada árbol
        print(f"Número de héroes en el árbol: {arbol_heroes.contar_super_heroes()}")

        # Contar villanos de forma recursiva
        def contar_villanos(root):
            """Cuenta los nodos de un árbol, sin distinguir entre héroes y villanos"""
            if root is None:
                return 0
            else:
                return 1 + contar_villanos(root.left) + contar_villanos(root.right)

        print(f"Número de villanos en el árbol: {contar_villanos(arbol_villanos.root)}")

        # II. Barrido ordenado de cada árbol
        print("Héroes ordenados alfabéticamente:")
        arbol_heroes.inorden()  # Barrido inorden de héroes
        print("Villanos ordenados alfabéticamente:")
        arbol_villanos.inorden_villanos()  # Barrido inorden de villanos

# --- Ejemplo de uso ---

# Creación del árbol AVL y carga de datos de héroes y villanos
arbol_mcu = AVLTreeMarvel()

# Insertar héroes y villanos de MCU
arbol_mcu.insert_node("Captain America", {"is_hero": True})
arbol_mcu.insert_node("Iron Man", {"is_hero": True})
arbol_mcu.insert_node("Thanos", {"is_hero": False})
arbol_mcu.insert_node("Doctor Strange", {"is_hero": True})
arbol_mcu.insert_node("Hela", {"is_hero": False})
arbol_mcu.insert_node("Black Panther", {"is_hero": True})
arbol_mcu.insert_node("Ultron", {"is_hero": False})
arbol_mcu.insert_node("Loki", {"is_hero": False})
arbol_mcu.insert_node("Scarlet Witch", {"is_hero": True})

# Realizar las tareas

# Punto b: Listar villanos ordenados alfabéticamente
arbol_mcu.listar_villanos()

# Punto c: Mostrar superhéroes que empiezan con 'C'
arbol_mcu.mostrar_superheroes_con_C()

# Punto d: Contar superhéroes en el árbol
arbol_mcu.contar_superheroes()

# Punto e: Modificar el nombre de Doctor Strange
arbol_mcu.modificar_doctor_strange()

# Punto f: Listar superhéroes en orden descendente
arbol_mcu.listar_superheroes_descendente()

# Punto g: Generar el bosque de héroes y villanos
arbol_mcu.generar_bosque()
