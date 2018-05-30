bl_info = {
    "name": "Cycle Draw Type",
    "category": "Object",
}

import bpy

addon_keymaps = []

class CycleDrawType(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cycle_draw_type"
    bl_label = "Cycle Draw Type"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        currentType = context.active_object.draw_type
        if currentType == 'WIRE':
          targetType = 'TEXTURED'
        else:
          targetType = 'WIRE'
        for obj in context.selected_objects:
          obj.draw_type = targetType

        return {'FINISHED'}

def register():
    bpy.utils.register_class(CycleDrawType)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')

    kmi = km.keymap_items.new(CycleDrawType.bl_idname, 'W', 'PRESS', alt=True)
    addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(CycleDrawType)


if __name__ == "__main__":
    register()
