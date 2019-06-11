#読む たぶん整数と小数を整数と小数にするやつ
def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index

# 各計算記号をtokenという辞書に入れる
def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMultipled(line, index):
  token = {'type': 'MULTIPLED'}
  return token, index + 1

def readDivided(line, index):
  token = {'type': 'DIVIDED'}
  return token, index + 1

# 分割して、数字や計算記号を読んだら上のやつに投げる
# tokensっていうリストを作る
def tokenize(line): # 字句に分割する
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMultipled(line, index)
    elif line[index] == '/':
      (token, index) = readDivided(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens

# 掛け算と割り算を計算する
def evaluate1(tokens): # 字句の並びを計算する
    tokens2 = tokens
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLED':
                # tokens2の方で、かけたやつをリストの後ろに入れる
                tokens2.insert(index + 1, {'type': 'NUMBER', 'number': tokens[index - 2]['number'] * tokens[index]['number']})
                # tokens2の方で、元のかけ算パートを消す
                del tokens2[index - 2:index + 1]
                index -= 2
            elif tokens[index - 1]['type'] == 'DIVIDED':
                tokens2.insert(index + 1, {'type': 'NUMBER', 'number': tokens[index - 2]['number'] / tokens[index]['number']})
                del tokens2[index - 2:index + 1]
                index -= 2
        index += 1
    return tokens2


def evaluate2(tokens2): # 字句の並びを計算する
  answer = 0
  tokens2.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(tokens2):
    if tokens2[index]['type'] == 'NUMBER':
      if tokens2[index - 1]['type'] == 'PLUS':
        answer += tokens2[index]['number']
      elif tokens2[index - 1]['type'] == 'MINUS':
        answer -= tokens2[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def test(line):
  tokens = tokenize(line)
  tokens2 = evaluate1(tokens)
  actualAnswer = evaluate2(tokens2)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("3*4")
  test("3.8*4.2")
  test("8/4")
  test("4.9/3.4")
  test("8*3+4-16/2")
  test("4+6.2*4-9.1+2.2/2")
  test("6+5.5*7/2")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input() # 1行読む
  tokens = tokenize(line) # 字句に分割する
  tokens2 = evaluate1(tokens) # かけ算を計算する
  answer = evaluate2(tokens2) # 足し算を計算する
  print("answer = %f\n" % answer)
