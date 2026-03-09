"""シンプルなCLIサンプルプログラム。"""

from __future__ import annotations

import argparse
import sys


def greet(name: str) -> str:
    """名前を受け取って挨拶文を返す。"""
    return f"こんにちは、{name}さん！Pythonサンプルへようこそ。"


def build_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        description="名前を受け取って挨拶を表示するサンプルCLIです。"
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = build_parser()
    parser.add_argument("name", nargs="?", help="挨拶したい相手の名前")
    args = parser.parse_args(argv)

    if args.name is None:
        parser.print_help()
        raise SystemExit(0)

    return args


def main() -> int:
    args = parse_args()
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
