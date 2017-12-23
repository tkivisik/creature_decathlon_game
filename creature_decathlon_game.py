import sys
from creatures import *

def main(*args):
    if True:
        for i in range(50):
            marko = Human("Marko_{}".format(str(i).rjust(2, "0")))
            print(marko)
            glaenir = Elf("Glaenir_{}".format(str(i).rjust(2, "0")))
            print(glaenir)
            vidarok = Orc("Vidarok_{}".format(str(i).rjust(2, "0")))
            print(vidarok)
    print args


if __name__ == '__main__':
    main(sys.argv)
