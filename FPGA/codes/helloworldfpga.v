module helloworldfpga(

    input  wire U,
    input  wire V,
    input  wire W,
    
    output wire G,
    );
   // assign U=0;
    //assign V=0;
    //assign W=0;
    
    always @(*)
    begin
   G=(V|!W)&(U|!W)&(!U|!V|W); 
    end
    endmodule
