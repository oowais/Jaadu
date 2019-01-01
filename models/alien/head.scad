module face() {
    s = 2.7;
    
    difference() {
        union () {
            for (i = [0: 1: 13]) {
                translate([0, i, 0]) rotate([90, 0, 0]) scale([8.75-(i/s), 4.25-(i/s), 1]) linear_extrude(1) circle(r=1);
            }
            
            hull() {
                union() {
                    for (i = [2: 1: 5]) {
                        translate([0, i, 0]) rotate([90, 0, 0]) scale([8.75-(i/s), 4.25-(i/s), 1]) linear_extrude(1) circle(r=1);
                    }
                }
                translate([0, 4, -5]) linear_extrude(1) circle(r=2);
            }
            
            translate([0, 4, -7]) cylinder(h=2, r=1.8);
        }
        
        hull () {
            translate([0, 0.9, 0]) rotate([90, 0, 0]) scale([7.75, 3, 1]) linear_extrude(1) circle(r=1);
            translate([0, 11, 0]) rotate([90, 0, 0]) scale([3.5, 0.01, 1]) linear_extrude(1) circle(r=1);
        }
        
        translate([0, 4, -6.4]) cylinder(h=7, r1=1.6, r2=1.39);
        
        translate([-2, 3, -6.4]) cube([4, 2, 1]);
        
        translate([-9, 0.1, 0]) cube([18, 12, 5]);
        
        translate([0, 4, -8]) cylinder(h=2, r=0.4);
        hull() {
            translate([0, 4, -6.8]) cylinder(h=1, r=0.4);
            translate([0, 2.5, -6.8]) cylinder(h=2, r=0.2);
        }
        
        translate([1.5, -1.1, -1.5]) cube([3.25, 2, 3.25]);
        translate([1.5, -0.1, -1.925]) cube([3.25, 0.3, 4.1]);
        translate([2.425, -0.6, -1.925]) cube([1.4, 0.8, 4.1]);
        translate([1.7, 1, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([4.5, 1, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([1.7, 1, -1.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([4.5, 1, -1.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        
        translate([-4.75, -1.1, -1.5]) cube([3.25, 2, 3.25]);
        translate([-4.75, -0.1, -1.925]) cube([3.25, 0.3, 4.1]);
        translate([-3.825, -0.6, -1.925]) cube([1.4, 0.8, 4.1]);
        translate([-1.7, 1, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-4.5, 1, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-1.7, 1, -1.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-4.5, 1, -1.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        
        translate([0, 14, 0]) rotate([90, 0, 0]) scale([3.5, 0.1, 1]) linear_extrude(3) circle(r=1);
        
        translate([7, 0, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([7, 0, -2]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([1.7, 0, 3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([1.7, 0, -3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-7, 0, 1.95]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-7, 0, -2]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-1.7, 0, 3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
        translate([-1.7, 0, -3.7]) rotate([90, 0, 0]) cylinder(r=0.1, h=5);
    }
}

$fn=300;
scale([10, 10, 10]) face();