# MorphAnalysisAPI

Japanese Morphological Analysis Web API.

We can try following 3 japanese morphlogical analysis using this API.

- [MeCab](https://taku910.github.io/mecab/)
  - mecab with [NEologd](https://github.com/neologd/mecab-ipadic-neologd)
- [JUMAN++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)
- [Sudachi](https://github.com/WorksApplications/SudachiPy) (SudachiPy)

## Requirements

- python3
  - requests
- Docker

## Usage

### Execute Docker Container

```shell
docker build . -t morph-analysis-api # wait a minute
docker run -it --rm -d -p 5000:5000 -v $PWD/:/app morph-analysis-api:latest python app.py
```

### Down Docker Container

```shell
docker stop `container_id`
```

### Test Morphological Analysis

```shell
python3 request.py
```

#### Usage Test Script

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

### About API

| HTTP method | end point | request parameters | request headers |
---- | ---- | ---- | ----
| POST | /mecab | sentence | Content-Type:application/json |
| POST | /mecab-neologd | sentence | Content-Type:application/json |
| POST | /jumanpp | sentence | Content-Type:application/json |
| POST | /sudachi | sentence, mode [optional. 'A', 'B', or 'C'] | Content-Type:application/json |
