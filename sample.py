"""シンプルなCLIサンプルプログラム。

使い方:
    python sample.py 太郎
"""

import sys


def greet(name: str) -> str:
    """名前を受け取って挨拶文を返す。"""
    return f"こんにちは、{name}さん！Pythonサンプルへようこそ。"


def main() -> int:
    if len(sys.argv) < 2:
        print("使い方: python sample.py <名前>")
        return 1

    name = sys.argv[1]
    print(greet(name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
