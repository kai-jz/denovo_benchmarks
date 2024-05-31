"""TODO"""

import argparse
import re
import pandas as pd
from base import OutputMapperBase


class OutputMapper(OutputMapperBase):
    pass
    # Redefine base class methods 
    # or implement new methods if needed.
    

parser = argparse.ArgumentParser()
parser.add_argument(
    "output_path", help="The path to the algorithm predictions file."
)
args = parser.parse_args()

# Read predictions from output file
output_data = pd.read_csv(args.output_path, sep="\t")

# Rename columns to the expected names
output_data = output_data.rename(
    {
        "output_seq": "sequence",
        "output_score": "score",
        "scan": "scans",
    },
    axis=1,
)

# Transform data to the common output format
output_mapper = OutputMapper()
output_data = output_mapper.format_output(output_data)

# Save processed predictions to outputs.csv
# (the expected name for the algorithm output file)
output_data.to_csv("outputs.csv", index=False)
