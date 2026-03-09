"""シンプルなCLIサンプルプログラム。"""

from __future__ import annotations

import argparse


def greet(name: str) -> str:
    """名前を受け取って挨拶文を返す。"""
    return f"こんにちは、{name}さん！Pythonサンプルへようこそ。"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="名前を受け取って挨拶を表示するサンプルCLIです。"
    )
    parser.add_argument("name", help="挨拶したい相手の名前")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
