import urllib.request
import ssl
import json
import argparse
import feature_compiler

parser = argparse.ArgumentParser()
parser.add_argument("entity", help = "The ID of the test plan you wish to extract data from", type = str, nargs="+")
args = parser.parse_args()

class Target_Process():     
    def __init__(self):
        self.tp_uri = "https://bluefruit.tpondemand.com/api/v1/"
        self.token = "NTE6V0FMZWJ1c2dkTkZ1aDVKdzRSM0FHSGFYM3pJd0IraUhnR016UzRqS0NiUT0="

    def get_tests(self, entities):
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        request = urllib.request.Request(self.tp_uri + "TestPlans/" + entities + "/TestCases/?format=json&include=[ID,Name,TestSteps[Description],TestPlans]" + "&access_token=" + self.token)
        request.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(request, context=ctx)
        return response.read().decode("UTF-8")

def main():
    request = Target_Process()
    for item in args.entity:
        data = json.loads(request.get_tests(item))
        feature_compiler.json_parser(data)

if(__name__ == "__main__"):
    main()