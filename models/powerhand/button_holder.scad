module button_holder_1() {
    difference() {
        cube([0.5, 0.5, 1.2]);
        translate([-0.01, -0.01, -0.01]) cube([0.2, 0.7, 3]);
        translate([0.3, -0.01, 0.3]) rotate([-90, 0, 0]) cylinder(d=0.1, h=0.7);
        translate([0.3, -0.01, 0.8]) rotate([-90, 0, 0]) cylinder(d=0.1, h=0.7);
    }
}

module button_holder_2() {
    difference() {
        cube([0.5, 4.6, 1.2]);
        translate([0.1, 1, 0.2]) cube([0.41, 5, 0.7]);
        translate([-0.01, -0.01, -0.01]) cube([0.52, 2.21, 1.22]);
    }
}

module button_holder() {
    button_holder_1();
    button_holder_2();
}

$fn=300;
//scale([10, 10, 10]) button_holder_1();
//scale([10, 10, 10]) button_holder_2();