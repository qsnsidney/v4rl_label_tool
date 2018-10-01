import bpy

bbox_data = []
with open("/path/to/project/output/3_labelimg/world_bbox.txt", 'r') as f:
    for line in f:
        l = line.split()
        l = [float(x) for x in l]
        bbox_data.append(tuple(l))

for i in range(len(bbox_data)):    
    bpy.ops.mesh.primitive_cube_add(location=bbox_data[i][:3]) 
    bpy.context.scene.objects.active.rotation_euler = bbox_data[i][6:]
    bpy.context.scene.objects.active.dimensions = bbox_data[i][3:6]
    
