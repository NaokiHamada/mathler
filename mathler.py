import argparse
import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='Mathler solver')
parser.add_argument("expression", type=str)
parser.add_argument("-c", "--chars", type=str, default="+-*/1234567890()", help="valid chars")
parser.add_argument("-t", "--trials", type=int, default=6, help="max trials")
args = parser.parse_args()

CHARS = args.chars
EXPR = args.expression
TRIALS = args.trials
M = len(CHARS)
N = len(EXPR)
ANS = eval(EXPR)


def judge(guess):
    r = [0] * N
    e = EXPR
    for i in range(N):
        if guess[i] == EXPR[i]:
            r[i] = 2
            e = e[:i] + "!" + e[i+1:]
    for i in range(N):
        if e[i] == "!":
            continue
        p = e.find(guess[i])
        if p == -1:
            continue
        e = e[:p] + "?" + e[p+1:]
        r[i] = 1
    return "".join(["_", "?", "!"][i] for i in r)


def valid(a):
    if a[0] in "0+-*/)":
        return False
    for i in range(N-1):
        if a[i] in "+-*/" and a[i+1] in "+-*/)":
            return False
    if a[-1] in "+-*/(":
        return False
    return True


def expr(pattern, priorities):
    i = pattern.find("?")
    if i == -1:
        return pattern
    pri = dict(sorted(priorities[i].items(), key=lambda x: x[1]))
    for c in pri:
        pat = pattern[:i] + c + pattern[i+1:]
        if not valid(pat):
            continue
        for p in priorities:
            p[c] += 1  # used once
        e = expr(pat, priorities)
        for p in priorities:
            p[c] -= 1
        try:
            ans = eval(e)
        except:
            continue
        if ans == ANS:
            return e


pattern = "?" * N
priorities = [{c: 0 for c in CHARS} for _ in range(N)]

print(f"Find the hidden calculation that equals {ANS}")
for trial in range(1, TRIALS + 1):
    print()
    print(f"Trial = {trial}/{TRIALS}")
    guess = expr(pattern, priorities)
    hints = judge(guess)
    print(f"Guess = {guess}")
    print(f"Hint  = {hints}")
    if hints == "!" * N:
        print()
        print(f"Solved: {guess}")
        exit(0)
    else:
        for i in range(N):
            if hints[i] == "!":
                priorities[i][guess[i]] -= N * 10**3  # must be here
                pattern = pattern[:i] + guess[i] + pattern[i+1:]
                for p in priorities:
                    p[guess[i]] += N * 10**1  # may not be here
            elif hints[i] == "?":
                priorities[i][guess[i]] += N * 10**3  # must not be here
                for p in priorities:
                    p[guess[i]] -= N * 10**2  # may be here
            else:  # hints[i] == 0
                for p in priorities:
                    p[guess[i]] += N * 10**2

print()
print("Failed.")
exit(1)
