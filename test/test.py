import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start T Flip Flop Test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Initial values
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # Release reset
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 10)

    # tin = 0, output should hold
    dut.ui_in[0].value = 0
    await ClockCycles(dut.clk, 20)

    # tin = 1, output should toggle
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 20)

    # tin = 0, output should hold again
    dut.ui_in[0].value = 0
    await ClockCycles(dut.clk, 20)

    # tin = 1, toggle again
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 20)

    # Reset again
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 10)

    dut._log.info("T Flip Flop Test Completed")
