from interpreter import Interpreter
import sys


if __name__ == "__main__":
    interp = Interpreter()
    text = ''
    code = []
    while text != 'END.':
        print("in> ", end="")
        text = input()
        print(f": {text}")
        code.append(text)
    text = " ".join(code)
    try:     
        result = interp.eval(text)
        if len(result) == 0:
            print(f"out>")
        else:
            print(f"out> {result}")      
    except (SyntaxError, ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
    print("Done!")
