module connector() {
    cube([1, 5.5, 0.5]);
    translate([0, 5.5, 0]) difference() {
        linear_extrude(height=0.5) circle(r=1);
        translate([-1.1, 0, -0.1]) cube([2.2, 1.1, 1.2]);
    }
    
    difference() {
        sphere(r=5.5);
        sphere(r=5.2);
        translate([-1.1, 0, -0.1]) cube([2.2, 1.1, 1.2]);
        translate([-5.5, -5.5, -5.5]) cube([11, 5.6, 11]);
        translate([-5.5, -1, -10.7]) cube([11, 11, 11]);
        rotate([0, 45, 0]) translate([0, -1, 0]) cube([11, 11, 11]);
        rotate([0, 180+45, 0]) translate([0, -1, 0]) cube([11, 11, 11]);
    }
}

$fn=300;
scale([10, 10, 10]) connector();