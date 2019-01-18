module holder_for_bluetooth() {
    difference() {
        cube([1.1, 4.5+0.1, 1.8+0.2]);
        translate([-0.1, 0.1, 0.1]) cube([1.1, 4.5+0.1, 1.8]);
    }
}

$fn=300;
scale([10, 10, 10]) holder_for_bluetooth();