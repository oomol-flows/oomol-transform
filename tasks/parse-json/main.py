from json import loads, JSONDecodeError
from typing import Any


#region generated meta
import typing
class Inputs(typing.TypedDict):
  string: str
class Outputs(typing.TypedDict):
  json: typing.Any
#endregion

def main(params: Inputs) -> Outputs:
  json_object: Any
  try:
    json_object = loads(params["string"])
  except JSONDecodeError as err:
    raise ValueError("Invalid JSON") from err
  if not isinstance(json_object, dict):
    raise ValueError("JSON value isn't a object")
  return { "json": json_object }
