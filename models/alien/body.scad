include <globals.scad>
use <rasp_case.scad>
use <battery_holder.scad>
use <front.scad>
use <base.scad>
use <backmost_hold.scad>
use <top.scad>
use <arm_right.scad>
use <arm_left.scad>
use <leg_right.scad>
use <leg_left.scad>

module total_body(x, y, z) {
    base(x=x, y=y, z=base_total_z);
    translate([0, 0, base_total_z + filler]) {
        front(x=x, y=face_total_y, z=face_total_z);
    }
    
    translate([0, b_legspace + filler, b_overall_z + filler]) {
        battery_holder(x=x, y=bh_y, z=bh_z);
    }
    
    translate([0, b_legspace + filler + (bh_y - raspi_total_y), b_overall_z + filler + bh_z + filler]) {
        raspi_case(x=x, y=raspi_total_y, z=raspi_total_z);
    }
    
    translate([0, b_legspace + filler + bh_y + filler, b_overall_z + filler]) {
        backmost_hold(x=total_x, y=bp_total_y, z=bp_total_z);
    }
    
    // temp
    translate([9.15, -4.3, b_legfit_z + filler]) arm_left();
    translate([0.85, -4.3, b_legfit_z + filler]) arm_right();
    translate([10, -4, -3.2]) rotate([9, 0, 0]) leg_left();
    translate([0, -4, -3.2]) rotate([9, 0, 0]) leg_right();
    // temp
    
    /* Plexi-materials */
    //translate([0, 0, z]) rotate([elevation_deg, 0, 0]) top(x=total_x, y=top_total_y, z=plexi_thickness, hole=false, screws=false);
    //translate([0, 0, z + filler]) rotate([-lower_elevation_deg, 0, 0]) top(x=total_x, y=top_total_y, z=plexi_thickness);
    //translate([total_x, total_y, bp_total_z]) rotate([0, 0, 180]) all_plate_stack();
}

$fn=300;
translate([-5, 0, 2.2]) rotate([-elevation_deg, 0, 0]) total_body(x=total_x, y=total_y, z=total_z);