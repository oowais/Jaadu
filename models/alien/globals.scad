// General
total_x = 10;
total_y = 10;
total_z = 10;
filler = 0.01;
screw_r = 0.1;
screw_h = 2;
elevation_deg = 12.5;
lower_elevation_deg = 18.5;
plexi_thickness = 0.2;

// For legs
l_arms_base_d = 3.5;

// For Base
b_overall_z = 0.1;
b_legfit_z = 0.6;
b_legspace = 3.5 + 0.5;
b_armspace_z = 3.5;
base_head_fit_1 = 2;
base_head_fit_2 = 3;
base_total_z = b_armspace_z + b_legfit_z;

// For Top
top_total_y = (total_y * cos(elevation_deg)) + 0.74;

// For Face
face_total_y = b_legspace;
face_total_z = total_z - (base_total_z + filler);

// For Battery Holder
bh_y = 5;
bh_z = 2.9;

// For RasPI Holder
raspi_total_y = 4;
raspi_total_z = 1;

// For backmost part
bp_total_y = total_y - (b_legspace + filler + bh_y + filler);
bp_total_z = 7;