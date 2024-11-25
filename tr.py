import time
import random
import os

def clear_screen():
    """Ekranni tozalash."""
    os.system("cls" if os.name == "nt" else "clear")

def print_road(player_pos, obstacles, level, score):
    """Yo‘lni chizish."""
    road = ["|       |"] * 10
    for obs in obstacles:
        if 0 <= obs[1] < 10:
            road[obs[1]] = road[obs[1]][:obs[0] + 1] + "#" + road[obs[1]][obs[0] + 2:]
    road[9] = road[9][:player_pos + 1] + "P" + road[9][player_pos + 2:]
    clear_screen()
    for line in road:
        print(line)
    print("=========")
    print(f"Level: {level} | Score: {score}")

def move_obstacles(obstacles):
    """To‘siqlarni pastga siljitish."""
    return [[obs[0], obs[1] + 2] for obs in obstacles if obs[1] < 10]

def check_collision(player_pos, obstacles):
    """To‘qnashuvni tekshirish."""
    for obs in obstacles:
        if obs[1] == 9 and obs[0] == player_pos:  # Agar to‘siq oxirgi qatorda bo‘lsa va pozitsiya bir xil bo‘lsa
            return True
    return False

def main():
    while True:
        player_pos = 3  # Mototsiklning boshlang‘ich pozitsiyasi
        obstacles = []  # To‘siqlar ro‘yxati
        score = 0       # Ball
        level = 1       # Boshlang‘ich daraja
        max_score = 150 # G‘alaba uchun kerak bo‘lgan ball

        print("Trafik Rider: Mototsikl Versiyasi")
        print("O‘yinni boshlash uchun ENTER tugmasini bosing!")
        input()

        try:
            while True:
                # Darajalar va tezlikni boshqarish
                if score >= 150:
                    clear_screen()
                    print("W I N N E R !")
                    break
                elif score >= 100:
                    level = 3
                    speed = 0.2
                elif score >= 50:
                    level = 2
                    speed = 0.3
                else:
                    level = 1
                    speed = 0.5

                # To‘siqlarni qo‘shish
                if random.random() < 0.5:  # To‘siq paydo bo‘lish ehtimoli
                    obstacles.append([random.randint(1, 5), 0])

                # To‘siqlarni harakatlantirish
                obstacles = move_obstacles(obstacles)

                # To‘qnashuvni tekshirish
                if check_collision(player_pos, obstacles):
                    clear_screen()
                    print("To‘qnashuv yuz berdi! O‘yin qayta boshlanmoqda...")
                    time.sleep(2)  # 2 soniya kutish
                    break  # O'yinni qayta boshlash uchun tashqi siklga qaytish

                # Yo‘lni chizish
                print_road(player_pos, obstacles, level, score)

                # Harakatni amalga oshirish
                if os.name == "nt":  # Windows uchun
                    import msvcrt
                    if msvcrt.kbhit():
                        action = msvcrt.getch().decode("utf-8").lower()
                        if action == "a" and player_pos > 1:
                            player_pos -= 1
                        elif action == "d" and player_pos < 5:
                            player_pos += 1
                else:  # Unix/Linux uchun
                    import sys, select
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        action = sys.stdin.read(1).lower()
                        if action == "a" and player_pos > 1:
                            player_pos -= 1
                        elif action == "d" and player_pos < 5:
                            player_pos += 1

                score += 1
                time.sleep(speed)  # Tezlikni darajaga qarab boshqarish

        except KeyboardInterrupt:
            print("\nO‘yin to‘xtatildi.")
            break

if __name__ == "__main__":
    main()
