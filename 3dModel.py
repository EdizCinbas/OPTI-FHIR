import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_box(ax, center, size, color):
    """
    Draw a 3D box given its center, size, and color.
    """
    l, w, h = size
    x, y, z = center
    corners = np.array([[x - l/2, y - w/2, z - h/2],
                        [x + l/2, y - w/2, z - h/2],
                        [x + l/2, y + w/2, z - h/2],
                        [x - l/2, y + w/2, z - h/2],
                        [x - l/2, y - w/2, z + h/2],
                        [x + l/2, y - w/2, z + h/2],
                        [x + l/2, y + w/2, z + h/2],
                        [x - l/2, y + w/2, z + h/2]])
    
    # Draw sides
    faces = [[corners[j] for j in [0,1,5,4]], [corners[j] for j in [1,2,6,5]], 
             [corners[j] for j in [2,3,7,6]], [corners[j] for j in [3,0,4,7]],
             [corners[j] for j in [4,5,6,7]], [corners[j] for j in [0,3,2,1]]]
    
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=0.5, edgecolors='black', alpha=0.5))

body_height = 170  # assume the height is 170cm
small_leg_length = 45  # assume the lower leg is 45cm
big_leg_kength = 45 # assume the upper leg is 45cm
chair_height = small_leg_length  
desk_height = chair_height + 22.5   
chair_seat_height = chair_height / 100  
desk_surface_height = desk_height / 100 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_stick_figure(ax, body_height_cm, small_leg_length_cm, big_leg_length_cm, chair_seat_height_m, desk_surface_height_m):
    """
    Draw a stick figure sitting on a chair in front of a desk with accurate representation of knees and legs.

    Parameters:
    ax: Matplotlib 3D axis object for drawing.
    body_height_cm: Total height of the stick figure in cm.
    small_leg_length_cm: Length of the lower leg (from knee to foot) in cm.
    big_leg_length_cm: Length of the upper leg (thigh, from hip to knee) in cm.
    chair_seat_height_m: Height of the chair seat from the ground in meters.
    desk_surface_height_m: Height of the desk surface from the ground in meters.
    """
    # Conversion from cm to meters for leg lengths
    small_leg_length_m = small_leg_length_cm / 100
    big_leg_length_m = big_leg_length_cm / 100

    # Calculate torso height (simplified to height above seat)
    torso_and_head_height_m = body_height_cm / 100 - (small_leg_length_m + big_leg_length_m)

    # Coordinates for the torso
    torso_bottom = [0, -0.5, chair_seat_height_m]
    torso_top = [0, -0.5, chair_seat_height_m + torso_and_head_height_m]

    # Coordinates for the head (simplified as a point above the torso)
    head = [0, -0.5, chair_seat_height_m + torso_and_head_height_m + 0.1]  # Small offset for the head

    # Draw the torso
    ax.plot([torso_bottom[0], torso_top[0]], [torso_bottom[1], torso_top[1]], [torso_bottom[2], torso_top[2]], color='black')
    
    # Draw the head
    ax.scatter(head[0], head[1], head[2], color='black', s=40)

    # Leg positions - starting from the bottom of the torso, bend at the knee, and down to the feet
    knee_height_m = chair_seat_height_m - 0.1  # Slightly above chair seat for visual representation
    feet_ground_level_m = 0  # Feet on ground

    # Lower legs (small_leg_length_m) - simple straight lines for visual
    knee_to_feet_x = 0.1  # Horizontal offset for feet position
    ax.plot([0, knee_to_feet_x], [-0.5, -0.5], [knee_height_m, feet_ground_level_m], color='black')  # Right leg
    ax.plot([0, -knee_to_feet_x], [-0.5, -0.5], [knee_height_m, feet_ground_level_m], color='black')  # Left leg

    # Upper legs (big_leg_length_m) - positioned on the chair
    ax.plot([0, 0], [-0.5, -0.5], [chair_seat_height_m, knee_height_m], color='black')  # Right thigh
    ax.plot([0, 0], [-0.5, -0.5], [chair_seat_height_m, knee_height_m], color='black')  # Left thigh

    # Arms (simplified representation, assuming resting on the desk or in lap)
    arm_end_y = -0.5  # Arms alongside the body or slightly extended towards the desk
    ax.plot([torso_top[0], 0.2], [torso_top[1], arm_end_y], [torso_top[2], desk_surface_height_m], color='black')  # Right arm towards desk
    ax.plot([torso_top[0], -0.2], [torso_top[1], arm_end_y], [torso_top[2], desk_surface_height_m], color='black')  # Left arm towards desk

# The remaining setup for drawing the desk and chair remains unchanged.
    

# set chair size
chair_seat_size = (0.45, 0.45, 0.02)  # chair seat length, width, height
chair_back_size = (0.45, 0.02, 0.4)  # chair back
desk_size = (1.2, 0.7, 0.02)  # 
leg_thickness = 0.05 


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# draw desk
desk_center = [0, 0, desk_surface_height + desk_size[2]/2]  # 桌面中心位置
draw_box(ax, desk_center, desk_size, 'saddlebrown')

# draw desk leg
for dx in [-1, 1]:
    for dy in [-1, 1]:
        leg_center = [dx * (desk_size[0]/2 - leg_thickness/2), dy * (desk_size[1]/2 - leg_thickness/2), desk_surface_height/2]
        draw_box(ax, leg_center, (leg_thickness, leg_thickness, desk_surface_height), 'saddlebrown')

chair_seat_center = [0, 0, chair_seat_height + chair_seat_size[2]/2]
chair_seat_center[1] -= (desk_size[1]/2 + chair_seat_size[1]/2 - 0.1)  

draw_box(ax, chair_seat_center, chair_seat_size, 'navy')

# draw chair leg
for dx in [-1, 1]:
    for dy in [-1, 1]:
        leg_center = [chair_seat_center[0] + dx * (chair_seat_size[0]/2 - leg_thickness/2),
                      chair_seat_center[1] + dy * (chair_seat_size[1]/2 - leg_thickness/2), 
                      chair_seat_height/2]
        draw_box(ax, leg_center, (leg_thickness, leg_thickness, chair_seat_height), 'navy')

# draw chair back
chair_back_center = [chair_seat_center[0], chair_seat_center[1] - chair_seat_size[1]/2 + chair_back_size[1]/2, 
                     chair_seat_height + chair_back_size[2]/2]
draw_box(ax, chair_back_center, chair_back_size, 'navy')
draw_stick_figure(ax, body_height, small_leg_length, big_leg_kength, chair_seat_height, desk_surface_height)

# 设置图形的显示范围和标签
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


ax.view_init(elev=0, azim=90)  # Adjust azim for the desired side view

# Continue with any final setup before showing the plot
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])  # Adjusted for better visualization of the vertical scale
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
ax.view_init(elev=0, azim=0)  # Adjust azim for the desired side view

# Continue with any final setup before showing the plot
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])  # Adjusted for better visualization of the vertical scale
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig.savefig('skeleton.jpg')