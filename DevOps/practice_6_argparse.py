﻿import os
import re
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Short sample app')

    parser.add_argument('-a', action="store_true", default=False)
    parser.add_argument('-b', action="store", dest="b")
    parser.add_argument('-c', action="store", dest="c", type=int)

    # print(parser.parse_args(['-a', '-bval', '-c', '3']))
    print(parser.parse_known_args()) 
