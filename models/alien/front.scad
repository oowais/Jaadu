include <globals.scad>
use <top.scad>

module eyes_setting(x, z) {
    y = 1;
    difference() {
        cube([x, 1, z]);
        translate([-0.1, 0, z]) rotate([-elevation_deg, 0, 0]) top(x=x+0.2, z=10);
        
        for (i = [2.5: 2.5: x-2.5]) {
            translate([i, 0.3, z-1]) rotate([-elevation_deg, 0, 0]) cylinder(r=screw_r, h=2);
        }
        
        translate([(x/2) - 3.21 - 0.5, -0.1, (z/2) - (3.21/2)]) cube([3.21, 1.2, 3.21]);
        translate([(x/2) - 3.21 - 0.5, 0.8, (z/2) - (4.1/2)]) cube([3.21, 0.3, 4.1]);
        translate([(x/2) - 3.21 - 0.5 + 0.2, y + 0.1, (z/2) - (4.1/2) + 3.85]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) - 3.21 - 0.5 + 0.2, y + 0.1, (z/2) - (4.1/2) + 0.25]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) - 3.21 - 0.5 + 0.2 + 2.8, y + 0.1, (z/2) - (4.1/2) + 3.85]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) - 3.21 - 0.5 + 0.2 + 2.8, y + 0.1, (z/2) - (4.1/2) + 0.25]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) - 3.21 - 0.5 + (3.21/2) - (1.4/2), y - 0.5, (z/2) - (4.1/2)]) cube([1.4, 0.51, 4.1]);
        
        translate([(x/2) + 0.5, -0.1, (z/2) - (3.21/2)]) cube([3.21, 1.2, 3.21]);
        translate([(x/2) + 0.5, 0.8, (z/2) - (4.1/2)]) cube([3.21, 0.3, 4.1]);
        translate([(x/2) + 0.5 + 0.2, y + 0.1, (z/2) - (4.1/2) + 3.85]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) + 0.5 + 0.2, y + 0.1, (z/2) - (4.1/2) + 0.25]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) + 0.5 + 0.2 + 2.8, y + 0.1, (z/2) - (4.1/2) + 3.85]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) + 0.5 + 0.2 + 2.8, y + 0.1, (z/2) - (4.1/2) + 0.25]) rotate([90, 0, 0]) cylinder(r=screw_r, h=5);
        translate([(x/2) + 0.5 + (3.21/2) - (1.4/2), y - 0.5, (z/2) - (4.1/2)]) cube([1.4, 0.51, 4.1]);
    }
}

module front(x, y, z) {
    difference() {
        cube([x, y, 0.1]);
        translate([x/2, base_head_fit_1, -0.1]) cylinder(r=screw_r, h=1);
        translate([x/2, base_head_fit_2, -0.1]) cylinder(r=screw_r, h=1);
    }
    eyes_setting(x=x, z=z);
}

$fn=300;
scale([10, 10, 10]) front(x=total_x, y=face_total_y, z=face_total_z);