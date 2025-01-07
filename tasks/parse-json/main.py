import json

def main(params: dict):
  return { 
    "json": json.loads(params["string"])
   }
