#import levenshtein

thm_map = { "Theorem": "thm", "Lemma": "lemma", "Remark": "remk",
            "Definition": "defn", "Proposition": "prop" }

thm_keywords = ["Theorem", "Lemma"]

prf_keywords = ["Proof", "proof", "proot"]

qed_keywords = ['o']

thm_end_keywords = [".", ":"]

hyphen_keywords = ["-"]

latex = ""

data = [
    {"locale": "en", "description": "RATTLESNAKES\nMAY BE FOUND IN THIS AREA\nGIVE THEM DISTANCE\nAND RESPECT\n",
     "bounding_poly": {"vertices": [{"x": 135, "y": 172}, {"x": 334, "y": 172}, {"x": 334, "y": 263}, {"x": 135, "y": 263}]}},
    {"description": "RATTLESNAKES", "bounding_poly": {"vertices": [{"x": 154, "y": 178}, {"x": 313, "y": 172}, {"x": 314, "y": 190}, {"x": 155, "y": 196}]}},
    {"description": "MAY", "bounding_poly": {"vertices": [{"x": 135, "y": 201}, {"x": 162, "y": 200}, {"x": 163, "y": 218}, {"x": 136, "y": 219}]}},
    {"description": "BE", "bounding_poly": {"vertices": [{"x": 167, "y": 200}, {"x": 183, "y": 199}, {"x": 184, "y": 217}, {"x": 168, "y": 218}]}},
    {"description": "FOUND", "bounding_poly": {"vertices": [{"x": 192, "y": 200}, {"x": 235, "y": 199}, {"x": 236, "y": 216}, {"x": 193, "y": 217}]}},
    {"description": "IN", "bounding_poly": {"vertices": [{"x": 243, "y": 198}, {"x": 250, "y": 198}, {"x": 251, "y": 215}, {"x": 244, "y": 215}]}},
    {"description": "THIS", "bounding_poly": {"vertices": [{"x": 262, "y": 197}, {"x": 288, "y": 196}, {"x": 289, "y": 214}, {"x": 263, "y": 215}]}},
    {"description": "AREA", "bounding_poly": {"vertices": [{"x": 297, "y": 196}, {"x": 333, "y": 195}, {"x": 334, "y": 212}, {"x": 298, "y": 213}]}},
    {"description": "GIVE", "bounding_poly": {"vertices": [{"x": 154, "y": 226}, {"x": 184, "y": 225}, {"x": 184, "y": 243}, {"x": 154, "y": 244}]}},
    {"description": "THEM", "bounding_poly": {"vertices": [{"x": 195, "y": 226}, {"x": 228, "y": 225}, {"x": 228, "y": 242}, {"x": 195, "y": 243}]}},
    {"description": "DISTANCE", "bounding_poly": {"vertices": [{"x": 242, "y": 225}, {"x": 310, "y": 224}, {"x": 310, "y": 242}, {"x": 242, "y": 243}]}},
    {"description": "AND", "bounding_poly": {"vertices": [{"x": 179, "y": 246}, {"x": 207, "y": 245}, {"x": 207, "y": 262}, {"x": 179, "y": 263}]}},
    {"description": "RESPECT", "bounding_poly": {"vertices": [{"x": 216, "y": 246}, {"x": 282, "y": 245}, {"x": 282, "y": 262}, {"x": 216, "y": 263}]}}
    ]


