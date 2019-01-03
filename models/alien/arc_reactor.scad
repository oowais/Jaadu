module single_pattern() {
    difference() {
        scale([2.6, 4.2, 0.1]) cylinder(h=1, r=1);
        translate([0, 0, -0.1]) scale([2.4, 4, 0.3]) cylinder(h=1, r=1);
    }
}

module pattern() {
    for (i= [1: 1: 10]) {
        rotate([0, 0, 36 * i]) single_pattern();
    }
    scale([0.2, 0.6, 1]) single_pattern();
    rotate([0, 0, 90]) scale([0.2, 0.6, 1]) single_pattern();
    translate([-0.5, -0.5, 0]) cube([1, 1, 0.1]);
}

module arc_reactor() {
    difference() {
        union() {
            pattern();
            rotate([5, 0, 0]) cylinder(h=5, r=0.3);
        }
        rotate([5, 0, 0]) translate([0, 0, -0.1]) cylinder(r=0.2, h=7);
        translate([0, 5, 0.7]) rotate([90, 0, 0]) cylinder(d=0.2, h=10);
        translate([-5, 0, 1.1]) rotate([0, 90, 0]) cylinder(d=0.2, h=10);
    }
}

$fn=300;
scale([10, 10, 10]) arc_reactor();