from __future__ import division, print_function
 
import os
import sys
from io import BytesIO, IOBase
from collections import deque
 
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
else:
    _str = str
    str = lambda x=b"": x if type(x) is bytes else _str(x).encode()
 
 
def main():
    n = int(readline())
    a = deque(readlist())
 
    res, seq = [], [0]
    while a:
        if len(a) == 1 and a[0] > seq[-1]:
            seq.append(a.pop())
            res.append('R')
        elif a[0] < a[-1] and a[0] > seq[-1]:
            seq.append(a.popleft())
            res.append('L')
        elif a[-1] < a[0] and a[-1] > seq[-1]:
            seq.append(a.pop())
            res.append('R')
        elif a[0] == a[-1] and a[0] > seq[-1]:
            case_1, case_2 = 1, 1
            start = a[0]
            i = 1
            while i < len(a) and a[i] > start:
                start = a[i]
                i += 1
                case_1 += 1
            start = a[-1]
            i = len(a) - 2
            while i >= 0 and a[i] > start:
                start = a[i]
                i -= 1
                case_2 += 1
            res += ['L'] * case_1 if case_1 > case_2 else ['R'] * case_2
            break
        elif a[0] > seq[-1]:
            seq.append(a.popleft())
            res.append('L')
        elif a[-1] > seq[-1]:
            seq.append(a.pop())
            res.append('R')
        else:
            break
 
    print(len(res))
    print(''.join(res))
 
 
# region template
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._buffer = BytesIO()
        self._fd = file.fileno()
        self._writable = "x" in file.mode or "r" not in file.mode
        self.write = self._buffer.write if self._writable else None
 
    def read(self):
        if self._buffer.tell():
            return self._buffer.read()
        return os.read(self._fd, os.fstat(self._fd).st_size)
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self._buffer.tell()
            self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr)
        self.newlines -= 1
        return self._buffer.readline()
 
    def flush(self):
        if self._writable:
            os.write(self._fd, self._buffer.getvalue())
            self._buffer.truncate(0), self._buffer.seek(0)
 
 
class ostream:
    def __lshift__(self, a):
        if a is endl:
            sys.stdout.write(b"\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(str(a))
        return self
 
 
def print(*args, **kwargs):
    sep, file = kwargs.pop("sep", b" "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", b"\n"))
    if kwargs.pop("flush", False):
        file.flush()
 
 
sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
cout, endl = ostream(), object()
 
readline = sys.stdin.readline
readlist = lambda var=int: [var(n) for n in readline().split()]
input = lambda: readline().rstrip(b"\r\n")
 
# endregion
 
if __name__ == "__main__":
    main()