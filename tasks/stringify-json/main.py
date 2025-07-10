import json

#region generated meta
import typing
class Inputs(typing.TypedDict):
  json: typing.Any
  indent: int
  ensure_ascii: bool
class Outputs(typing.TypedDict):
  string: str
#endregion

def main(params: Inputs) -> Outputs:
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
