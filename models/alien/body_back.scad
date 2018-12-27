include <body.scad>

module body_back() {
    difference() {
        union() {
            mirror([0, 1, 0]) basic_body(support=false); // the main body without the support
            
            translate([0, 0, 14.85]) linear_extrude(0.1) circle(r=2.4); // the head lock portion
            
            translate([0.9, -0.8, 13.2]) rotate([0, -90, 0]) cube([1.8, 2.7, 1.7]); // servo holding case
      
            difference() {
                linear_extrude(height=1.75) circle(r=8.1); // the base of the body
                
                translate([-8.1, -8.1, -0.01]) cube([16.2, 9.2, 1.77]); // remove back portion of the base
                
                translate([1.3, 1.7, 0.3]) cube([5, 3, 2]); // right side holding 
                
                translate([-6.3, 1.7, 0.3]) cube([5, 3, 2]); // left side holding
                
                translate([1.3, 4.1, 0.3]) cube([2, 3, 2]); // right side back holding
                
                translate([-3.3, 4.1, 0.3]) cube([2, 3, 2]); // left side back holding
            }
        }
        
        translate([-0.75, 1.5, -0.01]) cube([1.5, 5, 1.7]); // holding pin insert area
        
        translate([0, 1.7, 1.3]) rotate([90, 0, 0]) cylinder(r=0.25, h=1.1); // holding pin insert area 
        
        translate([0.9, -0.8, 13.2]) rotate([0, -90, 0]) translate([0.2, 0.2, 0.2]) cube([1.61, 2.3, 1.3]); // servo holding
        
        translate([0.9, -0.8, 13.2]) rotate([0, -90, 0]) translate([0.2, -0.1, 0.5]) cube([1.35, 0.31, 0.6]); // bringing out the servo wire
        
        for(i=[45: 45: 135]) {
            rotate([0, 0, -i]) translate([2.2, 0, 14]) scale([1, 12, 1]) cylinder(r=0.05, h=2); // Upper neck holding
        }
        
        translate([1.4, 0.6, 14]) cylinder(r=0.4, h=1); // Bring out wires for head
        
        translate([-1.4, 0.6, 14]) cylinder(r=0.4, h=1); // Bring out wires for head
    }
}

$fn=300;
scale([10, 10, 10]) body_back();