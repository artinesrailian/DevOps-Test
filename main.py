import argparse
import utils.square as square

# Version of the script
__version__ = '1.0.0'

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--version', action='store_true', help='Display the script version')

# Parse the command line arguments
args = parser.parse_args()

# Check if the version argument is specified
if args.version:
    print("DevOps-Test Version:", __version__)
else:
    # This is the main application which calls the square function
    square.square()
    input("Press 'Enter' key to exit ...")
    pass
