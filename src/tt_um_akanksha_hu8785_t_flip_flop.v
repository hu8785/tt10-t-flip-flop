`default_nettype none

module tt_um_akanksha_hu8785_t_flip_flop (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire tin = ui_in[0];

    reg tq;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            tq <= 1'b0;
        else if (tin)
            tq <= ~tq;
    end

    assign uo_out[0] = tq;
    assign uo_out[1] = ~tq;
    assign uo_out[2] = 1'b0;
    assign uo_out[3] = 1'b0;
    assign uo_out[4] = 1'b0;
    assign uo_out[5] = 1'b0;
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    wire _unused = &{ena, ui_in[7:1], uio_in, 1'b0};

endmodule

`default_nettype wire
