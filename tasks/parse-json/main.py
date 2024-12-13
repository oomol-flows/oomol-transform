import json

def main(inputs: dict):
  return { 
    "json": json.loads(inputs["string"])
   }
