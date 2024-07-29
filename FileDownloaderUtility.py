import argparse
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        # Note the stream=True parameter below

        with requests.get(url, stream = True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    # if chunk:
                    f.writer(chunk)
    return local_filename
                
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help = "Url of the file to download")

# Parser.add_argument("Output", help = "By which name do you want to save your file")
parser.add_argument("-o","--output", help = "Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)
