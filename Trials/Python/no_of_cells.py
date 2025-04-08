import math

width = 68  # meters
height = 80  # meters
grid_size = 2.0  # meter (you can change this)

x_cells = math.ceil(width / grid_size)
y_cells = math.ceil(height / grid_size)
total_cells = x_cells * y_cells

print(f"Grid size: {grid_size}m")
print(f"Grid cells: {x_cells} (X-axis) × {y_cells} (Y-axis)")
print(f"Total grid cells: {total_cells}")
