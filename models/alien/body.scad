module basic_body(support=true) {
    
    difference() {
        scale([8, 8, 16]) sphere(r=1); // The total body
        
        translate([-8, -8, -16]) cube([16, 16, 16]); // Cut the body into half from bottom
        
        translate([0, 0, -0.1]) cylinder(h=18, r=2); // Make cut for the head
        
        translate([-8, 0, -0.1]) cube([16, 8, 16]); // Cut the body into half from side
        
        translate([0, 0, -1]) scale([8, 8, 16]) sphere(r=1); // Cut the body shell to make hollow from inside
        
        translate([0, 0, 8]) rotate([90, 0, 0]) cylinder(r=4.5, h=20); // Cut for the arc reactor
    }

    difference() {
        
        union() {
            translate([0, 0, 8]) rotate([90, 0, 0]) cylinder(r=5, h=10); // Outer part of the arc reactor
            
            if (true == support) { 
                rotate([45, 60, 0]) translate([0, 0, 1.3]) cylinder(r=0.3, h=6.8); // right side support for body with base
                
                rotate([45, 60, -83]) translate([0, 0, 1.3])cylinder(r=0.3, h=6.8); // left side support for body with base
            }
            
            cylinder(r=2, h=1); // the cylinder at base
        }
       
        translate([-2.5, 0, -0.1]) cube([5, 5, 2]); // cut cylinder at base in half
        
        translate([0, 0.1, 8]) rotate([90, 0, 0]) cylinder(r=4.5, h=11); // make arc reactor hollow
           
        difference() {
            translate([-8, -11, 0]) cube([16, 11, 16]); // Outer cube having whole body
            
            scale([8.5, 8.5, 16.5]) sphere(r=1); // cut the outer cube to get perfect cut for cylindrical arc reactor
        }
        
        for (i = [-0.5 : -1.5 : -4]) {
            for (j = [0: 36: 360]) {
                translate([0, i, 8])  rotate([0, j + (i * 10) , 0]) scale([3, 1, 1]) cylinder(r=0.21, h=5.1); // the wire openings
            }
        }
        
        translate([0, -0.7, -0.1]) cylinder(r=0.3, h=1.2); // Hole at base for lock
        
        translate([-0.3, -0.7, -0.1]) cube([0.6, 0.71, 0.31]); // lock cut at base
    }
}


$fn=300;
basic_body();