module head_back_holder() {
        rotate([90, 0, 0]) scale([3.4, 0.07, 1]) linear_extrude(2) circle(r=1);
        translate([0, 0.5, 0]) rotate([90, 0, 0]) scale([3.7, 0.2, 1]) linear_extrude(0.5) circle(r=1);
 }
 
$fn=300;
scale([10, 10, 10]) head_back_holder(); 