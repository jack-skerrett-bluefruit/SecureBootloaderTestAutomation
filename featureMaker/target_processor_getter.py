import urllib.request
import ssl
import json
import argparse
import featureCompiler

parser = argparse.ArgumentParser()
parser.add_argument("entity", help = "The ID of the test plan you wish to extract data from", type = str)
args = parser.parse_args()

class Target_Process(): 

     
    def __init__(self, tp_name,token):
        self.tp_uri = tp_name
        self.token = token

    def get_tests(self, entities): #this is mostly copy paste from the tutorial on the wiki so I need to figure out EXACTLY what it's doing
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        request = urllib.request.Request(self.tp_uri + "TestPlans/" + entities + "/TestCases/?format=json&include=[ID,Name,TestSteps[Description],TestPlans]" + "&access_token=" + self.token)
        request.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(request, context=ctx)
        return response.read().decode("UTF-8")

def main():
    request = Target_Process('https://bluefruit.tpondemand.com/api/v1/', "NTE6V0FMZWJ1c2dkTkZ1aDVKdzRSM0FHSGFYM3pJd0IraUhnR016UzRqS0NiUT0=")

    data = json.loads(request.get_tests(args.entity))
    featureCompiler.json_parser(data)


if(__name__ == "__main__"):
    main()