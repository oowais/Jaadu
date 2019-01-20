use <middle_part.scad>
use <sonar_cut.scad>

module talk_point() {
    rotate([90, 0, 0]) middle_part();
    
    translate([0, 1.175, 1.175]) {
        rotate([90, 15, 90]) sonar_cut();
        translate([0.2, 0, 0]) rotate([90, -15, 90]) sonar_cut();
        translate([0.4, 0, 0]) rotate([90, -45, 90]) sonar_cut();
        translate([0.6, 0, 0]) rotate([90, -75, 90]) sonar_cut();
        translate([0.8, 0, 0]) rotate([90, -105, 90]) sonar_cut();
    }
    
    translate([0, -1.175-0.2, 1.175]) {
        rotate([-90, 15, -90]) sonar_cut();
        translate([0.2, 0, 0]) rotate([-90, -15, -90]) sonar_cut();
        translate([0.4, 0, 0]) rotate([-90, -45, -90]) sonar_cut();
        translate([0.6, 0, 0]) rotate([-90, -75, -90]) sonar_cut();
        translate([0.8, 0, 0]) rotate([-90, -105, -90]) sonar_cut();
    }
}

$fn=300;
talk_point();