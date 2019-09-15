#import levenshtein

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
                 "decressing": "decreasing", "quence": "sequence" }

thm_map = { "Theorem": "thm", "Lemma": "lemma", "Remark": "remk",
            "Definition": "defn", "Proposition": "prop" }

thm_keywords = ["Theorem", "Lemma"]

prf_keywords = ["Proof", "proof", "proot", "Proofi"]

qed_keywords = ['o']

thm_end_keywords = [".", ":", ")"]

colon_keywords = [".", ":", ","]

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
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 66,
            "y": 289
          },
          {
            "x": 426,
            "y": 289
          },
          {
            "x": 426,
            "y": 427
          },
          {
            "x": 66,
            "y": 427
          }
        ]
      },
      "description": "Bolzano- Weerstrass Theorem:\nEvery bounded sequence of real\nnumbers has a convergent subsequence\nProof\nMCT.\n",
      "locale": "en"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 66,
            "y": 289
          },
          {
            "x": 153,
            "y": 289
          },
          {
            "x": 153,
            "y": 311
          },
          {
            "x": 66,
            "y": 311
          }
        ]
      },
      "description": "Bolzano"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 155,
            "y": 289
          },
          {
            "x": 160,
            "y": 289
          },
          {
            "x": 160,
            "y": 311
          },
          {
            "x": 155,
            "y": 311
          }
        ]
      },
      "description": "-"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 161,
            "y": 289
          },
          {
            "x": 286,
            "y": 289
          },
          {
            "x": 286,
            "y": 311
          },
          {
            "x": 161,
            "y": 311
          }
        ]
      },
      "description": "Weerstrass"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 315,
            "y": 289
          },
          {
            "x": 393,
            "y": 289
          },
          {
            "x": 393,
            "y": 311
          },
          {
            "x": 315,
            "y": 311
          }
        ]
      },
      "description": "Theorem"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 401,
            "y": 289
          },
          {
            "x": 406,
            "y": 289
          },
          {
            "x": 406,
            "y": 311
          },
          {
            "x": 401,
            "y": 311
          }
        ]
      },
      "description": ":"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 84,
            "y": 325
          },
          {
            "x": 129,
            "y": 325
          },
          {
            "x": 129,
            "y": 348
          },
          {
            "x": 84,
            "y": 348
          }
        ]
      },
      "description": "Every"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 134,
            "y": 325
          },
          {
            "x": 192,
            "y": 325
          },
          {
            "x": 192,
            "y": 348
          },
          {
            "x": 134,
            "y": 348
          }
        ]
      },
      "description": "bounded"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 206,
            "y": 325
          },
          {
            "x": 272,
            "y": 325
          },
          {
            "x": 272,
            "y": 348
          },
          {
            "x": 206,
            "y": 348
          }
        ]
      },
      "description": "sequence"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 289,
            "y": 325
          },
          {
            "x": 297,
            "y": 325
          },
          {
            "x": 297,
            "y": 348
          },
          {
            "x": 289,
            "y": 348
          }
        ]
      },
      "description": "of"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 314,
            "y": 325
          },
          {
            "x": 366,
            "y": 325
          },
          {
            "x": 366,
            "y": 348
          },
          {
            "x": 314,
            "y": 348
          }
        ]
      },
      "description": "real"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 82,
            "y": 352
          },
          {
            "x": 150,
            "y": 352
          },
          {
            "x": 150,
            "y": 371
          },
          {
            "x": 82,
            "y": 371
          }
        ]
      },
      "description": "numbers"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 169,
            "y": 352
          },
          {
            "x": 202,
            "y": 352
          },
          {
            "x": 202,
            "y": 371
          },
          {
            "x": 169,
            "y": 371
          }
        ]
      },
      "description": "has"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 215,
            "y": 352
          },
          {
            "x": 220,
            "y": 352
          },
          {
            "x": 220,
            "y": 371
          },
          {
            "x": 215,
            "y": 371
          }
        ]
      },
      "description": "a"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 232,
            "y": 352
          },
          {
            "x": 313,
            "y": 352
          },
          {
            "x": 313,
            "y": 371
          },
          {
            "x": 232,
            "y": 371
          }
        ]
      },
      "description": "convergent"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 335,
            "y": 352
          },
          {
            "x": 426,
            "y": 352
          },
          {
            "x": 426,
            "y": 371
          },
          {
            "x": 335,
            "y": 371
          }
        ]
      },
      "description": "subsequence"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 89,
            "y": 405
          },
          {
            "x": 130,
            "y": 405
          },
          {
            "x": 130,
            "y": 427
          },
          {
            "x": 89,
            "y": 427
          }
        ]
      },
      "description": "Proof"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 168,
            "y": 405
          },
          {
            "x": 202,
            "y": 405
          },
          {
            "x": 202,
            "y": 427
          },
          {
            "x": 168,
            "y": 427
          }
        ]
      },
      "description": "MCT"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 211,
            "y": 405
          },
          {
            "x": 216,
            "y": 405
          },
          {
            "x": 216,
            "y": 427
          },
          {
            "x": 211,
            "y": 427
          }
        ]
      },
      "description": "."
    }
  ]

