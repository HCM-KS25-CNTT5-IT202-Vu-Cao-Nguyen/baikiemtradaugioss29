from abc import ABC, abstractmethod


class BaseCharacter(ABC):
    def __init__(self, base_hp):
        self.__base_hp = base_hp

    @property
    def base_hp(self):
        return self.__base_hp

    @abstractmethod
    def attack_enemy(self):
        pass

    def __add__(self, other):
        if isinstance(other, BaseCharacter):
            return int(self.base_hp + other.base_hp)
        return 0


class MagicalStance:
    def attack_enemy(self):
        return 150.0


class Warrior(BaseCharacter):
    def __init__(self, base_hp, strength):
        super().__init__(base_hp)
        self.strength = strength

    def attack_enemy(self):
        return self.strength * 2.5


class Spellblade(Warrior, MagicalStance):
    def __init__(self, base_hp, strength):
        Warrior.__init__(self, base_hp, strength)

    def attack_enemy(self):
        dmg_physical = Warrior.attack_enemy(self)
        dmg_magic = MagicalStance.attack_enemy(self)
        return dmg_physical + dmg_magic


class VolcanoZone:
    def activate_buff(self, character):
        print(
            f"[VolcanoZone] Kích hoạt hiệu ứng Núi lửa! Nhân vật {type(character).__name__} nhận thêm 20% sát thương.")
        return 1.2


def apply_battleground_effect(environment, character):
    if hasattr(environment, 'activate_buff'):
        multiplier = environment.activate_buff(character)
        print(f"[System] Hiệu ứng môi trường đã kích hoạt. Hệ số: {multiplier}")
    else:
        print("[System] Môi trường không có hiệu ứng đặc biệt.")


current_hero = None

while True:
    print("\n=== RPG CHARACTER MANAGER ===")
    print("1. Khởi tạo Ma kiếm sĩ (Spellblade)")
    print("2. Giao tranh & Kích hoạt môi trường")
    print("3. Thoát")
    choice = input("Chọn chức năng: ")

    if choice == '1':
        try:
            hp = int(input("Nhập HP cơ bản: "))
            strength = int(input("Nhập Strength (Sức mạnh): "))

            current_hero = Spellblade(hp, strength)

            total_hp = current_hero + current_hero
            print(f"Spellblade. HP: {current_hero.base_hp}, Strength: {current_hero.strength}")
            print(f"Tổng HP = {total_hp}")

            print(f"{' -> '.join([cls.__name__ for cls in Spellblade.__mro__])}")

        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ cho HP và Strength.")

    elif choice == '2':
        if current_hero is None:
            print("Lỗi: Chưa khởi tạo nhân vật! Vui lòng chọn Chức năng 1 trước.")
            continue

        dmg = current_hero.attack_enemy()
        print(f"Attack! Ma kiếm sĩ gây ra {dmg} sát thương tổng hợp.")

        volcano = VolcanoZone()
        apply_battleground_effect(volcano, current_hero)

    elif choice == '3':
        print("Đang thoát hệ thống...")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
