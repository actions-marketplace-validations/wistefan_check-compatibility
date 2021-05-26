# Check compatibility

This action helps to persist and check compatibility information. The action uses a json file, to persist or read the information.

A compatibility file will look as following:
```json
[
    {
        "mintaka" : "0.1.2",
        "orion" : "0.6.0",
        "compatible": false
    },
    {
        "mintaka" : "0.1.2",
        "orion" : "0.7.0",
        "compatible": true
    },
    {
        "mintaka" : "0.2.0",
        "orion" : "0.7.0",
        "compatible": true
    }
]
```

The action provides the following functionality:

### IS_COMPATIBLE

Check if the given components are marked as compatible in the provided compatibility file.


Usage: 

```yaml
uses: wistefan/check-compatibility@master
with:
    componentOne: "orion"
    componentTwo: "mintaka"
    versionOne: "0.7.0"
    versionTwo: "0.1.2"
```
If not file or entry exists, the compatibiltiy is unkown and will lead to failure, as it will when marked ```false```

### PERSIST_INFO

Insert(add|replace) the given info to the file or create a new one.

Usage: 

```yaml
uses: wistefan/check-compatibility@master
with:
    operation: PERSIST_INFO
    componentOne: "orion"
    componentTwo: "mintaka"
    versionOne: "0.7.0"
    versionTwo: "0.1.2"
    compatible: True
```

### MARKDOWN

Formats the given json to a markdown table for further usage(f.e. in github readmes).

Usage: 

```yaml
uses: wistefan/check-compatibility@master
with:
    operation: MARKDOWN
    componentOne: "orion"
    componentTwo: "mintaka"
```

With the example json on top, this will produce the following table:

| Orion | Mintaka | Compatible |
|-------|---------|------------|
|```0.6.0```|```0.1.2```|```false```|
|```0.7.0```|```0.1.2```|```true```|
|```0.7.0```|```0.2.0```|```true```|

## Inputs

### `operation`

The operation to be executed. Possible values: ["IS_COMPATIBLE", "PERSIST_INFO", "MARKDOWN"]. Default: "IS_COMPATIBLE"

### `compatibilityFile`

**Required** Path to the compatibility file.

### `componentOne`

**Required** Name of the first component to be handled.

### `componentTwo`

**Required** Name of the second component to be handled.

### `versionOne`

Version of the first component to be handled. **Required** for operations ['IS_COMPATIBLE', 'PERSIST_INFO']

### `versionTwo`

Version of the second component to be handled. **Required** for operations ['IS_COMPATIBLE', 'PERSIST_INFO'

### `compatible`

Compatibility information for operation 'PERSIST_INFO'. Possible values: [True, False]


## Example usage

```yaml
uses: wistefan/check-compatibility@master
with:
    componentOne: "orion"
    componentTwo: "mintaka"
    versionOne: "0.7.0"
    versionTwo: "0.1.2"
```