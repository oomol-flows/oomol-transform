from json import loads, JSONDecodeError
from typing import Any
from oocana import Context
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError


#region generated meta
import typing
class Inputs(typing.TypedDict):
  object: dict
  disable_additional_properties: bool
Outputs = typing.Dict[str, typing.Any]
#endregion

def main(params: Inputs, context: Context) -> Outputs:
  object: dict[str, Any] = params["object"]
  output_keys = sorted(list(context.outputs_def.keys()))
  outputs_required: list[str] = []
  outputs_properties: dict[str, Any] = {}

  for key in output_keys:
    handle = context.outputs_def[key]
    if not handle["nullable"]:
      outputs_required.append(key)
    json_schema: dict[str, Any] | None = handle["json_schema"]
    if json_schema is None:
      json_schema = {}
    outputs_properties[key] = json_schema

    # TODO: oocana 的 bug 导致会多一个 contentMediaType 字段
    #       等待修复后删除如下防御性代码
    json_schema.pop("contentMediaType", None)

  try:
    validate(
      instance=object,
      schema={
        "type": "object",
        "additionalProperties": not params["disable_additional_properties"],
        "required": outputs_required,
        "properties": outputs_properties,
      },
    )
  except SchemaError as err:
    raise RuntimeError("invalid JSON Schema") from err
  except ValidationError as err:
    raise ValueError("invalid JSON: cannot pass JSON Schema validation") from err

  outputs_object: dict[str, Any] = {}
  for key in output_keys:
    if key not in object:
      continue
    value = object[key]
    if value is None and context.outputs_def[key]["nullable"]:
      continue
    outputs_object[key] = value
  return outputs_object
