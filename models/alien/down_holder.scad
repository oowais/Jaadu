$fn=100;

difference() {
    union() {
        translate([-0.25, 0, 0]) cube([0.5, 1.4, 0.4]);
        cylinder(r=0.25, h=2);
        translate([0, 1.4, 0]) cylinder(r=0.25, h=2);
    } 
    translate([0, 2.45, 1.3]) rotate([90, 0, 0]) cylinder(r=0.21, h=3.85);
}