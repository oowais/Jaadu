module down_holder_2() {
    cylinder(r=0.20, h=3.85); // Lock pin
}

$fn=300;
scale([10, 10, 10]) down_holder_2();