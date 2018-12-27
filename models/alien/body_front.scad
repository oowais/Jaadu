include <body.scad>

module body_front() {
    difference() {
        union() {
            basic_body(support=false); // basic body without support
            
            difference() {
                linear_extrude(height=1.75) circle(r=8.1); // the base of the body
                
                translate([-8.1, -1.1, -0.01]) cube([16.2, 9.2, 1.77]); // cut base of body as required
                
                translate([0, -1.1, 0.6]) linear_extrude(height=1.16) circle(r=8.1); // make base of body hollow
            }
            
            difference() {
                translate([-0.5, -2.2, 0]) cube([1, 1, 2]); // cube to attach base lock to
                
                translate([0, -1, 1.3]) rotate([90, 0, 0]) cylinder(r=0.25, h=1.1); // base lock attach point
            }
        }
        
        
        translate([2.5, -9, 0.6]) cube([8, 6.5, 1.15]); // Left cut for Critter leg
        
        translate([-10.5, -9, 0.6]) cube([8, 6.5, 1.15]); // Right cut for Critter leg
        
        translate([3.78, -3.78, -0.01]) linear_extrude(height=1, $fn=300) circle(r=0.4); // left leg bigger hole
        
        hull() {
            translate([3.78, -3.78, -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.4); // Left leg servo hold big
            
            translate([3.78, -2.28, -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.2); // Left leg servo hold small
        }
        
        translate([-3.78, -3.78, -0.1]) linear_extrude(height=1, $fn=300) circle(r=0.4); // right leg bigger hole
            
        hull() {
            translate([-3.78, -3.78, -0.1]) linear_extrude(height=0.31, $fn=300) circle(r=0.4); // Right leg servo hold big
            
            translate([-3.78, -2.28, -0.1]) linear_extrude(height=0.31, $fn=300) circle(r=0.2); // Right leg servo hold small
        }
            
        translate([0, 0, 14.8]) linear_extrude(0.2) circle(r=2.5); // Cut for neck hold
        
        for(i=[45: 45: 135]) {
            rotate([0, 0, -i]) translate([2.2, 0, 14]) scale([1, 12, 1]) cylinder(r=0.05, h=2); // Neck holders
        }
        
    }
}


$fn=300;
scale([10,10,10]) body_front();