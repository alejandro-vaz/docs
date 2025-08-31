---
title: "Write"
description: "Prints all bytes until it finds a null one."
icon: "pen"
iconType: "solid"
---

## Parameters
<ParamField path="pointer" type="*const u8" required/>

## Response
<ResponseField name="" type="()" required/>

<RequestExample>
```rust From main.rs
stack::system::write(pointer);
```
```rust Elsewhere
crate::stack::system::write(pointer);
```
</RequestExample>

<ResponseExample>
```rust Wrapper system.rs
https://raw.githubusercontent.com/alejandro-vaz/mathsys/main/python/mathsys/bin/stack/system.rs
```
</ResponseExample>


## Implementation
<CodeGroup dropdown>
```asm write.asm lines expandable
https://raw.githubusercontent.com/alejandro-vaz/mathsys/main/python/mathsys/bin/unix/x86/64/system/write.asm
```
```wasm write.wat lines expandable
https://raw.githubusercontent.com/alejandro-vaz/mathsys/main/python/mathsys/bin/web/system/write.wat
```
</CodeGroup>