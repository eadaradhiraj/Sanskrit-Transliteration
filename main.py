import argparse
from sanskrit_transliteration import transliterate

parser = argparse.ArgumentParser(
    description='Transliterate Sanskrit Text. Currently supported schemes are VELTHIUS, WX, SLP1, HK, SKT'
)
parser.add_argument('-i', '--inputtext', type=str, nargs=1, required=True)
parser.add_argument('-f', '--fromscheme', type=str, nargs=1, required=True)
parser.add_argument('-t', '--toscheme', type=str, nargs=1, required=True)

args = parser.parse_args()
print(
    transliterate(
        text=args.text,
        from_scheme=args.fromscheme,
        to_scheme=args.toscheme,
    )
)
