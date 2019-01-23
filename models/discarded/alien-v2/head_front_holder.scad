module head_front_holder() {
    difference() {
        rotate([90, 0, 0]) scale([8.75, 4.25, 1]) linear_extrude(0.2) circle(r=1);
        translate([7, 0.5, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([7, 0.5, -2]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([1.7, 0.5, 3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([1.7, 0.5, -3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-7, 0.5, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-7, 0.5, -2]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-1.7, 0.5, 3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-1.7, 0.5, -3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([0, 0.1, 0]) rotate([90, 0, 0]) scale([7.75, 3.25, 1]) linear_extrude(0.7) circle(r=1);
    }
 }
 
$fn=300;
scale([10, 10, 10]) head_front_holder();