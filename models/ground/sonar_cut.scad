module sonar_cut() {
    linear_extrude(0.2) 
        difference() {
            hull() {
                circle(d=1.65+0.7);
                translate([4, 0, 0]) circle(d=0.01);
            }
            circle(d=1.65);
        }
}

$fn=300;
scale([10, 10, 10]) sonar_cut();