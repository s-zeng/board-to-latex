import integrator

#global vars

head = "\\documentclass{article}\n\
\\usepackage[margin=1in]{geometry}\n\
\\usepackage{amsmath}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{amsthm}\n\
\\theoremstyle{plain}\n\
\\newtheorem*{thm}{Theorem}\n\
\\newtheorem*{lemma}{Lemma}\n\
\\theoremstyle{remark}\n\
\\newtheorem*{remk}{Remark}\n\
\\theoremstyle{definition}\n\
\\newtheorem*{defn}{Definition}\n\
\\begin{document}\n\n"

tail = "\n\n\\end{document}"

spelling_map = { "bra": "be a", "ove": "over", "Weerstrass": "Weierstrass",
                 "empt": "empty", "Conurgence": "Convergence",
                 "decressing": "decreasing", "quence": "sequence", "Theonen": "Theorem" }

thm_map = { "Theorem": "thm", "Lemma": "lemma", "Remark": "remk",
            "Definition": "defn", "Proposition": "prop" }

thm_keywords = ["Theorem", "Lemma", "Remark", "Definition", "Proposition"]

prf_keywords = ["Proof", "proof", "proot", "Proofi"]

qed_keywords = ['o']

thm_end_keywords = [".", ":", ")"]

colon_keywords = [".", ":", ","]

hyphen_keywords = ["-"]

