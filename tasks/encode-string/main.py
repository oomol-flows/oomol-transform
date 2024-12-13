from typing import Literal

def main(inputs: dict):
  string: str = inputs["string"]
  encoding: Literal["utf8", "ascii", "hex"] = inputs["encoding"]
  return {
    "binary": string.encode(encoding),
  }
