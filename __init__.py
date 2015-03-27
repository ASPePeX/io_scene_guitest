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
    "category": "User Interface"}

def register():
	print("Register")
#    bpy.utils.register_module(__name__)
#    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
	print("Unregister")
#    bpy.utils.unregister_module(__name__)
#    bpy.types.INFO_MT_file_export.remove(menu_func_export)

#if __name__ == "__main__":
#    register()
