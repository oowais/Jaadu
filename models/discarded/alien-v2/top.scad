include <globals.scad>

module top(x=10, y=10.5, z=0.2, hole=true, screws=true) {
    difference() {
        cube([x, y, z]);
        if (hole == true) { 
            translate([x/2, y/2, -0.01]) cylinder(r=1, h=1);
        }
        if (screws == true) {
            for (i = [2.5: 2.5: x-2.5]) {
                translate([i, 0.6, -z]) cylinder(r=screw_r, h=1);
                translate([i, y-0.4, -z]) cylinder(r=screw_r, h=1);
            }
        }
    }
}

module circ_cut(r, t=plexi_thickness) {
    sphere(r=r);
    for (j = [0: 10: 180]) {
        for (i = [0: 36: 360]) {
            rotate([0, 0, i+j]) translate([-((2*r*sin(j))+1)/2, -0.5, r*cos(j)]) cube([(2*r*sin(j))+1, (r/2.5)*sin(j), t]);
        }
    }
}

module top_pieces(y, z=plexi_thickness) {
    cube([total_x, y, z]);
}

module all_plate_stack(num=0) {    
    total_height = 5.1;
    if (num > 0) {
        difference() {
            if (num <= 12) {
                i = (num == 1) ? plexi_thickness : plexi_thickness + ((num - 1) * (plexi_thickness + filler));
                translate([0, 0, i]) top_pieces(y=i/sin(lower_elevation_deg-1.5));
            }
            else if ( num > 12) {
                i = (num == 13) ? plexi_thickness : plexi_thickness + ((num - 13) * (plexi_thickness + filler));
                translate([0, 0, (total_height)-i]) top_pieces(y=i/sin(elevation_deg+2.1));
            }
            translate([total_x/2, total_y/2, (total_height/2)]) circ_cut(r=4, t=0.5);
        }
    } else {
        difference() {
            union() {
                for (i = [plexi_thickness: plexi_thickness + filler: (total_height/2)]) {
                    translate([0, 0, i]) top_pieces(y=i/sin(lower_elevation_deg-1.5));
                }
                for (i = [plexi_thickness: (plexi_thickness + filler): (total_height/2)]) {
                    translate([0, 0, (total_height)-i]) top_pieces(y=i/sin(elevation_deg+2.1));
                }
            }
            translate([total_x/2, total_y/2, (total_height/2)]) circ_cut(r=4, t=0.5);
        }
    }
}

$fn=300;
// For the bottom-most top part
//scale([10, 10, 10]) top(x=total_x, y=top_total_y, z=plexi_thickness);
// For the topmost top part
//scale([10, 10, 10]) top(x=total_x, y=top_total_y, z=plexi_thickness, hole=false, screws=false);
// Total plate stack
//scale([10, 10, 10]) all_plate_stack(num=0); // num = 0
// Plate Stacks (num = 1 to 24)
//scale([10, 10, 10]) all_plate_stack(num=1); // num = 1
//scale([10, 10, 10]) all_plate_stack(num=2); // num = 2
//scale([10, 10, 10]) all_plate_stack(num=3); // num = 3
//scale([10, 10, 10]) all_plate_stack(num=4); // num = 4
//scale([10, 10, 10]) all_plate_stack(num=5); // num = 5
//scale([10, 10, 10]) all_plate_stack(num=6); // num = 6
//scale([10, 10, 10]) all_plate_stack(num=7); // num = 7
//scale([10, 10, 10]) all_plate_stack(num=8); // num = 8
//scale([10, 10, 10]) all_plate_stack(num=9); // num = 9
//scale([10, 10, 10]) all_plate_stack(num=10); // num = 10
//scale([10, 10, 10]) all_plate_stack(num=11); // num = 11
//scale([10, 10, 10]) all_plate_stack(num=12); // num = 12
//scale([10, 10, 10]) all_plate_stack(num=13); // num = 13
//scale([10, 10, 10]) all_plate_stack(num=14); // num = 14
//scale([10, 10, 10]) all_plate_stack(num=15); // num = 15
//scale([10, 10, 10]) all_plate_stack(num=16); // num = 16
//scale([10, 10, 10]) all_plate_stack(num=17); // num = 17
//scale([10, 10, 10]) all_plate_stack(num=18); // num = 18
//scale([10, 10, 10]) all_plate_stack(num=19); // num = 19
//scale([10, 10, 10]) all_plate_stack(num=20); // num = 20
//scale([10, 10, 10]) all_plate_stack(num=21); // num = 21
//scale([10, 10, 10]) all_plate_stack(num=22); // num = 22
//scale([10, 10, 10]) all_plate_stack(num=23); // num = 23
//scale([10, 10, 10]) all_plate_stack(num=24); // num = 24