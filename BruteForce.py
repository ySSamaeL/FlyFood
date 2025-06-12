import time
from typing import List, Tuple, Dict, Optional
import matplotlib.pyplot as plt

Point = Tuple[int, int]

def manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_total_route_cost(
    start_point: Point,
    route: Tuple[str, ...],
    delivery_points: Dict[str, Point]
) -> int:
    current_point = start_point
    total_cost = 0

    for point_index in route:
        next_point = delivery_points[point_index]
        total_cost += manhattan_distance(current_point, next_point)
        current_point = next_point

    total_cost += manhattan_distance(current_point, start_point)
    return total_cost

def _generate_route_permutations(points: List[str]) -> List[List[str]]:
    all_permutations: List[List[str]] = []

    def backtrack(start_index: int):
        if start_index == len(points):
            all_permutations.append(points[:])
            return

        for i in range(start_index, len(points)):
            points[start_index], points[i] = points[i], points[start_index]
            backtrack(start_index + 1)
            points[start_index], points[i] = points[i], points[start_index]

    backtrack(0)
    return all_permutations

def find_optimal_route(
    start_point: Point,
    delivery_points: Dict[str, Point]
) -> Tuple[Optional[int], Optional[List[str]]]:
    point_list = list(delivery_points.keys())
    all_possible_routes = _generate_route_permutations(point_list)
    min_cost: Optional[int] = None
    optimal_route: Optional[List[str]] = None

    for route in all_possible_routes:
        cost = calculate_total_route_cost(start_point, tuple(route), delivery_points)

        if min_cost is None or cost < min_cost:
            min_cost = cost
            optimal_route = route

    return min_cost, optimal_route

def plot_route(start_point: Point, delivery_points: Dict[str, Point], 
               route: List[str], total_distance: int, exec_time: float):
    plt.figure(figsize=(12, 8))

    # Extrai coordenadas
    x_coords = [p[1] for p in delivery_points.values()]  # Coluna (eixo X)
    y_coords = [p[0] for p in delivery_points.values()]  # Linha (eixo Y)
    labels = list(delivery_points.keys())

    # Plota pontos de entrega
    plt.scatter(x_coords, y_coords, c='blue', s=100, label='Pontos de entrega')

    # Plota ponto de partida
    plt.scatter(start_point[1], start_point[0], c='red', marker='s', s=100, label='Partida (R)')

    # Desenha a rota
    current_point = start_point
    for point in route:
        next_point = delivery_points[point]
        # Linha horizontal primeiro
        plt.plot([current_point[1], next_point[1]], [current_point[0], current_point[0]], 'r-')
        # Linha vertical depois
        plt.plot([next_point[1], next_point[1]], [current_point[0], next_point[0]], 'r-')
        current_point = next_point

    # Volta ao ponto inicial
    plt.plot([current_point[1], start_point[1]], [current_point[0], current_point[0]], 'r-')
    plt.plot([start_point[1], start_point[1]], [current_point[0], start_point[0]], 'r-')

    # Adiciona rótulos
    for label, point in delivery_points.items():
        plt.annotate(label, (point[1], point[0]), textcoords="offset points", xytext=(0,5), ha='center')

    plt.title(f'Rota Ótima - Distância: {total_distance} | Tempo: {exec_time:.4f}s')
    plt.xlabel('Coluna')
    plt.ylabel('Linha')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Lê a primeira linha que contém as dimensões
    first_line = input().strip()
    lines, cols = map(int, first_line.split())

    # Lê as linhas subsequentes que contêm a matriz
    start_point: Optional[Point] = None
    delivery_points: Dict[str, Point] = {}

    for i in range(lines):
        row_points = input().strip().split()
        for j, point_char in enumerate(row_points):
            if point_char == 'R':
                start_point = (i, j)
            elif point_char != '0':
                # Mantém o caractere exatamente como está (considera 'a' e 'A' diferentes)
                delivery_points[point_char] = (i, j)

    if start_point is None:
        print("Erro: Ponto de partida 'R' não encontrado no mapa.")
    else:
        print(f"Calculando a rota ótima para {len(delivery_points)} pontos de entrega...")

        start_timer = time.time()
        cost, route = find_optimal_route(start_point, delivery_points)
        end_timer = time.time()
        duration = end_timer - start_timer

        print("-" * 40)
        if route:
            print(f"Solução ótima para a rota: {' '.join(route)}")
            print(f"Distância percorrida: {cost}")
            print(f"Tempo de execução: {duration:.4f} segundos")
            print("-" * 40)

            # Plotar a rota
            plot_route(start_point, delivery_points, route, cost, duration)
        else:
            print("Nenhum ponto de entrega encontrado.")
            print("-" * 40)
