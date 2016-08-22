import os
from datetime import date, timedelta
import logging
from argparse import ArgumentParser

# Script name
SCRIPT_NAME = ""
# Script description
SCRIPT_DESCRIPTION = ""
'''
Arguments:
'''

if __name__ == '__main__':

    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    logging.info("Running %" % SCRIPT_NAME)

    # Parse arguments from command line
    arg_parser = ArgumentParser(description=SCRIPT_DESCRIPTION)

    # Arguments
    # Example: arg_parser.add_argument('--argument', metavar='A', default=30, help='Argument help')

    args = arg_parser.parse_args()