rna = [
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 277,
            "y": 1220
          },
          {
            "x": 1855,
            "y": 1220
          },
          {
            "x": 1855,
            "y": 1961
          },
          {
            "x": 277,
            "y": 1961
          }
        ]
      },
      "description": "Rank-Nullity Theorem:\nLet v bra finite dimensional vector\nspace ove avocadoscado. Let avocadoscado be a\nlinear transformation. Then:\navocadoscado\nProofi Exercise for the reader.\n",
      "locale": "en"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 281,
            "y": 1220
          },
          {
            "x": 538,
            "y": 1232
          },
          {
            "x": 534,
            "y": 1323
          },
          {
            "x": 277,
            "y": 1311
          }
        ]
      },
      "description": "Rank"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 598,
            "y": 1235
          },
          {
            "x": 624,
            "y": 1236
          },
          {
            "x": 620,
            "y": 1327
          },
          {
            "x": 594,
            "y": 1326
          }
        ]
      },
      "description": "-"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 641,
            "y": 1237
          },
          {
            "x": 916,
            "y": 1250
          },
          {
            "x": 912,
            "y": 1341
          },
          {
            "x": 637,
            "y": 1328
          }
        ]
      },
      "description": "Nullity"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1036,
            "y": 1255
          },
          {
            "x": 1358,
            "y": 1270
          },
          {
            "x": 1353,
            "y": 1361
          },
          {
            "x": 1032,
            "y": 1346
          }
        ]
      },
      "description": "Theorem"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1398,
            "y": 1272
          },
          {
            "x": 1424,
            "y": 1273
          },
          {
            "x": 1420,
            "y": 1364
          },
          {
            "x": 1394,
            "y": 1363
          }
        ]
      },
      "description": ":"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 363,
            "y": 1370
          },
          {
            "x": 494,
            "y": 1371
          },
          {
            "x": 493,
            "y": 1464
          },
          {
            "x": 362,
            "y": 1463
          }
        ]
      },
      "description": "Let"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 542,
            "y": 1373
          },
          {
            "x": 568,
            "y": 1373
          },
          {
            "x": 567,
            "y": 1465
          },
          {
            "x": 541,
            "y": 1465
          }
        ]
      },
      "description": "v"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 631,
            "y": 1373
          },
          {
            "x": 840,
            "y": 1375
          },
          {
            "x": 839,
            "y": 1468
          },
          {
            "x": 630,
            "y": 1466
          }
        ]
      },
      "description": "bra"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 928,
            "y": 1375
          },
          {
            "x": 1069,
            "y": 1376
          },
          {
            "x": 1068,
            "y": 1469
          },
          {
            "x": 927,
            "y": 1468
          }
        ]
      },
      "description": "finite"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1134,
            "y": 1378
          },
          {
            "x": 1600,
            "y": 1382
          },
          {
            "x": 1599,
            "y": 1475
          },
          {
            "x": 1133,
            "y": 1471
          }
        ]
      },
      "description": "dimensional"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1647,
            "y": 1383
          },
          {
            "x": 1855,
            "y": 1385
          },
          {
            "x": 1854,
            "y": 1478
          },
          {
            "x": 1646,
            "y": 1476
          }
        ]
      },
      "description": "vector"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 342,
            "y": 1477
          },
          {
            "x": 535,
            "y": 1476
          },
          {
            "x": 535,
            "y": 1558
          },
          {
            "x": 342,
            "y": 1559
          }
        ]
      },
      "description": "space"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 616,
            "y": 1475
          },
          {
            "x": 707,
            "y": 1475
          },
          {
            "x": 707,
            "y": 1557
          },
          {
            "x": 616,
            "y": 1557
          }
        ]
      },
      "description": "ove"
    },
    
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 834,
            "y": 1473
          },
          {
            "x": 857,
            "y": 1473
          },
          {
            "x": 857,
            "y": 1554
          },
          {
            "x": 834,
            "y": 1554
          }
        ]
      },
      "description": "avocadoscado"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 883,
            "y": 1473
          },
          {
            "x": 906,
            "y": 1473
          },
          {
            "x": 906,
            "y": 1554
          },
          {
            "x": 883,
            "y": 1554
          }
        ]
      },
      "description": "."
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 987,
            "y": 1473
          },
          {
            "x": 1056,
            "y": 1473
          },
          {
            "x": 1056,
            "y": 1554
          },
          {
            "x": 987,
            "y": 1554
          }
        ]
      },
      "description": "Let"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1180,
            "y": 1472
          },
          {
            "x": 1269,
            "y": 1472
          },
          {
            "x": 1269,
            "y": 1554
          },
          {
            "x": 1180,
            "y": 1554
          }
        ]
      },
      "description": "avocadoscado"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1537,
            "y": 1471
          },
          {
            "x": 1640,
            "y": 1470
          },
          {
            "x": 1640,
            "y": 1551
          },
          {
            "x": 1537,
            "y": 1552
          }
        ]
      },
      "description": "be"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1695,
            "y": 1469
          },
          {
            "x": 1718,
            "y": 1469
          },
          {
            "x": 1718,
            "y": 1550
          },
          {
            "x": 1695,
            "y": 1550
          }
        ]
      },
      "description": "a"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 375,
            "y": 1579
          },
          {
            "x": 549,
            "y": 1574
          },
          {
            "x": 551,
            "y": 1655
          },
          {
            "x": 377,
            "y": 1660
          }
        ]
      },
      "description": "linear"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 674,
            "y": 1570
          },
          {
            "x": 1146,
            "y": 1556
          },
          {
            "x": 1148,
            "y": 1636
          },
          {
            "x": 676,
            "y": 1651
          }
        ]
      },
      "description": "transformation"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1165,
            "y": 1556
          },
          {
            "x": 1188,
            "y": 1555
          },
          {
            "x": 1190,
            "y": 1635
          },
          {
            "x": 1167,
            "y": 1636
          }
        ]
      },
      "description": "."
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1271,
            "y": 1551
          },
          {
            "x": 1366,
            "y": 1548
          },
          {
            "x": 1368,
            "y": 1629
          },
          {
            "x": 1273,
            "y": 1632
          }
        ]
      },
      "description": "Then"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1385,
            "y": 1549
          },
          {
            "x": 1408,
            "y": 1548
          },
          {
            "x": 1410,
            "y": 1628
          },
          {
            "x": 1387,
            "y": 1629
          }
        ]
      },
      "description": ":"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 486,
            "y": 1693
          },
          {
            "x": 670,
            "y": 1687
          },
          {
            "x": 673,
            "y": 1773
          },
          {
            "x": 489,
            "y": 1779
          }
        ]
      },
      "description": "avocadoscado"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 427,
            "y": 1857
          },
          {
            "x": 690,
            "y": 1854
          },
          {
            "x": 691,
            "y": 1958
          },
          {
            "x": 428,
            "y": 1961
          }
        ]
      },
      "description": "Proofi"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 777,
            "y": 1853
          },
          {
            "x": 1094,
            "y": 1849
          },
          {
            "x": 1095,
            "y": 1954
          },
          {
            "x": 778,
            "y": 1958
          }
        ]
      },
      "description": "Exercise"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1176,
            "y": 1848
          },
          {
            "x": 1236,
            "y": 1847
          },
          {
            "x": 1237,
            "y": 1951
          },
          {
            "x": 1177,
            "y": 1952
          }
        ]
      },
      "description": "for"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1318,
            "y": 1847
          },
          {
            "x": 1421,
            "y": 1846
          },
          {
            "x": 1422,
            "y": 1951
          },
          {
            "x": 1319,
            "y": 1952
          }
        ]
      },
      "description": "the"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1475,
            "y": 1845
          },
          {
            "x": 1708,
            "y": 1842
          },
          {
            "x": 1709,
            "y": 1946
          },
          {
            "x": 1476,
            "y": 1949
          }
        ]
      },
      "description": "reader"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1732,
            "y": 1843
          },
          {
            "x": 1762,
            "y": 1843
          },
          {
            "x": 1763,
            "y": 1946
          },
          {
            "x": 1733,
            "y": 1946
          }
        ]
      },
      "description": "."
    }
  ]

