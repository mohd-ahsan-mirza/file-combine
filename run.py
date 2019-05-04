import os
import sys

from combine import *

if len(sys.argv) == 2:
    file_combine = file_combine(sys.argv[1])
    file_combine.combine()
    print(file_combine.get_combined_filename())
