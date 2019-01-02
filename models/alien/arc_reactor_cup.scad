module cup() {
    difference() {
        cylinder(r=4.7, h=1.5);
        translate([0, 0, 0.2]) cylinder(r=4.49, h=2);
        translate([0, 5, 1]) rotate([90, 0, 0]) cylinder(d=0.2, h=10);
        translate([-5, 0, 1.4]) rotate([0, 90, 0]) cylinder(d=0.2, h=10);
    }
}

module cup_left() {
    difference() {
        cup();
        rotate([0, 0, 45]) translate([-5, 0, -0.1]) cube([10, 10, 3]);
    }
}

module cup_right() {
    difference() {
        cup();
        rotate([0, 0, 225]) translate([-5, 0, -0.1]) cube([10, 10, 3]);
    }
}
$fn=300;
scale([10, 10, 10]) translate([0.5, -0.5, 0]) cup_left();
scale([10, 10, 10]) translate([-0.5, 0.5, 0]) cup_right();