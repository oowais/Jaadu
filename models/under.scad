scale([10, 10, 10]) {
    difference() {
        cube([8.5, 8.5, 0.6]); // the actual base
        
        translate([1.75, 6.75, -0.01]) linear_extrude(height=1, $fn=300) circle(r=0.4); // left leg bigger hole
        
        hull() {
            translate([1.75, 6.75, -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.4);
            translate([1.75, 5.25, -0.01]) linear_extrude(height=0.31, $fn=300) circle(r=0.2);
        }
        
        translate([1.75, 5.3, -0.01]) linear_extrude(height=1, $fn=300) circle(d=0.1);
        
        translate([6.75, 6.75, -0.1]) linear_extrude(height=1, $fn=300) circle(r=0.4); // right leg bigger hole
        
        hull() {
            translate([6.75, 6.75, -0.1]) linear_extrude(height=0.31, $fn=300) circle(r=0.4);
            translate([6.75, 5.25, -0.1]) linear_extrude(height=0.31, $fn=300) circle(r=0.2);
        }
        
         translate([6.75, 5.3, -0.01]) linear_extrude(height=1, $fn=300) circle(d=0.1);
    }
}