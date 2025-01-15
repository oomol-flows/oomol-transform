from charset_normalizer import from_bytes

def main(params: dict):
  binary: bytes = params["binary"]
  encoding: str | None = params["encoding"]
  if encoding is None:
    results = from_bytes(binary).best()
    if results is None:
      encoding = "utf_8"
    else:
      encoding = results.encoding

  return { 
    "string": binary.decode(encoding),
    "encoding": encoding,
  }