formula_list_rna = [
    {
        "detection_list":[],
        "latex_confidence_rate": 0.85,
        "latex_styled": "\mathbb{F}"
        },
    {
        "detection_list":[],
        "latex_confidence_rate": 0.97,
        "latex_styled": "T : V \\to W"
        },
    {
     "detection_list": [
         "is_printed"
     ],
     "detection_map": {
         "contains_chart": 0,
         "contains_diagram": 0.0002,
         "contains_graph": 0.0001,
         "contains_table": 0,
         "is_blank": 0.0008,
         "is_inverted": 0,
         "is_not_math": 0.0009,
         "is_printed": 1
     },
     "latex_confidence": 0.1434476702596397,
     "latex_confidence_rate": 0.9911714196205139,
     "latex_styled": "\\begin{aligned} \\sigma = \\left\\{ \\left[ \\begin{array} { l l } { 1 } & { 0 } \\\\ { 0 } & { 0\
} \\end{array} \\right] , \\left[ \\begin{array} { l l } { 0 } & { 1 } \\\\ { 0 } & { 0 } \\end{array} \\right] , \\left\
 [ \\begin{array} { l l } { 0 } & { 0 } \\\\ { 1 } & { 0 } \\end{array} \\right] , \\left[ \\begin{array} { l l } { 0 } &\
  { 0 } \\\\ { 0 } & { 1 } \\end{array} \\right] \\right\\} \\\\ [ T ] _ { \\sigma } = \\left[ \\begin{array} { l l l l }\
  { 1 } & { 0 } & { 1 } & { 0 } \\\\ { 0 } & { 1 } & { 0 } & { 1 } \\\\ { 0 } & { 0 } & { 1 } & { 0 } \\\\ { 0 } & { 0 }\
 & { 0 } & { 1 } \\end{array} \\right] \\end{aligned}",
     "position": {
         "height": 139,
         "top_left_x": 28,
         "top_left_y": 5,
         "width": 304
     }
 }]

def distance(word1, word2):
    if len(word1) < len(word2):
        temp = word1
        word1 = word2
        word2 = temp
    d = len(word1) - len(word2)
    for i in range(len(word2)):
        if word1[i] != word2[i]:
            d += 1
    return d

def almost_thm(word):
    for keyword in thm_keywords:
        if distance(word, keyword) < 3:
            return keyword
        else:
            return word

def formulate(formula_list):
    for i in range(len(formula_list)):
        if formula_list[i]["latex_confidence_rate"] < 0.95:
            suffix = "\\ (?)"
        else:
            suffix = ""
        formula_list[i] = formula_list[i]["latex_styled"] + suffix
    

def preprocess(data):
    long_string = data[0]['description']
    if len(data) < 2:
        return data
    i = 1
    while distance(data[i]['description'], "Theorem") > 2:
        i += 1
    if(i != len(data)):
        data.pop(i)
        data.insert(i, {'description': ")"})
        data.insert(1, {'description': "Theorem"})
        data.insert(2, {'description': "("})

    j = 0
    while "avocadoscado" in long_string:
        display = False
        if "\navocadoscado\n" in long_string:
            if long_string.find("avocadoscado") == long_string.find("\navocadoscado\n") + 1:
                display = True
            while data[j]['description'] != "avocadoscado":
                j += 1
            if display:
                data[j]['description'] = "thicc avocado"
            else:
                data[j]['description'] = "smol avocado"
                        
        long_string = long_string.replace("avocadoscado", "", 1)
    
    return data

