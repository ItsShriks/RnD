point_counts = {
    "filtered_point_cloud.ply": 725669,
    "Stump.ply": 86655,
    "Separated.ply": 74814
}

total_points = sum(point_counts.values())

print(f"Total points: {total_points}\n")

for file, count in point_counts.items():
    percentage = (count / total_points) * 100
    print(f"{file}: {count} points → {percentage:.2f}% of total")
