---
title: "Exit"
description: "Crashes the runtime and returns the exit code."
icon: "arrow-right-from-bracket"
iconType: "solid"
---

## Parameters
<ParamField path="code" type="u8" required/>

## Response
<ResponseField name="" type="!" required/>

<RequestExample>
```rust From main.rs
stack::system::exit(code);
```
```rust Elsewhere
crate::stack::system::exit(code);
```
</RequestExample>

<ResponseExample>
```rust Wrapper system.rs
https://raw.githubusercontent.com/alejandro-vaz/mathsys/main/python/mathsys/bin/stack/system.rs
```
</ResponseExample>


## Implementation
<CodeGroup dropdown>
```asm exit.asm lines expandable
https://raw.githubusercontent.com/alejandro-vaz/mathsys/main/python/mathsys/bin/unix/x86/64/system/exit.asm
```
```wasm exit.wat lines expandable
https://raw.githubusercontent.com/alejandro-vaz/mathsys/main/python/mathsys/bin/web/system/exit.wat
```
</CodeGroup>