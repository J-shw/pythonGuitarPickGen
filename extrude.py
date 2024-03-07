import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def extrude_stl(input_file, output_file, distance, direction=(0, 0, 1)):
    # Load the STL file
    mesh_data = mesh.Mesh.from_file(input_file)

    # Extrude the vertices
    vertices = np.concatenate([mesh_data.vectors, mesh_data.vectors + np.array(direction) * distance])

    # Create the new mesh
    extruded_mesh = mesh.Mesh(vertices.reshape(-1, 3), remove_empty_areas=False)

    # Write the new mesh to an STL file
    extruded_mesh.save(output_file)

    return extruded_mesh

def plot_stl(mesh_data):
    # Create a new figure
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)

    # Add the mesh to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh_data.vectors))

    # Set plot parameters
    scale = mesh_data.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    input_file = "plane.stl"
    output_file = "output.stl"
    extruded_distance = 10  # Adjust as needed
    extrude_direction = (0, 0, 1)  # Adjust as needed

    # Extrude the STL file
    extruded_mesh = extrude_stl(input_file, output_file, extruded_distance, extrude_direction)

    # Plot the original and extruded mesh
    plot_stl(mesh_data=extruded_mesh)
