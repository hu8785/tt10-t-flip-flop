## How it works

This project implements a T flip-flop, also known as a toggle flip-flop.

The input is tin.

The outputs are q and qbar.

When tin is 0, the flip-flop holds its previous state. When tin is 1, the output q toggles on every rising edge of the clock. The qbar output is always the complement of q.

## How to test

Reset is first applied by setting rst_n to 0. After reset is released, tin is changed between 0 and 1.

Expected behavior:

- When tin is 0, q holds its previous value.
- When tin is 1, q toggles at the rising edge of clk.
- qbar is always the opposite of q.

## External hardware

None

## Pinout

### Inputs

| Pin | Name |
|---|---|
| ui[0] | tin |

### Outputs

| Pin | Name |
|---|---|
| uo[0] | q |
| uo[1] | qbar |