rn = [
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
      "description": "Rank-Nullity Theorem:\nLet v bra finite dimensional vector\nspace ove-t. Let TV w be a\nlinear transformation. Then:\nrank (T) + nullity (T) =dim\nProofi Exercise for the reader.\n",
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
            "x": 736,
            "y": 1475
          },
          {
            "x": 759,
            "y": 1475
          },
          {
            "x": 759,
            "y": 1556
          },
          {
            "x": 736,
            "y": 1556
          }
        ]
      },
      "description": "-"
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
      "description": "t"
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
      "description": "TV"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1426,
            "y": 1470
          },
          {
            "x": 1449,
            "y": 1470
          },
          {
            "x": 1449,
            "y": 1551
          },
          {
            "x": 1426,
            "y": 1551
          }
        ]
      },
      "description": "w"
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
      "description": "rank"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 730,
            "y": 1687
          },
          {
            "x": 754,
            "y": 1686
          },
          {
            "x": 757,
            "y": 1770
          },
          {
            "x": 733,
            "y": 1771
          }
        ]
      },
      "description": "("
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 783,
            "y": 1685
          },
          {
            "x": 807,
            "y": 1684
          },
          {
            "x": 810,
            "y": 1768
          },
          {
            "x": 786,
            "y": 1769
          }
        ]
      },
      "description": "T"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 835,
            "y": 1682
          },
          {
            "x": 859,
            "y": 1681
          },
          {
            "x": 862,
            "y": 1765
          },
          {
            "x": 838,
            "y": 1766
          }
        ]
      },
      "description": ")"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 878,
            "y": 1681
          },
          {
            "x": 902,
            "y": 1680
          },
          {
            "x": 905,
            "y": 1764
          },
          {
            "x": 881,
            "y": 1765
          }
        ]
      },
      "description": "+"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 936,
            "y": 1678
          },
          {
            "x": 1139,
            "y": 1671
          },
          {
            "x": 1142,
            "y": 1757
          },
          {
            "x": 939,
            "y": 1764
          }
        ]
      },
      "description": "nullity"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1161,
            "y": 1671
          },
          {
            "x": 1185,
            "y": 1670
          },
          {
            "x": 1188,
            "y": 1754
          },
          {
            "x": 1164,
            "y": 1755
          }
        ]
      },
      "description": "("
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1196,
            "y": 1670
          },
          {
            "x": 1220,
            "y": 1669
          },
          {
            "x": 1223,
            "y": 1753
          },
          {
            "x": 1199,
            "y": 1754
          }
        ]
      },
      "description": "T"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1238,
            "y": 1669
          },
          {
            "x": 1262,
            "y": 1668
          },
          {
            "x": 1265,
            "y": 1752
          },
          {
            "x": 1241,
            "y": 1753
          }
        ]
      },
      "description": ")"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1289,
            "y": 1667
          },
          {
            "x": 1313,
            "y": 1666
          },
          {
            "x": 1316,
            "y": 1750
          },
          {
            "x": 1292,
            "y": 1751
          }
        ]
      },
      "description": "="
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1356,
            "y": 1664
          },
          {
            "x": 1453,
            "y": 1661
          },
          {
            "x": 1456,
            "y": 1746
          },
          {
            "x": 1359,
            "y": 1749
          }
        ]
      },
      "description": "dim"
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

