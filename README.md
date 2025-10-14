# Transform

A collection of essential data conversion blocks for the OOMOL platform.

## Overview

The Transform package provides fundamental building blocks for converting data between different formats in your OOMOL workflows. Whether you're working with strings, binary data, or JSON objects, these blocks help you seamlessly transform data from one format to another.

## Use Cases

- **Data Processing Pipelines**: Convert between text and binary formats when working with files or network data
- **API Integration**: Parse JSON responses from web services or format data for API requests
- **File Operations**: Encode and decode files with different character encodings
- **Data Formatting**: Control how JSON data is displayed with custom indentation and character encoding

## Available Blocks

### Encode String

Converts a text string into binary data using a specified character encoding.

**Inputs:**
- `string` - The text string to encode
- `encoding` - The character encoding format to use (default: UTF-8)

**Outputs:**
- `binary` - The encoded binary data

**Common Uses:**
- Preparing text data for file writing
- Converting strings before network transmission
- Working with different character sets (UTF-8, ASCII, etc.)

---

### Decode String

Converts binary data back into a readable text string.

**Inputs:**
- `binary` - The binary data to decode
- `encoding` - The character encoding format (optional - auto-detected if not specified)

**Outputs:**
- `string` - The decoded text string
- `encoding` - The detected or used encoding format

**Common Uses:**
- Reading binary file contents as text
- Processing received network data
- Converting data from different encoding formats

---

### Stringify JSON

Converts a JSON object into a formatted text string.

**Inputs:**
- `json` - The JSON object to convert
- `indent` - Number of spaces for indentation (0 = compact format, >0 = pretty format)
- `ensure_ascii` - Whether to escape non-ASCII characters (useful for compatibility)

**Outputs:**
- `string` - The formatted JSON string

**Common Uses:**
- Preparing JSON data for file storage
- Formatting JSON for display or logging
- Creating API request payloads
- Controlling JSON output formatting

---

### Parse JSON

Converts a JSON-formatted text string into a usable JSON object.

**Inputs:**
- `string` - The JSON-formatted text to parse

**Outputs:**
- `json` - The parsed JSON object

**Common Uses:**
- Reading JSON configuration files
- Processing API responses
- Converting JSON strings to structured data

---

### Extract Object

Splits a JSON object into individual fields for separate processing.

**Inputs:**
- `object` - The JSON object to extract fields from
- `disable_additional_properties` - When enabled, only extracts specified fields and reports an error if extra fields exist

**Outputs:**
- Dynamic outputs based on the object's fields

**Common Uses:**
- Breaking down complex objects into individual components
- Extracting specific data from API responses
- Validating object structure

## Example Workflows

### Encode & Decode
A simple workflow that demonstrates encoding a string to binary and decoding it back to text. This is useful for understanding how text data is stored and transmitted in binary format.

### Parse & Stringify
A workflow that converts JSON objects to formatted strings and back. Perfect for learning how to control JSON formatting and work with structured data.

## Getting Started

1. Add the Transform package to your OOMOL project
2. Drag and drop the blocks you need into your workflow
3. Connect the blocks to create your data transformation pipeline
4. Configure the encoding or formatting options as needed

## Technical Details

- **Version**: 0.0.7
- **Repository**: [github.com/oomol-flows/oomol-transform](https://github.com/oomol-flows/oomol-transform)
- **License**: Open source

## Support

For issues, feature requests, or contributions, please visit the [GitHub repository](https://github.com/oomol-flows/oomol-transform).
