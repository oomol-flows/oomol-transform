def main(params: dict):
  string: str = params["string"]
  encoding: str = params["encoding"]
  return {
    "binary": string.encode(encoding),
  }
