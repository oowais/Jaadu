include <globals.scad>
use <top.scad>

module backmost_hold(x, y, z) {
    difference() {
        cube([x, y, z]);
        translate([-0.01, 0, z]) rotate([-lower_elevation_deg, 0, 0]) top(x=x+0.2, z=3);
        for (i = [2.5: 2.5: x-2.5]) {
            translate([i, 0.3, z-1]) rotate([-lower_elevation_deg, 0, 0]) cylinder(r=screw_r, h=1);
        }
    }
}

module backmost_glass(front_z, back_z) {
  // Have to make about 24 pieces of it to fill up backmost_hold 
  hull() {
      cube([0.2, 0.1, back_z]);
      translate([0, 0.8, 0]) cube([0.2, 0.1, front_z]);
  }  
}

$fn=300;
scale([10, 10, 10]) backmost_hold(x=total_x, y=bp_total_y, z=bp_total_z);
//scale([10, 10, 10]) rotate([0, 90, 0]) backmost_glass(front_z=6.5, back_z=6.7);


