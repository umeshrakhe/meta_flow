import argparse
"""
import yaml
def load_conf_file(config_file):
   with open(config_file, "r") as f:
       config = yaml.safe_load(f)
       server_conf = config[0]["server"]
       exec_conf = config[1]["execution"]
   return server_conf, exec_conf
   """

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', choices=['dev', 'prod'], required=True)
    #parser.add_argument('--file', type=open, action=LoadFromFile, required=True)
    parser.add_argument('--srcCd', type=str, required=True, help="Source file code")
    parser.add_argument('--feed', type=str, required=True, help="Feed file Name with Path")
    parser.add_argument('--cobDt', type=str, required=True, help="Cob Date")
    parser.add_argument('--usrName', type=str, required=True, help="Database username")
    parser.add_argument('--host', type=str, required=True, help="Database hostname")
    parser.add_argument('--pwd', type=str, required=True, help="Database password")
    parser.add_argument('--database', type=str, required=True, help="Database name")
    parser.add_argument('--port', type=int, required=False, default=8889)
    
    return vars(parser.parse_args())

class LoadFromFile (argparse.Action):
    def __call__ (self, parser, namespace, values, option_string = None):
        with values as f:
            # parse arguments in the file and store them in the target namespace
            #args = (f.read().split())
            #return args
            parser.parse_args(f.read().split(), namespace)

class OracleDbConnection:
    def __init__(self):
        pass