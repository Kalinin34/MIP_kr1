import time

# Класс, представляющий одно состояние игры в дереве игры
class GameTreeNode:
    def __init__(self, number, player_turn, player_score, ai_score, bank, depth=0):
        self.number = number  # Текущее число в игре
        self.player_turn = player_turn  # True - ходит человек, False - ходит AI
        self.player_score = player_score  # Очки человека
        self.ai_score = ai_score  # Очки AI
        self.bank = bank  # Очки в банке
        self.depth = depth  # Глубина в дереве (расстояние от начального состояния)
        self.children = []  # Список дочерних состояний (следующих ходов)
        self.move = None  # Какое деление применено (2 или 3)

# Функция оценки состояния игры (чем выше - тем лучше для AI)
def evaluate_state(node):
    score_diff = node.ai_score - node.player_score  # Разница очков между AI и игроком
    bank_bonus = node.bank if not node.player_turn else -node.bank  # Учет влияния банка
    return score_diff + 0.5 * bank_bonus  # Итоговая оценка состояния

# Генерация всех возможных следующих ходов из текущего состояния
def generate_children(node):
    for move in [2, 3]:  # Попробовать деление на 2 и 3
        if node.number % move == 0:  # Делить можно только если число делится без остатка
            next_number = node.number // move

            # Копируем текущие очки и банк
            player_score = node.player_score
            ai_score = node.ai_score
            bank = node.bank

            # Расчет изменения очков после хода
            if node.player_turn:
                if next_number % 2 == 0:
                    player_score += 1  # Если результат четный — +1 очко
                else:
                    player_score -= 1  # Если нечетный — -1 очко
            else:
                if next_number % 2 == 0:
                    ai_score += 1
                else:
                    ai_score -= 1

            # Увеличение банка, если число заканчивается на 0 или 5
            if str(next_number)[-1] in ['0', '5']:
                bank += 1

            # Если число стало 2 — игрок получает банк
            if next_number == 2:
                if node.player_turn:
                    player_score += bank
                else:
                    ai_score += bank
                bank = 0  # Банк обнуляется

            # Создание нового узла дерева с новым состоянием
            child = GameTreeNode(
                number=next_number,
                player_turn=not node.player_turn,  # Меняется очередь хода
                player_score=player_score,
                ai_score=ai_score,
                bank=bank,
                depth=node.depth + 1
            )
            child.move = move  # Сохраняем, каким делением это состояние получено (2 или 3)
            node.children.append(child)  # Добавляем в список потомков

# Алгоритм минимакс — AI старается максимизировать итоговую оценку
# depth — глубина поиска
# maximizing_player — True, если в этом шаге AI максимизирует оценку

def minimax(node, depth, maximizing_player):
    if depth == 0 или node.number in [2, 3]:
        return evaluate_state(node), node.move  # Если достигли конца — возвращаем оценку

    generate_children(node)  # Генерируем возможные ходы

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for child in node.children:
            eval, _ = minimax(child, depth - 1, False)  # Следующий ход — соперника
            if eval > max_eval:
                max_eval = eval
                best_move = child.move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for child in node.children:
            eval, _ = minimax(child, depth - 1, True)  # Следующий ход — AI
            if eval < min_eval:
                min_eval = eval
                best_move = child.move
        return min_eval, best_move

# Алгоритм альфа-бета отсечения — ускоренный минимакс
# alpha — наилучшая оценка для максимизирующего игрока (AI)
# beta — наилучшая оценка для минимизирующего игрока (человека)

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 или node.number in [2, 3]:
        return evaluate_state(node), node.move

    generate_children(node)

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for child in node.children:
            eval, _ = alpha_beta(child, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child.move
            alpha = max(alpha, eval)
            if beta <= alpha:  # Обрезка лишних веток
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for child in node.children:
            eval, _ = alpha_beta(child, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child.move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Главная функция, которая вызывается для выбора хода AI
# Выбирается алгоритм и глубина просмотра

def ai_decide_move(current_number, player_turn, player_score, ai_score, bank, algorithm="minimax", max_depth=4):
    root = GameTreeNode(current_number, player_turn, player_score, ai_score, bank)
    start_time = time.time()

    if algorithm == "minimax":
        _, best_move = minimax(root, max_depth, not player_turn)
    elif algorithm == "alphabeta":
        _, best_move = alpha_beta(root, max_depth, float('-inf'), float('inf'), not player_turn)
    else:
        raise ValueError("Неизвестный алгоритм")  # Ошибка, если указан неверный алгоритм

    duration = time.time() - start_time  # Время, затраченное на расчёт хода
    return best_move, duration