wop = [
    {'locale': 'en', 'description': 'Theorem (\nWORD. Every non-empt subset\nof the integers has a smallest element.\nproot\nAxiom of choice o\n',
     'bounding_poly': {'vertices': [{'x': 519, 'y': 685}, {'x': 2784, 'y': 685}, {'x': 2784, 'y': 1284}, {'x': 519, 'y': 1284}]}},
    {'description': 'Theorem', 'bounding_poly': {'vertices': [{'x': 532, 'y': 721}, {'x': 935, 'y': 715}, {'x': 937, 'y': 844}, {'x': 534, 'y': 850}]}},
    {'description': '(', 'bounding_poly': {'vertices': [{'x': 1028, 'y': 713}, {'x': 1066, 'y': 712}, {'x': 1068, 'y': 841}, {'x': 1030, 'y': 842}]}},
    {'description': 'WORD', 'bounding_poly': {'vertices': [{'x': 1027, 'y': 713}, {'x': 1393, 'y': 707}, {'x': 1395, 'y': 836}, {'x': 1029, 'y': 842}]}},
    {'description': '.', 'bounding_poly': {'vertices': [{'x': 1408, 'y': 707}, {'x': 1446, 'y': 706}, {'x': 1448, 'y': 835}, {'x': 1410, 'y': 836}]}},
    {'description': 'Every', 'bounding_poly': {'vertices': [{'x': 1541, 'y': 705}, {'x': 1768, 'y': 701}, {'x': 1770, 'y': 830}, {'x': 1543, 'y': 834}]}},
    {'description': 'non', 'bounding_poly': {'vertices': [{'x': 1826, 'y': 700}, {'x': 1993, 'y': 697}, {'x': 1995, 'y': 826}, {'x': 1828, 'y': 829}]}},
    {'description': '-', 'bounding_poly': {'vertices': [{'x': 2010, 'y': 698}, {'x': 2048, 'y': 697}, {'x': 2050, 'y': 826}, {'x': 2012, 'y': 827}]}},
    {'description': 'empt', 'bounding_poly': {'vertices': [{'x': 2068, 'y': 697}, {'x': 2318, 'y': 693}, {'x': 2320, 'y': 822}, {'x': 2070, 'y': 826}]}},
    {'description': 'subset', 'bounding_poly': {'vertices': [{'x': 2466, 'y': 690}, {'x': 2782, 'y': 685}, {'x': 2784, 'y': 814}, {'x': 2468, 'y': 819}]}},
    {'description': 'of', 'bounding_poly': {'vertices': [{'x': 519, 'y': 879}, {'x': 603, 'y': 878}, {'x': 604, 'y': 970}, {'x': 520, 'y': 971}]}},
    {'description': 'the', 'bounding_poly': {'vertices': [{'x': 705, 'y': 877}, {'x': 836, 'y': 876}, {'x': 837, 'y': 968}, {'x': 706, 'y': 969}]}},
    {'description': 'integers', 'bounding_poly': {'vertices': [{'x': 948, 'y': 874}, {'x': 1266, 'y': 871}, {'x': 1267, 'y': 963}, {'x': 949, 'y': 966}]}},
    {'description': 'has', 'bounding_poly': {'vertices': [{'x': 1372, 'y': 871}, {'x': 1556, 'y': 869}, {'x': 1557, 'y': 961}, {'x': 1373, 'y': 963}]}},
    {'description': 'a', 'bounding_poly': {'vertices': [{'x': 1631, 'y': 868}, {'x': 1657, 'y': 868}, {'x': 1658, 'y': 959}, {'x': 1632, 'y': 959}]}},
    {'description': 'smallest', 'bounding_poly': {'vertices': [{'x': 1778, 'y': 866}, {'x': 2109, 'y': 863}, {'x': 2110, 'y': 955}, {'x': 1779, 'y': 958}]}},
    {'description': 'element', 'bounding_poly': {'vertices': [{'x': 2207, 'y': 861}, {'x': 2573, 'y': 857}, {'x': 2574, 'y': 949}, {'x': 2208, 'y': 953}]}},
    {'description': '.', 'bounding_poly': {'vertices': [{'x': 2598, 'y': 858}, {'x': 2624, 'y': 858}, {'x': 2625, 'y': 949}, {'x': 2599, 'y': 949}]}},
    {'description': 'proot', 'bounding_poly': {'vertices': [{'x': 576, 'y': 1134}, {'x': 797, 'y': 1135}, {'x': 797, 'y': 1280}, {'x': 576, 'y': 1279}]}},
    {'description': 'Axiom', 'bounding_poly': {'vertices': [{'x': 1096, 'y': 1136}, {'x': 1358, 'y': 1137}, {'x': 1358, 'y': 1281}, {'x': 1096, 'y': 1280}]}},
    {'description': 'of', 'bounding_poly': {'vertices': [{'x': 1464, 'y': 1137}, {'x': 1597, 'y': 1137}, {'x': 1597, 'y': 1282}, {'x': 1464, 'y': 1282}]}},
    {'description': 'choice', 'bounding_poly': {'vertices': [{'x': 1719, 'y': 1138}, {'x': 1980, 'y': 1139}, {'x': 1980, 'y': 1284}, {'x': 1719, 'y': 1283}]}},
    {'description': 'o', 'bounding_poly': {'vertices': [{'x': 2087, 'y': 1139}, {'x': 2129, 'y': 1139}, {'x': 2129, 'y': 1283}, {'x': 2087, 'y': 1283}]}}
    ]

