import json

def main(params: dict):
  json_value = params["json"]
  indent: int | None = params["indent"]
  ensure_ascii: bool = params["ensure_ascii"]

  if indent == 0:
    indent = None

  return { 
    "string": json.dumps(
      obj=json_value,
      indent=indent,
      ensure_ascii=ensure_ascii,
    ),
  }
