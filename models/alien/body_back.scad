include <body.scad>

$fn=100;

difference() {
    union() {
        mirror([0, 1, 0]) basic_body(support=false);
        translate([0, 0, 14.85]) linear_extrude(0.1) circle(r=2.4);
        translate([0.9, -0.8, 13.2]) rotate([0, -90, 0]) cube([1.8, 2.7, 1.7]); // servo holding case
  
        difference() {
            linear_extrude(height=1.75) circle(r=8.1);
            translate([-8.1, -8.1, -0.01]) cube([16.2, 9.2, 1.77]);
            translate([3.3, 1.7, 0.3]) cube([3, 3, 3]);
            translate([-6.3, 1.7, 0.3]) cube([3, 3, 3]);
            translate([-3, 4.7, 0.3]) cube([6, 2.55, 2]);
        }
    }
    
    translate([-3, 1.5, -0.01]) cube([6, 3, 1.7]);
    
    translate([0, 1.7, 1.3]) rotate([90, 0, 0]) cylinder(r=0.25, h=1.1);
    
    translate([0.9, -0.8, 13.2]) rotate([0, -90, 0]) translate([0.2, 0.2, 0.2]) cube([1.61, 2.3, 1.3]); // servo holding
    translate([0.9, -0.8, 13.2]) rotate([0, -90, 0]) translate([0.2, -0.1, 0.5]) cube([1.35, 0.31, 0.6]); // bringing out the servo wire
    
    for(i=[45: 45: 135]) {
        rotate([0, 0, -i]) translate([2.2, 0, 14]) scale([1, 12, 1]) cylinder(r=0.05, h=2);
    }
    
    translate([1.4, 0.6, 14]) cylinder(r=0.4, h=1);
    
    translate([-1.4, 0.6, 14]) cylinder(r=0.4, h=1);
}