from typing import Literal

def main(inputs: dict):
  binary: bytes = inputs["binary"]
  encoding: Literal["utf8", "ascii", "hex"] = inputs["encoding"]
  return { 
    "string": binary.decode(encoding)
  }