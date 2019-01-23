module bar() {
    difference() {
        cube([13, 1.75, 0.2]);
        linear_extrude(0.2) difference() {
            circle(r=14);
            circle(r=13);
        }
    }
}

module circles() {
    difference() {
        linear_extrude(0.2) difference() {
                circle(r=13);
                scale([1.6, 1, 1]) circle(r=7);
                translate([-7, 7.2, 0]) circle(r=3);
                translate([-4, 8, 0]) circle(r=2);
                translate([-1.5, 7, 0]) circle(r=2);
            }
        rotate([0, 0, 45]) translate([-13, -13, -0.1]) cube([13, 26, 1]);
        translate([0, -14, -0.1]) cube([14, 14, 1]); 
    }
}

module led_cuts() {
    translate([0, 0, -0.1]) difference() {
        linear_extrude(0.4) union() {
            difference() {
                circle(r=12);
                circle(r=11.7);
            }
            difference() {
                circle(r=10);
                circle(r=9.7);
            }
            translate([1, 10.8, 0]) difference() {
                circle(r=1.1);
                circle(r=0.8);
                translate([0, -1, 0]) square(2);
            }
        }
        cube([10, 5.6, 0.4]);
        translate([3, 5, 0]) rotate([0, 0, 130]) cube([12, 5, 0.4]);
    }
}

module complete_extension(cuts=false) {
    difference() {
        union() {
            bar();
            circles();
        }
        if (cuts == true)
            led_cuts();
    }
}

$fn=300;
scale([10, 10, 10]) complete_extension(cuts=true);