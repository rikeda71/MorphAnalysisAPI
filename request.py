import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sentence', default='すもももももももものうち',
                    help='a japanese sentence. default=`すもももももももものうち`')
parser.add_argument('-m', '--machine', default='mecab',
                    choices=['mecab', 'mecab-neologd', 'sudachi', 'jumanpp'],
                    help='choice morphological analysis machine.\
                    default=`mecab`')
args = parser.parse_args()
headers = {'Content-Type': 'application/json'}
json = {'sentence': args.sentence}

r = requests.post('http://localhost:5000/' + args.machine,
                  json=json, headers=headers)
print(r.text)
