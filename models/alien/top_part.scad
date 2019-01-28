module our_pattern() {
    translate([6.4, 5.13, 0]) scale([0.03, 0.03, 0.02]) import("stl/simple.stl");
}

module face() {
    difference() {
        cube([20, 5.89, 0.2]);
        translate([5 + (10/2) - 3.21 - 0.5, (5.89/2) - (3.21/2), -0.1]) cube([3.21, 3.21, 1.2]);
        translate([5 + (10/2) + 0.5, (5.89/2) - (3.21/2), -0.1]) cube([3.21, 3.21, 1.2]);
        translate([0, -8.3, -0.1]) rotate([0, 0, 45]) cube([10, 10, 0.4]);
        translate([20, -8.3, -0.1]) rotate([0, 0, 45]) cube([10, 10, 0.4]);
        difference() {
            for(i=[0.3: 0.8: 6]) {
                translate([-0.1, i, -0.1]) cube([20.2, 0.2, 0.4]);
            }
            translate([5, 0, -0.1]) cube([10, 6, 0.4]);
        }
    }
}

module head() {
    union() {
        difference() {
            cube([20, 20, 0.2]);
            rotate([0, 0, 56.14]) translate([0, 0, -0.1]) cube([20, 20, 0.4]);
            translate([0, 15, -0.1]) cube([20, 10, 0.4]);
            translate([20, 0, -0.1]) rotate([0, 0, 90-56.14])  cube([20, 20, 0.4]);
            translate([1, 0.75, -0.1]) scale([0.9, 0.9, 2]) difference() {
                cube([20, 20, 0.2]);
                rotate([0, 0, 56.14]) translate([0, 0, -0.1]) cube([20, 20, 0.4]);
                translate([0, 15, -0.1]) cube([20, 10, 0.4]);
                translate([20, 0, -0.1]) rotate([0, 0, 90-56.14])  cube([20, 20, 0.4]);
            }
        }
        difference() {
            union() {
                translate([1, 0.7, 0]) our_pattern();
                translate([14, 0.7, 0]) our_pattern();
            }
            rotate([0, 0, 56.14]) translate([0, 0, -0.1]) cube([20, 20, 1]);
            translate([20, 0, -0.1]) rotate([0, 0, 90-56.14])  cube([20, 20, 1]);
            translate([20, 0, -0.1]) cube([10, 15, 1]);
        }
    }
}

$fn=300;
//scale([10, 10, 10]) face();
//scale([10, 10, 10]) head();
//our_pattern();