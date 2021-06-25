##
## Image-Compressor-python-
## File description:
## main
##

import sys
from Kmeans import K_means

def main():
    av = sys.argv
    if (len(av) != 4) :
        return 84
    algo = K_means(av[1], int(av[2]), float(av[3]) )
    algo.start()
    algo.transform()

if __name__ == "__main__":
    main()
