module down_holder() {
    difference() {
        union() {
            translate([-0.25, 0, 0]) cube([0.5, 1.4, 0.4]); // Holder base
            
            cylinder(r=0.25, h=2); // Right holder 
            
            translate([0, 1.4, 0]) cylinder(r=0.25, h=2); // left holder
        } 
        
        translate([0, 2.45, 1.3]) rotate([90, 0, 0]) cylinder(r=0.21, h=3.85); // cuts to put holder pin
    }
}

$fn=300;
scale([10, 10, 10]) down_holder();