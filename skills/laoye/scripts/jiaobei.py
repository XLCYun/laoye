import json
import random
from pathlib import Path


STANDING_CUP_PROBABILITY = 0.0015
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DATA_FILE = SKILL_DIR / "data" / "yudi_lingqian_all_28.json"

SINGLE_CUP_NAMES = {
    (0, 0): "阴杯",
    (0, 1): "圣杯",
    (1, 0): "圣杯",
    (1, 1): "笑杯",
}

SHORT_CUP_NAMES = {
    "圣杯": "圣",
    "笑杯": "笑",
    "阴杯": "阴",
}

TRIPLE_PATTERNS = {
    ("圣", "圣", "圣"): "三圣杯",
    ("笑", "笑", "笑"): "三笑杯",
    ("阴", "阴", "阴"): "三阴杯",
}


def load_signs():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    signs = data.get("signs", [])
    if not signs:
        raise ValueError(f"{DATA_FILE} 中没有 signs 数据。")

    sign_map = {}
    for sign in signs:
        cup_type = sign.get("茭杯型")
        sign_map[cup_type] = sign

    return sign_map


def build_expected_cup_types():
    expected = {"竖杯"}
    values = tuple(SHORT_CUP_NAMES.values())
    for first in values:
        for second in values:
            for third in values:
                pattern = (first, second, third)
                expected.add(TRIPLE_PATTERNS.get(pattern, "".join(pattern)))
    return expected


def validate_sign_map(sign_map):
    expected = build_expected_cup_types()
    actual = set(sign_map)

    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        problems = []
        if missing:
            problems.append(f"JSON 缺少杯型: {missing}")
        if extra:
            problems.append(f"JSON 出现未知杯型: {extra}")
        raise ValueError("；".join(problems))


def throw_single_cup():
    first = random.randint(0, 1)
    second = random.randint(0, 1)
    return SINGLE_CUP_NAMES[(first, second)]


def normalize_cup_pattern(cups):
    short_names = tuple(SHORT_CUP_NAMES[cup] for cup in cups)
    return TRIPLE_PATTERNS.get(short_names, "".join(short_names))


def draw_cup_pattern():
    if random.random() < STANDING_CUP_PROBABILITY:
        return "立杯", "竖杯", []

    cups = [throw_single_cup() for _ in range(3)]
    cup_pattern = normalize_cup_pattern(cups)
    return "三次掷杯", cup_pattern, cups


def print_sign_result(draw_kind, cup_pattern, cups, sign):
    print(f"抽签方式: {draw_kind}")
    if cups:
        print(f"三次杯型: {'、'.join(cups)}")
    print(f"对应茭杯型: {cup_pattern}")
    print()
    print(sign["签号"])
    print(f"标题: {sign['标题']}")
    print(f"茭杯型: {sign['茭杯型']}")
    print(f"签级: {sign['签级']}")
    print(f"卦曰: {sign['卦']}")
    print(f"诗曰: {sign['诗']}")
    print(f"解曰: {sign['解']}")
    print("典故:")
    print(sign["典故"])


def main():
    sign_map = load_signs()
    validate_sign_map(sign_map)

    draw_kind, cup_pattern, cups = draw_cup_pattern()
    sign = sign_map.get(cup_pattern)
    if sign is None:
        raise ValueError(f"生成的杯型 {cup_pattern} 无法从 JSON 中找到对应签文。")

    print_sign_result(draw_kind, cup_pattern, cups, sign)


if __name__ == "__main__":
    main()