bw = [
    {},
    {'description': 'Bolzano'},
    {'description': '-'},
    {'description': 'Weierstrass'},
    {'description': 'Theorem'},
    {'description': ':'},
    {'description': 'Every'},
    {'description': 'bounded'},
    {'description': 'sequence'},
    {'description': 'of'},
    {'description': 'real'},
    {'description': 'numbers'},
    {'description': 'has'},
    {'description': 'a'},
    {'description': 'convergent'},
    {'description': 'subsequence'},
    {'description': 'Proof'},
    {'description': ':'},
    {'description': 'MCT'},
    {'description': '.'}
    ]

def parse(data, latex, tail):
    print(latex)
    if data == []:
        print(latex + tail)
        return latex + tail
    elif data[0]['description'] in thm_keywords:
        name = thm_map[data[0]['description']]
        latex += '\\begin{' + name + '}'
        tail = '\n\\end{' + name + '}' + tail
        if data[1]['description'] == '(':
            latex += '['
            return parse_thm(data[2:], latex, tail)
    elif data[0]['description'] in prf_keywords:
        latex += '\n\\begin{proof}\n'
        tail = '\n\\end{proof}' + tail
        return parse_prf(data[1:], latex, tail)
    elif data[0]['description'] in hyphen_keywords:
        latex = latex[:-1] + data[0]['description']
        return parse(data[1:], latex, tail)
    elif data[0]['description'] == '.':
        latex = latex[:-1] + data[0]['description']
        return parse(data[1:], latex, tail)
    else:
        latex += data[0]['description'] + ' '
        return parse(data[1:], latex, tail)


def parse_thm(data, latex, tail):
    print(latex)
    if data[0]['description'] in thm_end_keywords:
        latex = latex[:-1] + ']\n'
        return parse(data[1:], latex, tail)
    else:
        latex += data[0]['description'] + ' '
        return parse_thm(data[1:], latex, tail)

def parse_prf(data, latex, tail):
    if data[0]['description'] in qed_keywords:
        return parse(data[1:], latex, tail)
    if data[0]['description'] == ')':
        return parse_prf(data[1:], latex, tail)
    else:
        latex += data[0]['description'] + ' '
        return parse_prf(data[1:], latex, tail)

result = parse(wop[1:], "", "")
#result = parse(bw[1:], "", "")

head = "\\documentclass{article}\n\
\\usepackage[margin=1in]{geometry}\n\
\\usepackage{amsmath}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{amsthm}\n\
\\theoremstyle{plain}\n\
\\newtheorem{thm}{Theorem}\n\
\\newtheorem{lemma}{Lemma}\n\
\\theoremstyle{remark}\n\
\\newtheorem{remk}{Remark}\n\
\\theoremstyle{definition}\n\
\\newtheorem{defn}{Definition}\n\
\\begin{document}\n\n"

tail = "\n\n\\end{document}"


print(head + result + tail)
