# oomol-transform

Common data conversion.

## Encode string

Encode the string passed in the `string` field into binary data and return it in the `binary` field.

`encoding` indicates the encoding format of the string.

## Decode string

Decode the binary data passed in the `binary` field into a string and return it in the `string` field.

`encoding` indicates the encoding format of the string.

## Stringify JSON

Encode the data passed in the `json` field into a JSON-formatted string and return it in the `string` field.

`indent` indicates how many spaces are used for indentation in the final JSON string. If the value is 0, the JSON is formatted in a compact format.

`ensure_ascii` indicates whether non-ASCII characters are escaped in the final JSON string.

## Parse JSON

Parse the string passed in the `string` field in JSON format and return it in the `json` field.