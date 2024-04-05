import bpy
import re

# Get all materials in the scene
materials = bpy.data.materials

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.dff.day_cols = False
        obj.dff.night_cols = False
# Loop through each material
for material in materials:
    # Find and extract words inside square brackets from the material name
    bracket_contents = re.findall(r'\[(.*?)\]', material.name)
    
    # If there are bracket contents
    if bracket_contents:
        # Split the contents by comma to separate words
        words = bracket_contents[0].split(',')
        
        # Process each word
        for word in words:
            word = word.strip()  # Remove leading/trailing spaces
            # Example processing:
            if 'spec' in word:
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)
                material.diffuse_color = (1, 1, 1, 1)
                material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 1
                material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1
                material.dff.ambient = 0.5
                material.dff.export_specular = True
                material.dff.specular_level = 0.2
                material.dff.specular_texture = "vehiclespecdot64"
            elif 'none' in word:
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)
                material.diffuse_color = (1, 1, 1, 1)
                material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 1
                material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1
                material.dff.ambient = 0.5
                material.dff.export_env_map = False
                material.dff.export_specular = False
                material.dff.export_reflection = False
            elif 'prim' in word:
                r_prim = 60 / 255
                g_prim = 255 / 255
                b_prim = 0 / 255
                a_prim = 255 / 255
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (r_prim, g_prim, b_prim, a_prim)
                material.diffuse_color = (r_prim, g_prim, b_prim, a_prim)
                material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 1
                material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1
                material.dff.ambient = 0.5
                material.dff.export_env_map = True
                material.dff.env_map_tex = "xvehicleenv128"
                material.dff.env_map_coef = 1
                material.dff.env_map_fb_alpha = False
                material.dff.export_reflection = True
                material.dff.reflection_scale_x = 1
                material.dff.reflection_scale_y = 1
                material.dff.reflection_offset_x = 1
                material.dff.reflection_offset_y = 1
                material.dff.reflection_intensity = 0.05
                material.dff.export_specular = True
                material.dff.specular_level = 0.2
                material.dff.specular_texture = "vehiclespecdot64"
            elif 'ref' in word:
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)
                material.diffuse_color = (1, 1, 1, 1)
                material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 1
                material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1
                material.dff.ambient = 0.5
                material.dff.export_env_map = True
                material.dff.env_map_tex = "vehicleenvmap128"
                material.dff.env_map_coef = 1
                material.dff.env_map_fb_alpha = False
                material.dff.export_reflection = True
                material.dff.reflection_scale_x = 1
                material.dff.reflection_scale_y = 1
                material.dff.reflection_offset_x = 1
                material.dff.reflection_offset_y = 1
                material.dff.reflection_intensity = 0.08
                material.dff.export_specular = True
                material.dff.specular_level = 0.2
                material.dff.specular_texture = "vehiclespecdot64"
            elif 'glass' in word:
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 0, 0, 0.5)
                material.diffuse_color = (0, 0, 0, 0.5)
                material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 1
                material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1
                material.dff.ambient = 0.5
                material.dff.export_env_map = True
                material.dff.env_map_tex = "vehicleenvmap128"
                material.dff.env_map_coef = 1
                material.dff.env_map_fb_alpha = False
                material.dff.export_reflection = True
                material.dff.reflection_scale_x = 1
                material.dff.reflection_scale_y = 1
                material.dff.reflection_offset_x = 1
                material.dff.reflection_offset_y = 1
                material.dff.reflection_intensity = 0.08
                material.dff.export_specular = True
                material.dff.specular_level = 0.2
                material.dff.specular_texture = "vehiclespecdot64"
            elif 'mirror' in word:
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)
                material.diffuse_color = (1, 1, 1, 1)
                material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 1
                material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = 1
                material.dff.ambient = 0.5
                material.dff.export_env_map = True
                material.dff.env_map_tex = "vehicleenvmap128"
                material.dff.env_map_coef = 1
                material.dff.env_map_fb_alpha = False
                material.dff.export_reflection = True
                material.dff.reflection_scale_x = 1
                material.dff.reflection_scale_y = 1
                material.dff.reflection_offset_x = 1
                material.dff.reflection_offset_y = 1
                material.dff.reflection_intensity = 0.5
                material.dff.export_specular = True
                material.dff.specular_level = 0.2
                material.dff.specular_texture = "vehiclespecdot64"
            elif 'FR' in word:
                r_fr = 0 / 255
                g_fr = 255 / 255
                b_fr = 200 / 255
                a_fr = 255 / 255
                material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (r_fr, g_fr, b_fr, a_fr)
                material.dff.ambient = 0.5