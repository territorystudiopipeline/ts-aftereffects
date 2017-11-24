# Copyright (c) 2014 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Logic to populate the Shotgun menu in Cinema4d
"""

import os
import sys
import c4d
import c4d.gui
import subprocess

import c4d
from c4d import gui, bitmaps, plugins, utils

class MenuGenerator(object):
    """
    Class used by the Cinema4D engine to build the Shotgun menu from the various
    commands registered by the apps that have been loaded.
    """
    def __init__(self, engine):
        """
        Construction
        
        :param engine:    The toolkit engine that owns this menu generator
        """
        self._engine = engine

    # def create_menu(self):
    #     """
    #     Create the Shotgun menu
    #     """
        
    #     print "CREATE MENU HAPPENING INSIDE OF C4D"

        # #Get the main/plugins menus
        # mainMenu = c4d.gui.GetMenuResource("M_EDITOR")
        # pluginsMenu = c4d.gui.SearchPluginMenuResource()

        # #Create the menu container and set the title of the new entry
        # menu = c4d.BaseContainer()
        # menu.InsData(c4d.MENURESOURCE_SUBTITLE, "Shotgun")
        
        # #Add a string that shows current context
        # # ctx = self._engine.context
        # # ctx_name = str(ctx)
        # # menu.InsData(c4d.MENURESOURCE_STRING, ctx_name)
        # menu.InsData(c4d.MENURESOURCE_COMMAND, "IDM_NEU")             # Add registered default command 'New Scene' to the menu

        # #Add jump to Shotgun/Filesystem commands
        # # c4d.plugins.RegisterCommandPlugin(PLUGIN_ID, "Jump to Shotgun", 0, None, "Jump To Shotgun Command", self._jump_to_sg())
        # # menu.InsData(c4d.MENURESOURCE_STRING, "Jump to Shotgun")
        # # menu.InsData(c4d.MENURESOURCE_STRING, "Jump to Filesystem")

        # #Add separator
        # menu.InsData(c4d.MENURESOURCE_SEPERATOR, True);               # Add a separator

        # #Insert menu
        # if pluginsMenu:
        #     # Insert menu after 'Plugins' menu
        #     mainMenu.InsDataAfter(c4d.MENURESOURCE_STRING, menu, pluginsMenu)
        # else:
        #     # Insert menu after the last existing menu ('Plugins' menu was not found)
        #     mainMenu.InsData(c4d.MENURESOURCE_STRING, menu)

        # #Update menus
        # self._engine.log_debug(c4d.gui)
        # c4d.gui.UpdateMenus()

        # context_menu = self.__build_context_menu(shotgun_menu)
        # mari.menus.addSeparator(shotgun_menu)

        # # now enumerate all items and create menu objects for them
        # menu_items = []
        # for (cmd_name, cmd_details) in self._engine.commands.items():
        #     #if not (cmd_name == "Shotgun File Manager..." or cmd_name == "Version up Current Scene..."):
        #     menu_items.append(AppCommand(cmd_name, cmd_details, self.__action_factory))

        # commands_by_app = {}
        # for cmd in menu_items:
        #     if cmd.get_type() == "context_menu":
        #         cmd.add_to_menu(context_menu)
        #     else:
        #         app_name = cmd.get_app_name()
        #         if app_name is None:
        #             app_name = "Other Items"
        #         if not app_name in commands_by_app:
        #             commands_by_app[app_name] = []
        #         commands_by_app[app_name].append(cmd)

        # self.__build_app_menu(commands_by_app, shotgun_menu)


#     def destroy_menu(self):
#         """
# #         Clean up the Shotgun menu by removing all items.  
#         """

#         print "DESTROY MENU HAPPENING INSIDE OF C4D"
#         self._engine.log_debug("Destroying the Shotgun menu for Mari...")
        
#         # clear the action factory:
#         self.__action_factory.clear()

#         # Remove all menu actions from sub-menus - note that this doesn't currently
#         # remove the actual sub-menus - how do we do that?
#         sub_menus = mari.menus.submenus(MenuGenerator.MAIN_MENU_SET, MenuGenerator.SHOTGUN_MENU_ROOT)
#         for sm in sub_menus:
#             actions = mari.menus.actions(MenuGenerator.MAIN_MENU_SET, MenuGenerator.SHOTGUN_MENU_ROOT, sm)
#             for action in actions:
#                 mari.menus.removeAction("%s/%s/%s/%s" % (MenuGenerator.MAIN_MENU_SET, MenuGenerator.SHOTGUN_MENU_ROOT, 
#                                                          sm, action.name()))
        
