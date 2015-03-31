# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "1 Awesome Fusee Uniplug GUI dodad",
    "author": "The super awesome Fusee team",
    "version": (0, 0, 1),
    "blender": (2, 70, 0),
    "description": "Testing different GUI functions",
    "category": "User Interface"
}
import bpy

class Bla(bpy.types.Operator):
    """Bla"""
    bl_idname = "object.bla"
    bl_label = "Bla"
    bl_options = {'REGISTER', 'UNDO'}

# http://www.blender.org/api/blender_python_api_2_73a_release/bpy.props.html
    booly = bpy.props.BoolProperty(name="My Bool", default=True, subtype='ANGLE')
    boolyv = bpy.props.BoolVectorProperty(name="My Bool Vector", default=(True,False,True, False), size=4)
    floaty = bpy.props.FloatProperty(name="My Float", default=0.4527)
    floatyv= bpy.props.FloatVectorProperty(name="MY Float Vector", size=5)
    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)  # The only one in use
    intyv = bpy.props.IntVectorProperty(name="My Int Vector", size=2, default=(2,6))
    stringy = bpy.props.StringProperty(name="My Sting")
    stringy = bpy.props.StringProperty(name="My Sting Path", subtype='FILE_PATH')

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        for i in range(self.total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(Bla.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(Bla)
    bpy.types.VIEW3D_MT_view.append(menu_func)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    # handle the keymap
    wm = bpy.context.window_manager
    # Note that in background mode (no GUI available), keyconfigs are not available either, so we have to check this
    # to avoid nasty errors in background case.
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(Bla.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
        kmi.properties.total = 4
        addon_keymaps.append((km, kmi))

def unregister():
    # Note: when unregistering, it's usually good practice to do it in reverse order you registered.
    # Can avoid strange issues like keymap still referring to operators already unregistered...
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

	#bpy.utils.unregister_class(BasicMenu)
    bpy.types.VIEW3D_MT_view.remove(menu_func)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(Bla)



if __name__ == "__main__":
    register()