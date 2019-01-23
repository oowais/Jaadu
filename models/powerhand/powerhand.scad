use <battery_holder.scad>
use <extension_holder.scad>
use <extension.scad>
use <button_holder.scad>

module powerhand() {
    translate([0, 0, 1-0.6]) button_holder();
    translate([0.5, 0, 0]) holder_for_battery();
    translate([2.8, 0, 0]) holder_for_extension();
    translate([3.4, 0.2, 0.1]) rotate([90, 0, 90]) 
        for(i=[0: 0.2: 1]) {
            translate([i+0.01, 0, 0]) complete_extension(cuts=true);
        }
}

$fn=300;
powerhand();