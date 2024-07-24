# KeyValidator
This was inspiried by making https://github.com/streaak/keyhacks faster and easier to check!

Currently it only supports Heroku keys but will constantly be updated to add more features as we go. The file can either be a direct paste from [secretsfinder](https://github.com/m4ll0k/SecretFinder), or the keys themselves. The program submits the requests then returns valid or invalid based on the results, please be aware there may be false positves, if you recieve a valid, please still manually test.

## Getting Started
Python is required for this program, along with the libraries:
- argparse
- subprocess
- json
- re
- concurrent.futures
  
Please verify these are installed if the program is not working. Once the program is installed you can run it using a list by the following command below. Using a single key mostly defeats the purpose and can easily be done just using the SecretFinder github so that has not been added *yet*, I still plan to do so eventually.
  
`python3 KeyValidator.py -l keys.txt`
