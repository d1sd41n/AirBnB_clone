#!/usr/bin/python3
"""Module's Doc"""
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_create(self, objeto):
        """creates new class ex: $ create obj_name"""
        if not objeto:
            print("** class name missing **")
            return
        if objeto == "BaseModel":
            obj = models.BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, options):
        if not options:
            print("** class name missing **")
            return

        options = options.split(" ")
        if options[0] == "BaseModel":
            if len(options) < 2:
                print("** instance id missing **")
                return
            dic = models.storage.all()
            name = options[0] + "." + options[1]

            if name in dic:
                print(dic[name])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, options):
        if not options:
            print("** class name missing **")
            return

        options = options.split(" ")
        if options[0] == "BaseModel":
            if len(options) < 2:
                print("** instance id missing **")
                return
            dic = models.storage.all()
            name = options[0] + "." + options[1]

            if name in dic:
                del dic[name]
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

        
    def do_EOF(self, line):
        """Exit command"""
        return True

    def do_quit(self, line):
        """Exit command"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
