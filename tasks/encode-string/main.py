from typing import Literal

def main(params: dict):
  string: str = params["string"]
  encoding: Literal["utf8", "ascii", "hex"] = params["encoding"]
  return {
    "binary": string.encode(encoding),
  }
