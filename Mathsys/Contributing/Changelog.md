---
title: "Changelog"
description: "Mathsys update changelog."
icon: "code-pull-request"
iconType: "solid"
mode: "wide"
---

<Steps>
    <Step stepNumber="0">
        <AccordionGroup>
            <Accordion title="v0.0.1">
                ## Major
                1. Initial release.
            </Accordion>
            <Accordion title="v0.1.0">
                ## Major
                1. Added *TypeScript* compiler.
                ## Patch
                1. Completed [#1](https://github.com/abscissa-math/mathsys/issues/1)
                1. Completed [#2](https://github.com/abscissa-math/mathsys/issues/2)
                1. Completed [#3](https://github.com/abscissa-math/mathsys/issues/3)
                1. Added type annotations in *Python* compiler for some classes.
            </Accordion>
            <Accordion title="v0.2.1">
                ## Major
                1. Added support for `+` and `-` operations in the tokenizer and parser.
                ## Minor
                1. Redefined syntax.
                1. Modularized compiler.
                1. Published `pip` and `npm` packages.
                ## Patch
                1. Deleted semantic analyzer.
                1. Improved entry points.
            </Accordion>
            <Accordion title="v0.2.4">
                ## Patch
                1. Completed [#5](https://github.com/abscissa-math/mathsys/issues/5)
                1. Completed [#6](https://github.com/abscissa-math/mathsys/issues/6)
                1. Completed [#7](https://github.com/abscissa-math/mathsys/issues/7)
            </Accordion>
            <Accordion title="v0.3.0">
                ## Minor
                1. Built *IR* generator.
                1. Switched to *Lark* parser.
                ## Patch
                1. Removed *TypeScript* compiler temporarily.
                1. Defined a simple *IR* instruction set.
                1. Modularized the parser so multiple syntaxes are allowed in the future.
            </Accordion>
            <Accordion title="v0.3.1">
                ## Patch
                1. Made entry point fixed imports to `main/` dynamic.
            </Accordion>
            <Accordion title="v0.3.2">
                ## Patch
                1. Added the `syntax/` directory with its files to package-shipped files.
            </Accordion>
            <Accordion title="v0.6.1">
                ## Major
                1. Replaced *IR* generator for *LaTeX* generator.
                ## Minor
                1. Added support for multiplication.
                1. Redesigned internal syntax and removed comments in it.
                1. Added tests.
                ## Patch
                1. Improved `.gitignore` structure.
                1. Create `node` project again with commands.
                1. Improved `pip` package structure.
            </Accordion>
            <Accordion title="v0.8.0">
                ## Major
                1. Added division.
                1. Added vectors.
                ## Minor
                1. Added multiple-levels syntax hierarchy system.
                1. Added comments.
                1. Added bare expressions and equations.
                1. Improved and cleaned syntax.
                ## Patch
                1. Added `lark` dependency to *Python* package.
                1. Added `·` as a character for multiplication.
                1. Added more test cases.
            </Accordion>
            <Accordion title="v0.10.2">
                ## Major
                1. Added exponentiation.
                ## Patch
                1. Removed `sheet` types.
                1. Made comments always uppercase.
                1. Refactored `Factor` *LaTeX* generation.
                1. Added `º()` function on parser which accesses a list safely.
            </Accordion>
        </AccordionGroup>
    </Step>
    <Step stepNumber="1">
        <AccordionGroup>
            <Accordion title="v1.0.0">
                ## Major
                1. Added *Rust* runtime.
                1. Added *IR* generator.
                1. Added executable builder.
                1. Added streamlined workflows for developing on assembly and assembly support.
                ## Minor
                1. Updated syntax to make parsing possible.
                ## Patch
                1. Updated `README.md`.
                1. Improved entry point.
            </Accordion>
            <Accordion title="v1.2.7">
                ## Major
                1. Added limits.
                1. Added immutable definitions.
                ## Minor
                1. Added Greek letter mapping.
                1. Added `inf` keyword for infinity.
                ## Patch
                1. Added tags to `README.md`.
                1. Trimmed down `babel.config.json`.
                1. Improved public *API*.
                1. Added thread safety to runtime allocator.
                1. Optimized runtime `bcmp()` function.
                1. Removed mod `lib::string`.
                1. Added inlining for stack functions imported from assembly.
                1. Improved compile commands with subshells and heredocs.
                1. Renamed environment variable for the *IR* to `Mathsys`.
                1. Streamlined compilation process with `all.o` binaries.
                1. Refactored complex functions in the compilation steps to keep cyclomatic complexity under 10.
            </Accordion>
        </AccordionGroup>
    </Step>
</Steps>