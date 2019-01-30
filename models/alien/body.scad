include <globals.scad>
use <rasp_case.scad>
use <front.scad>
use <base.scad>
use <backmost_hold.scad>
use <arm_right.scad>
use <arm_left.scad>
use <leg_right.scad>
use <leg_left.scad>

module total_body(x, y, z) {
    base(x=x, y=y, z=base_total_z);
    translate([0, 0, base_total_z + filler]) {
        front(x=x, y=face_total_y, z=face_total_z);
    }
    
    translate([0, b_legspace + filler + (bh_y - raspi_total_y), b_overall_z + filler]) {
        raspi_case(x=x, y=raspi_total_y, z=raspi_total_z);
    }
    
    translate([0, b_legspace + filler + bh_y + filler, b_overall_z + filler]) {
        backmost_hold(x=total_x, y=bp_total_y, z=bp_total_z);
    }
    
    translate([9.15, -4.3, b_legfit_z + filler]) arm_left();
    translate([0.85, -4.3, b_legfit_z + filler]) arm_right();
    translate([10, -4, -3.2]) rotate([9, 0, 0]) leg_left();
    translate([0, -4, -3.2]) rotate([9, 0, 0]) leg_right();
}

$fn=300;
translate([-5, 0, 2.2]) rotate([-elevation_deg, 0, 0]) total_body(x=total_x, y=total_y, z=total_z);