#         # remove all actions from the Shotgun root menu:
#         actions = mari.menus.actions(MenuGenerator.MAIN_MENU_SET, MenuGenerator.SHOTGUN_MENU_ROOT)
#         for action in actions:
#             mari.menus.removeAction("%s/%s/%s" % (MenuGenerator.MAIN_MENU_SET, MenuGenerator.SHOTGUN_MENU_ROOT, 
#                                                   action.name()))        

    # def _jump_to_sg(self):
    #     """
    #     Jump to shotgun, launch web browser
    #     """
    #     url = self._engine.context.shotgun_url
    #     if sys.platform=='darwin':
    #         subprocess.Popen(['open', url])
    #     elif sys.platform=='win32':
    #         os.startfile(url)
    #     else : 
    #         c4d.gui.MessageDialog("Please open URL at : %s" % url)

    # def _jump_to_fs(self):
    #     """
    #     Jump from context to the file system
    #     """
    #     # launch one window for each location on disk
    #     paths = self._engine.context.filesystem_locations
    #     for disk_location in paths:

    #         # get the setting
    #         system = sys.platform

    #         # run the app
    #         if system == "linux2":
    #             cmd = "xdg-open \"%s\"" % disk_location
    #         elif system == "darwin":
    #             cmd = "open \"%s\"" % disk_location
    #         elif system == "win32":
    #             cmd = "cmd.exe /C start \"Folder\" \"%s\"" % disk_location
    #         else:
    #             raise Exception("Platform '%s' is not supported." % system)

    #         exit_code = os.system(cmd)
    #         if exit_code != 0:
    #             self._engine.log_error("Failed to launch '%s'!" % cmd)

#     def __build_app_menu(self, commands_by_app, shotgun_menu):
#         """
#         Build the main app menu for all app commands
        
#         :param commands_by_app:    A dictionary of commands to add to the main Shotgun menu
#         :param shotgun_menu:       The full path to the shotgun menu         
#         """
#         for app_name in sorted(commands_by_app.keys()):
#             if len(commands_by_app[app_name]) > 1:
#                 # create a sub-menu to put these commands under
#                 menu_name = "%s/%s" % (shotgun_menu, app_name)
#                 for cmd in commands_by_app[app_name]:
#                     cmd.add_to_menu(menu_name)
#             else:
#                 # just create a single menu item for this command
#                 cmd = commands_by_app[app_name][0]
#                 cmd.add_to_menu(shotgun_menu)


#     def __build_context_menu(self, shotgun_menu):
#         """
#         Build the standard context menu with jump-to-file-system & jump-to-shotgun
#         commands
        
#         :param shotgun_menu:    The full path to the shotgun menu
#         :returns:               Returns the path to the context menu
#         """
#         ctx = self._engine.context
#         ctx_name = str(ctx)
        
#         # Because there is currently no API for removing empty sub-menus (see foundry
#         # issue #2014080310000042) it's not a good idea to create the normal work
#         # are sub-menu as switching context will result in the menu being confusing
#         # with multiple context sub-menus all with different work areas!
#         # Instead, we create a single 'Current Work Area' menu and add an item under
#         # this to describe the work area that we can remove.
#         ctx_menu = "%s/%s" % (shotgun_menu, "Current Work Area")
#         action = mari.actions.create(ctx_name, "")
#         mari.menus.addAction(action, ctx_menu)
#         mari.menus.addSeparator(ctx_menu)

#         # When this is possible, the context menu should be created with the context
#         # name in-line with the rest of the engines:
#         # ctx_menu = "%s/%s" % (shotgun_menu, ctx_name)
        
#         action = self.__action_factory.create_action("Jump To File System", self._jump_to_fs)
#         mari.menus.addAction(action, ctx_menu)
#         action = self.__action_factory.create_action("Jump To Shotgun", self._jump_to_sg)
#         mari.menus.addAction(action, ctx_menu)

#         return ctx_menu

# class AppCommand(object):
#     """
#     Wrapper for a command registered by an app
#     """
#     def __init__(self, name, command_dict, action_factory):
#         """
#         Construction
        
#         :param name:            The name of the command
#         :param command_dict:    A dictionary of parameters specified for the command
#         :param action_factory:  An instance of the ActionFactory class used to create
#                                 Mari actions for command callbacks
#         """
#         self.name = name
#         self.properties = command_dict["properties"]
#         self.callback = command_dict["callback"]
#         self.favourite = False
#         self.__action_factory = action_factory
#         self.__action = None

#     def get_app_name(self):
#         """
#         Find the display name for the app this command was loaded from
        
#         :returns:    The app display name if known
#         """
#         if "app" not in self.properties:
#             return None 
#         return self.properties["app"].display_name

#     def get_app_instance_name(self):
#         """
#         Find the instance name for the app this command was loaded from
        
#         :returns:    The app instance name if known
#         """
#         if "app" not in self.properties:
#             return None

#         app_instance = self.properties["app"]
#         engine = app_instance.engine

#         for (app_instance_name, app_instance_obj) in engine.apps.items():
#             if app_instance_obj == app_instance:
#                 # found our app!
#                 return app_instance_name

#         return None

#     def get_type(self):
#         """
#         Find the type of this command
        
#         :returns:    The type of the command or 'default' if not found
#         """
#         return self.properties.get("type", "default")

#     def add_to_menu(self, menu):
#         """
#         Add this command to the menu
        
#         :param menu:    The menu this command should be added to.
#         """
#         # create a new action for the command if needed:
#         if not self.__action:
#             self.__action = self.__action_factory.create_action(self.name, self.callback)
        
#         if self.__action:
#             # add the action to the menu:
#             mari.menus.addAction(self.__action, menu)




