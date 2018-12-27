module basic_body(support=true) {
    difference() {
        scale([8, 8, 16]) sphere(r=1); 
        translate([-8, -8, -16]) cube([16, 16, 16]);
        translate([0, 0, -0.1]) cylinder(h=18, r=2);
        translate([-8, 0, -0.1]) cube([16, 8, 16]);
        translate([0, 0, -1]) scale([8, 8, 16]) sphere(r=1);
        translate([0, 0, 8]) rotate([90, 0, 0]) cylinder(r=4.5, h=20);
    }

    difference() {
      
        union() {
            translate([0, 0, 8]) rotate([90, 0, 0]) cylinder(r=5, h=10);
            if (true == support) { 
                rotate([45, 60, 0]) translate([0, 0, 1.3]) cylinder(r=0.3, h=6.8);
                rotate([45, 60, -83]) translate([0, 0, 1.3])cylinder(r=0.3, h=6.8);
            }
            cylinder(r=2, h=1);
        }
       
        translate([-2.5, 0, -0.1]) cube([5, 5, 2]);
        
        translate([0, 0.1, 8]) rotate([90, 0, 0]) cylinder(r=4.5, h=11);
           
        difference() {
            translate([-8, -11, 0]) cube([16, 11, 16]);
            scale([8.5, 8.5, 16.5]) sphere(r=1);
        }
        
        for (i = [-0.5 : -1.5 : -4]) {
            for (j = [0: 36: 360]) {
                translate([0, i, 8])  rotate([0, j + (i * 10) , 0]) scale([3, 1, 1]) cylinder(r=0.21, h=5.1);
            }
        }
        
        translate([0, -0.7, -0.1]) cylinder(r=0.3, h=1.2);
        
        translate([-0.3, -0.7, -0.1]) cube([0.6, 0.71, 0.31]);
    }
}

/*
$fn=100;
basic_body();
*/