def parse(data, latex, tail, formula_list):
    #print(latex)
    if data == []:
        #print(latex + tail)
        return latex + tail
    else:
        word = fix_spell(data[0]['description'])
    
    if almost_thm(data[0]['description']) in thm_keywords:
        name = thm_map[word]
        latex += '\\begin{' + name + '}'
        tail = '\n\\end{' + name + '}' + tail
        if data[1]['description'] == '(':
            latex += '['
            return parse_thm(data[2:], latex, tail, formula_list)
        else:
            return parse(data[1:], latex, tail, formula_list)
    elif distance(word, "Proof") < 2:
        latex += '\n\\begin{proof}\n'
        tail = '\n\\end{proof}' + tail
        return parse_prf(data[1:], latex, tail, formula_list)
    elif word in hyphen_keywords:
        latex = latex[:-1] + word
        return parse(data[1:], latex, tail, formula_list)
    elif word in colon_keywords:
        latex = latex[:-1] + word + " "
        return parse(data[1:], latex, tail, formula_list)
    elif word == "smol avocado":
        latex = latex + "$" + formula_list.pop(0) + "$ "
        return parse(data[1:], latex, tail, formula_list)
    elif word == "thicc avocado":
        latex = latex + "\n$$" + formula_list.pop(0) + "$$\n"
        return parse(data[1:], latex, tail, formula_list)
    else:
        latex += word + ' '
        return parse(data[1:], latex, tail, formula_list)


def parse_thm(data, latex, tail, formula_list):
    #print(latex)
    if data == []:
        return parse(data, latex, tail, formula_list)
    else:
        word = fix_spell(data[0]['description'])
    
    if word in thm_end_keywords:
        if latex[-1] == " ":
            latex = latex[:-1]
        if data[1]['description'] in thm_end_keywords:
            return parse_thm(data[1:], latex, tail, formula_list)
        latex = latex + "]\n"
        return parse(data[1:], latex, tail, formula_list)
    elif word in hyphen_keywords:
        latex = latex[:-1] + word
        return parse_thm(data[1:], latex, tail, formula_list)
    elif word in colon_keywords:
        latex = latex[:-1] + word + " "
        return parse_thm(data[1:], latex, tail, formula_list)
    elif word == "smol avocado":
        latex = latex + "$" + formula_list.pop(0) + "$"
        return parse_thm(data[1:], latex, tail, formula_list)
    elif word == "thicc avocado":
        latex = latex + "\n$$" + formula_list.pop(0) + "$$\n"
        return parse_thm(data[1:], latex, tail, formula_list)
    else:
        latex += word + ' '
        return parse_thm(data[1:], latex, tail, formula_list)

def parse_prf(data, latex, tail, formula_list):
    #print(latex)
    if data == []:
        return parse(data, latex, tail, formula_list)
    else:
        word = fix_spell(data[0]['description'])
    
                        
    if word in qed_keywords:
        return parse(data[1:], latex, tail, formula_list)
    if word == ')':
        return parse_prf(data[1:], latex, tail, formula_list)
    elif word in colon_keywords:
        latex = latex[:-1] + word + " "
        return parse_prf(data[1:], latex, tail, formula_list)
    elif word == "smol avocado":
        latex = latex + "$" + formula_list.pop(0) + "$"
        return parse_prf(data[1:], latex, tail, formula_list)
    elif word == "thicc avocado":
        latex = latex + "\n$$" + formula_list.pop(0) + "$$\n"
        return parse_prf(data[1:], latex, tail, formula_list)
    else:
        latex += word + ' '
        return parse_prf(data[1:], latex, tail, formula_list)

def fix_spell(word):
    if word in spelling_map.keys():
        word = spelling_map[word]
    return word

def process(data, formula_list):
    formulate(formula_list)
    data = preprocess(data)
    result = parse(data[1:], "", "", formula_list)
    #print(head + result + tail)
    return head + result + tail

#print(process(rna, formula_list_rna))

def get_latex_code(image_file_name, boundaries):
    data, formula_list = integrator.convert_to_latex(image_file_name, boundaries)
    return process(data, formula_list)

def get_latex_code_object(image_object, boundaries):
    data, formula_list = integrator.convert_object_to_latex(image_object, boundaries)
    return process(data, formula_list)

rnt = "/home/kronicmage/repos/api-examples/python/test.jpg"
theorem_statement = (200, 460, 1350, 600)
type_string = (850, 275, 1275, 360)
summation = (500, 775, 950, 1000)
all_of_them = [type_string, theorem_statement, summation]
