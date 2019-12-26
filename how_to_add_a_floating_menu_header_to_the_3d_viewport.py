"""
A test framework to show how to add a floating interface menu header to Blender 2.8x.
"""

import bpy
from bpy.types import Menu

bl_info = {
    "name": "Test Menu",
    "author": "Jeff Hanna",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D Viewport Header Interface Menu",
    "description": "Adds a new drop down menu to the 3D Viewport",
    "category": "Tech Artists",
}

class TestMenu(Menu):
    bl_label = "Test"
    bl_idname = "VIEW_MT_test_menu" # This should start with VIEW_MT_ and then be unique

    """
    A test menu showing how to add operators and separators.
    """

    def draw(self, layout):
        """
        Draws the menu.
        The first argument to the layout.operator() method is a string pointing to
        an operator's bl_idname. The operator does not to be instantiated before the 
        menu is drawn. If no matching operator is found the menu item will not be drawn.
        For this example I've used standard Blender operators to ensure the menu 
        draws correctly.

        Arguments:
            layout
        """

        layout = self.layout
        layout.operator("transform.transform", text="Test 00")
        layout.operator("object.randomize_transform", text="Test 01")
        layout.separator()
        layout.operator("object.align", text="Test 02")
        layout.menu("VIEW_MT_test_submenu")


class TestSubmenu(Menu):
    bl_label = "Test Submenu"
    bl_idname = "VIEW_MT_test_submenu"

    """
    A test submenu showing how it is added to the main menu.
    """

    def draw(self, layout):
        """
        Draws the menu.
        The first argument to the layout.operator() method is a string pointing to
        an operator's bl_idname. The operator does not to be instantiated before the 
        menu is drawn. If no matching operator is found the menu item will not be drawn.
        For this example I've used standard Blender operators to ensure the menu 
        draws correctly.
        
        Arguments:
            layout
        """
 
        layout = self.layout
        layout.operator("object.align", text = "Submenu Test 00")



def draw_menu(self, context):
    """
    A function that gets appended to Blender's list of editor menus. When Blender 
    calls this referenced function it draws the test menu header in the viewport.
   
    Arguments:
        context
    """
    layout = self.layout
    layout.menu(TestMenu.bl_idname)


classes = (TestMenu, TestSubmenu,)
register, unregister = bpy.utils.register_classes_factory(classes)
bpy.types.VIEW3D_MT_editor_menus.append(draw_menu)


if __name__ == '__main__':
    register()
