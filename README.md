# サンプルプログラム

最小構成の Python CLI サンプルです。名前を受け取って挨拶します。

## 実行方法（そのままコピペでOK）

1. このディレクトリに移動

```bash
cd /workspace/test
```

2. プログラムを実行

```bash
python3 sample.py 太郎
```

## ヘルプを見る

```bash
python3 sample.py --help
```

## 実行例

```text
こんにちは、太郎さん！Pythonサンプルへようこそ。
```


## テスト実行

```bash
python3 -m unittest -v
```


## ヘルプが見れないとき

- `sample.py` がある場所で実行してください（`cd /workspace/test`）。
- どの場所からでも実行したい場合は、次を使ってください。

```bash
python3 /workspace/test/sample.py --help
```
