import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start T Flip Flop Test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    assert dut.uo_out[0].value == 0

    # Release reset
    dut.rst_n.value = 1
    dut.ui_in[0].value = 0
    await ClockCycles(dut.clk, 2)

    # tin = 0, output should hold
    q_before = dut.uo_out[0].value
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out[0].value == q_before

    # tin = 1, output should toggle
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 1)
    q1 = dut.uo_out[0].value
    await ClockCycles(dut.clk, 1)
    q2 = dut.uo_out[0].value
    assert q1 != q2

    # qbar should be complement of q
    assert dut.uo_out[1].value != dut.uo_out[0].value

    # tin = 0 again, output should hold
    dut.ui_in[0].value = 0
    q_hold = dut.uo_out[0].value
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out[0].value == q_hold

    dut._log.info("T Flip Flop Test Completed")
