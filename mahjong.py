from collections import deque
import random
from pprint import pprint
import itertools
from itertools import islice


class Pai:
    """麻雀パイ"""
    MANZU = [f'{i}m' for i in '123456789']
    PINZU = [f'{i}p' for i in '123456789']
    SOZU = [f'{i}s' for i in '123456789']
    ZIHAI = [f'{i}z' for i in '1234567']
    ALL_PAI = 4 * tuple(MANZU + SOZU + PINZU + ZIHAI)


class Dice:
    """サイコロを定義"""
    dice_1 = [1, 2, 3, 4, 5, 6]
    dice_2 = [1, 2, 3, 4, 5, 6]

    def roll_dice(self):
        """サイコロの目を返す"""
        index = random.randrange(0, 6)
        value_1 = self.dice_1[index]
        index = random.randrange(0, 6)
        value_2 = self.dice_2[index]

        return value_1 + value_2


class GuraSai:
    """２しか出ないグラ賽"""
    dice_1 = [1, 2, 3, 4, 5, 6]
    dice_2 = [1, 2, 3, 4, 5, 6]

    def roll_dice(self):
        return self.dice_1[0] + self.dice_2[0]


class Taku:
    """卓"""

    def __init__(self):
        self.all_pai = list(Pai.ALL_PAI)
        self.kaze = ['ton', 'nan', 'sha', 'pei']
        self.yama = []
        self.wang_pai = []
        self.dora = None

    def si_pai(self):
        """シーパイする"""
        random.shuffle(self.all_pai)

    def set_taku(self):
        """牌を４つの山に分ける"""
        pass

    def hai_pai(self):
        """配牌する"""
        pass

    def set_dora(self):
        """ドラをセット"""
        self.dora = self.wang_pai[5]


class Janshi:
    """雀士"""

    def __init__(self, name):
        self.name = name
        self.tehai = []
        self.ho = []
        self.score = 25000
        self.is_parent = False

    def be_parent(self):
        """親になる"""
        self.is_parent = True

    def be_child(self):
        """子になる"""
        self.is_parent = False

    def get_haipai(self, haipai):
        self.tehai = haipai

    def ri_pai(self):
        """理牌する"""
        pass

    def tsumo(self, pai):
        """ツモする"""
        pass

    def chi(self):
        """チー"""
        pass

    def pon(self):
        """ポン"""
        pass

    def an_kan(self):
        """暗槓"""
        pass

    def min_kan(self):
        """明槓"""
        pass

    def dai_min_kan(self):
        """大明槓"""
        pass

    def dahai(self, pai):
        """打牌する"""
        pass

    def add_score(self, score):
        """スコアを加える"""
        self.score += score

    def pay_score(self, score):
        """スコアを払う"""
        self.score -= score
