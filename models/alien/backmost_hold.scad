include <globals.scad>
use <top.scad>

module backmost_hold(x, y, z) {
    difference() {
        cube([x, y, z]);
        translate([-0.01, 0, z]) rotate([-elevation_deg, 0, 0]) top(x=x+0.2, z=3);
        for (i = [2.5: 2.5: x-2.5]) {
            translate([i, 0.3, z-1]) rotate([-elevation_deg, 0, 0]) cylinder(r=screw_r, h=1);
        }
    }
}

$fn=300;
scale([10, 10, 10]) backmost_hold(x=total_x, y=bp_total_y, z=bp_total_z);