mct = [
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 367,
            "y": 355
          },
          {
            "x": 3385,
            "y": 355
          },
          {
            "x": 3385,
            "y": 1715
          },
          {
            "x": 367,
            "y": 1715
          }
        ]
      },
      "description": "Monotone Conurgence Theorem\nIf a real-valued non-decressing\nquence is bounded above, then\nit converges.\n",
      "locale": "en"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 395,
            "y": 446
          },
          {
            "x": 1273,
            "y": 419
          },
          {
            "x": 1281,
            "y": 700
          },
          {
            "x": 404,
            "y": 727
          }
        ]
      },
      "description": "Monotone"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1584,
            "y": 410
          },
          {
            "x": 2570,
            "y": 380
          },
          {
            "x": 2578,
            "y": 661
          },
          {
            "x": 1593,
            "y": 691
          }
        ]
      },
      "description": "Conurgence"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 2825,
            "y": 372
          },
          {
            "x": 3376,
            "y": 355
          },
          {
            "x": 3384,
            "y": 636
          },
          {
            "x": 2834,
            "y": 653
          }
        ]
      },
      "description": "Theorem"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 367,
            "y": 873
          },
          {
            "x": 528,
            "y": 866
          },
          {
            "x": 541,
            "y": 1156
          },
          {
            "x": 380,
            "y": 1163
          }
        ]
      },
      "description": "If"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 709,
            "y": 858
          },
          {
            "x": 795,
            "y": 854
          },
          {
            "x": 808,
            "y": 1143
          },
          {
            "x": 722,
            "y": 1147
          }
        ]
      },
      "description": "a"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 902,
            "y": 850
          },
          {
            "x": 1196,
            "y": 837
          },
          {
            "x": 1208,
            "y": 1126
          },
          {
            "x": 915,
            "y": 1139
          }
        ]
      },
      "description": "real"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1203,
            "y": 836
          },
          {
            "x": 1289,
            "y": 832
          },
          {
            "x": 1302,
            "y": 1121
          },
          {
            "x": 1216,
            "y": 1125
          }
        ]
      },
      "description": "-"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1297,
            "y": 832
          },
          {
            "x": 1778,
            "y": 811
          },
          {
            "x": 1790,
            "y": 1101
          },
          {
            "x": 1310,
            "y": 1122
          }
        ]
      },
      "description": "valued"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1994,
            "y": 802
          },
          {
            "x": 2242,
            "y": 791
          },
          {
            "x": 2254,
            "y": 1080
          },
          {
            "x": 2007,
            "y": 1091
          }
        ]
      },
      "description": "non"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 2279,
            "y": 789
          },
          {
            "x": 2365,
            "y": 785
          },
          {
            "x": 2378,
            "y": 1074
          },
          {
            "x": 2292,
            "y": 1078
          }
        ]
      },
      "description": "-"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 2401,
            "y": 783
          },
          {
            "x": 3201,
            "y": 748
          },
          {
            "x": 3214,
            "y": 1039
          },
          {
            "x": 2414,
            "y": 1074
          }
        ]
      },
      "description": "decressing"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 641,
            "y": 1221
          },
          {
            "x": 1093,
            "y": 1192
          },
          {
            "x": 1105,
            "y": 1377
          },
          {
            "x": 653,
            "y": 1407
          }
        ]
      },
      "description": "quence"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1301,
            "y": 1179
          },
          {
            "x": 1403,
            "y": 1172
          },
          {
            "x": 1415,
            "y": 1357
          },
          {
            "x": 1313,
            "y": 1364
          }
        ]
      },
      "description": "is"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1450,
            "y": 1169
          },
          {
            "x": 2061,
            "y": 1129
          },
          {
            "x": 2073,
            "y": 1314
          },
          {
            "x": 1462,
            "y": 1354
          }
        ]
      },
      "description": "bounded"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 2239,
            "y": 1117
          },
          {
            "x": 2610,
            "y": 1093
          },
          {
            "x": 2622,
            "y": 1277
          },
          {
            "x": 2251,
            "y": 1302
          }
        ]
      },
      "description": "above"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 2652,
            "y": 1091
          },
          {
            "x": 2706,
            "y": 1087
          },
          {
            "x": 2718,
            "y": 1271
          },
          {
            "x": 2664,
            "y": 1275
          }
        ]
      },
      "description": ","
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 2823,
            "y": 1079
          },
          {
            "x": 3081,
            "y": 1062
          },
          {
            "x": 3093,
            "y": 1247
          },
          {
            "x": 2835,
            "y": 1264
          }
        ]
      },
      "description": "then"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 368,
            "y": 1480
          },
          {
            "x": 456,
            "y": 1475
          },
          {
            "x": 469,
            "y": 1710
          },
          {
            "x": 381,
            "y": 1715
          }
        ]
      },
      "description": "it"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 593,
            "y": 1466
          },
          {
            "x": 1360,
            "y": 1422
          },
          {
            "x": 1373,
            "y": 1658
          },
          {
            "x": 606,
            "y": 1702
          }
        ]
      },
      "description": "converges"
    },
    {
      "bounding_poly": {
        "vertices": [
          {
            "x": 1414,
            "y": 1419
          },
          {
            "x": 1483,
            "y": 1415
          },
          {
            "x": 1496,
            "y": 1650
          },
          {
            "x": 1427,
            "y": 1654
          }
        ]
      },
      "description": "."
    }
  ]

