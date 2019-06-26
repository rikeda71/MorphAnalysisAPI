# MorphAnalysisAPI

以下の3つの形態素解析機をWebAPIで試せるようにしたもの

- [MeCab](https://taku910.github.io/mecab/)
  - mecab with [NEologd](https://github.com/neologd/mecab-ipadic-neologd)
- [JUMAN++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)
- [Sudachi](https://github.com/WorksApplications/SudachiPy) (SudachiPy)

## 必要なもの

- python3
  - requests
- Docker

## 使い方

### Docker Containerの起動

```shell
docker build . -t morph-analysis-api # wait a minute
docker run -t --rm -d -p 5000:5000 morph-analysis-api:latest
```

### Docker Containerの停止（削除）

```shell
docker stop `container_id`
```

### 形態素解析のテスト

```shell
python3 request.py
```

#### テスト用スクリプトの詳細

```shell
python3 request.py -h
usage: request.py [-h] [-s SENTENCE]
                  [-m {mecab,mecab-neologd,sudachi,jumanpp}]

optional arguments:
  -h, --help            show this help message and exit
  -s SENTENCE, --sentence SENTENCE
                        a japanese sentence. default=`すもももももももものうち`
  -m {mecab,mecab-neologd,sudachi,jumanpp}, --machine {mecab,mecab-neologd,sudachi,jumanpp}
                        choice morphological analysis machine. default=`mecab`
```

### APIの仕様

| HTTP method | end point | request parameters | request headers |
---- | ---- | ---- | ----
| POST | /mecab | sentence | Content-Type:application/json |
| POST | /mecab-neologd | sentence | Content-Type:application/json |
| POST | /jumanpp | sentence | Content-Type:application/json |
| POST | /sudachi | sentence, mode [optional. 'A', 'B', or 'C'] | Content-Type:application/json |
