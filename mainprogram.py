# mainprogram.py

import mypkg.module1
mypkg.module1.bar()

from mypkg import module2
module2.foo()

import mypkg
print(mypkg)