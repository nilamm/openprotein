import os
import sys
sys.path.append(r'/home/jupyter/openprotein')

from preprocessing import process_raw_data

IN_DIR = '/home/jupyter/data/casp12/'
OUT_DIR = '/home/jupyter/data/casp12-preprocessed/'

if os.path.exists(os.path.join(IN_DIR, sys.argv[1])):
    print("Preprocessing:", os.path.join(IN_DIR, sys.argv[1]))
    process_raw_data(use_gpu=False,
                     raw_data_path=os.path.join(IN_DIR, sys.argv[1]),
                     force_pre_processing_overwrite=True,
                     output_path=OUT_DIR)
else:
    print("Path doesn't exist:", os.path.join(IN_DIR, sys.argv[1]))