def sanitize(data):
    if " Theorem" in data[0]['description']:
        i = 0
        while data[i]['description'] != "Theorem":
            i += 1
        data.pop(i)
        data.insert(i, {'description': ")"})
        data.insert(1, {'description': "Theorem"})
        data.insert(2, {'description': "("})
    return data

def parse(data, latex, tail):
    #print(latex)
    if data == []:
        #print(latex + tail)
        return latex + tail
    else:
        word = fix_spell(data[0]['description'])
    
    if data[0]['description'] in thm_keywords:
        name = thm_map[word]
        latex += '\\begin{' + name + '}'
        tail = '\n\\end{' + name + '}' + tail
        if data[1]['description'] == '(':
            latex += '['
            return parse_thm(data[2:], latex, tail)
        else:
            return parse(data[1:], latex, tail)
    elif word in prf_keywords:
        latex += '\n\\begin{proof}\n'
        tail = '\n\\end{proof}' + tail
        return parse_prf(data[1:], latex, tail)
    elif word in hyphen_keywords:
        latex = latex[:-1] + word
        return parse(data[1:], latex, tail)
    elif word in colon_keywords:
        latex = latex[:-1] + word + " "
        return parse(data[1:], latex, tail)
    else:
        latex += word + ' '
        return parse(data[1:], latex, tail)


def parse_thm(data, latex, tail):
    #print(latex)
    if data == []:
        return parse(data, latex, tail)
    else:
        word = fix_spell(data[0]['description'])
    
    if word in thm_end_keywords:
        if latex[-1] == " ":
            latex = latex[:-1]
        if data[1]['description'] in thm_end_keywords:
            return parse_thm(data[1:], latex, tail)
        latex = latex + "]\n"
        return parse(data[1:], latex, tail)
    elif word in hyphen_keywords:
        latex = latex[:-1] + word
        return parse_thm(data[1:], latex, tail)
    elif word in colon_keywords:
        latex = latex[:-1] + word + " "
        return parse_thm(data[1:], latex, tail)
    else:
        latex += word + ' '
        return parse_thm(data[1:], latex, tail)

def parse_prf(data, latex, tail):
    #print(latex)
    if data == []:
        return parse(data, latex, tail)
    else:
        word = fix_spell(data[0]['description'])
    
                        
    if word in qed_keywords:
        return parse(data[1:], latex, tail)
    if word == ')':
        return parse_prf(data[1:], latex, tail)
    elif word in colon_keywords:
        latex = latex[:-1] + word + " "
        return parse_prf(data[1:], latex, tail)
    else:
        latex += word + ' '
        return parse_prf(data[1:], latex, tail)

def fix_spell(word):
    if word in spelling_map.keys():
        word = spelling_map[word]
    return word

def process(data):
    data = sanitize(data)
    result = parse(data[1:], "", "")
    print(head + result + tail)
    return head + result + tail

#process(bw)
#process(wop)
#process(rn)
#process(mct)
