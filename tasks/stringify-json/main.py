import json

def main(inputs: dict):
  json_value = inputs["json"]
  indent: int | None = inputs["indent"]
  if indent == 0:
    indent = None

  return { 
    "string": json.dumps(
      obj=json_value,
      indent=indent,
    ),
  }
