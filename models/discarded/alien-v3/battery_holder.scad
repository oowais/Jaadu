include <globals.scad>

module battery_holder(x, y, z) {
    battery_x = 9.8; 
    battery_y = 4.6; 
    battery_z = 2.7; 
    difference() {
        cube([x, y, z]);
        translate([-0.2, (y-battery_y)/2, (z-battery_z)/2]) cube([battery_x, battery_y, battery_z]);
    }
}

$fn=300;
scale([10, 10, 10]) battery_holder(x=total_x, y=bh_y, z=bh_z);