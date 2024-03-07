def generate_cube_stl(side_length, filename):
    header = ("solid cube\n")
    footer = ("endsolid cube\n")
    
    vertices = [
        (0, 0, 0),
        (side_length, 0, 0),
        (side_length, side_length, 0),
        (0, side_length, 0),
        (0, 0, side_length),
        (side_length, 0, side_length),
        (side_length, side_length, side_length),
        (0, side_length, side_length)
    ]
    
    faces = [
        (0, 1, 2),
        (0, 2, 3),
        (4, 5, 6),
        (4, 6, 7),
        (0, 1, 5),
        (0, 5, 4),
        (2, 3, 7),
        (2, 7, 6),
        (0, 3, 7),
        (0, 7, 4),
        (1, 2, 6),
        (1, 6, 5)
    ]
    
    with open(filename, 'w') as file:
        file.write(header)
        
        for face in faces:
            normal = calculate_normal(vertices[face[0]], vertices[face[1]], vertices[face[2]])
            file.write("facet normal {} {} {}\n".format(normal[0], normal[1], normal[2]))
            file.write("outer loop\n")
            
            for vertex_index in face:
                vertex = vertices[vertex_index]
                file.write("vertex {} {} {}\n".format(vertex[0], vertex[1], vertex[2]))
                
            file.write("endloop\n")
            file.write("endfacet\n")
        
        file.write(footer)

def calculate_normal(v1, v2, v3):
    u = [v2[i]-v1[i] for i in range(3)]
    v = [v3[i]-v1[i] for i in range(3)]
    
    normal = [
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    ]
    
    return normal

if __name__ == "__main__":
    side_length = 10  # Change the side length of the cube as required
    filename = "cube.stl"
    generate_cube_stl(side_length, filename)
