## How it works

This project implements a T flip-flop, also known as a toggle flip-flop.

The input is:
- tin

The outputs are:
- q
- qbar

When tin = 0, the flip-flop holds its previous state.  
When tin = 1, the output q toggles on every rising clock edge.  
The qbar output is always the complement of q.

## How to test

Reset is first applied by setting rst_n = 0. After reset is released, tin is changed between 0 and 1.

Expected behavior:
- If tin = 0, q holds its previous value.
- If tin = 1, q toggles at the rising edge of clk.
- qbar is always the opposite of q.

## External hardware

None

## Pinout

### Inputs
- ui[0] = tin

### Outputs
- uo[0] = q
- uo[1] = qbar<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Explain how your project works

## How to test

Explain how to use your project

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
