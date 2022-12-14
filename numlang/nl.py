import argparse, math

def run(code, *, x=0, y=None, i=0, l=None, n=0, last_int='n', last_list='l', last_var='l'):
    if y is None:
        y = []
    if l is None:
        l = []
    index = 0
    while index < len(code):
        c = code[index]
        if c == '#':
            x = int(input())
            last_int = last_var = 'x'
        elif c == '$':
            y = [int(_) for _ in input().split()]
            last_list = last_var = 'y'
        elif c == 'S':
            if last_list == 'l':
                l.sort()
            else:
                y.sort()
            last_var = last_list
        elif c == 'D':
            unique = []
            if last_list == 'l':
                for item in l:
                    if item not in unique:
                        unique.append(item)
                l = unique.copy()
            else:
                for item in y:
                    if item not in unique:
                        unique.append(item)
                y = unique.copy()
            last_var = last_list
        elif c == 'A':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            if last_list == 'y':
                y.append(eval(z, locals()))
            else:
                l.append(eval(z, locals()))
            last_var = last_list
        elif c == 'W':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            el = eval(z, locals())
            if last_list == 'y':
                while el in y:
                    y.remove(el)
            else:
                while el in l:
                    l.remove(el)
            last_var = last_list
        elif c == 'R':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            last_var = str(list(range(eval(z, locals()))))
        elif c == 'O':
            print(eval(str(last_var), locals()))
        elif c in 'Ff':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            num = eval(z, locals())
            factors = [r for r in range(1, num+1) if not num % r]
            last_var = str(factors)
            if c == 'F':
                last_list = 'l'
                l = factors.copy()
        elif c in 'Rr':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            num = eval(z, locals())
            primes = []
            _ = 2
            while len(primes) < num:
                if all(_%d for d in range(2,_)):
                    primes.append(_)
            last_var = str(primes)
            if c == 'F':
                last_list = 'l'
                l = primes.copy()
        elif c in 'Mm':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            num = eval(z, locals())
            primes = []
            _ = 1
            while len(primes) < num:
                _ += 1
                m = 2**_ - 1
                if all(m%k for k in range(2,m)):
                    primes.append(m)
            last_var = str(primes)
            if c == 'M':
                last_list = 'l'
                l = primes.copy()
        elif c in 'Gg':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            lst = eval(z, locals())
            last_var = math.gcd(*lst)
            if c == 'G':
                last_int = 'n'
                n = last_var
        elif c in 'Cc':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            lst = eval(z, locals())
            last_var = math.lcm(*lst)
            if c == 'C':
                last_int = 'n'
                n = last_var
        elif c == '?':
            z = ''
            index += 1
            while code[index] != ';':
                z += code[index]
                index += 1
            if eval(z, {**locals(), **{'P': lambda _: all(_%d for d in range(2,_))}}):
                z = ''
                index += 1
                while code[index] != ';':
                    z += code[index]
                    index += 1
                    if index >= len(code):
                        break
                last_var = eval(z, locals())
        elif c == '{':
            z = ''
            index += 1
            while code[index] != '}':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            for _i in eval(last_var, locals()):
                last_var = run(z, x=x, y=y, i=_i, l=l, n=n, last_int=last_int, last_list=last_list, last_var=last_var)
                print(last_var)
        elif c in '+-*/^%':
            z = str(last_var)
            while code[index] != ';':
                z += code[index]
                index += 1
                if index >= len(code):
                    break
            last_var = eval(z.replace('/', '//').replace('^', '**'), locals())
        elif c in 'xin':
            last_int = last_var = c
        elif c in 'yl':
            last_list = last_var = c
        index += 1
    return eval(str(last_var), locals())
  
run_interface = lambda code_to_run: run(code_to_run)

def from_console():
    parser = argparse.ArgumentParser(prog ='numlang',
                                     description ='Run NumLang code using the numlang command')
    parser.add_argument('code', metavar ='code', type=str, nargs=1, help= 'The NumLang code to run')
    args = parser.parse_args()
    print(run_interface(args.code[0]))
