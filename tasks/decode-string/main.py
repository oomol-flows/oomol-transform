from typing import Literal

def main(params: dict):
  binary: bytes = params["binary"]
  encoding: Literal["utf8", "ascii", "hex"] = params["encoding"]
  return { 
    "string": binary.decode(encoding)
  }