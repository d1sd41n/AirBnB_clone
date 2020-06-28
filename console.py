#!/usr/bin/python3
"""Module's Doc"""
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User"]
    dic_classes = {"BaseModel":models.BaseModel, "User":models.User}
    attr_list = ["id", "created_at", "updated_at"]

    def do_create(self, objeto):
        """creates new class ex: $ create obj_name"""
        if not objeto:
            print("** class name missing **")
            return
        if objeto in self.classes:
            obj = self.dic_classes[objeto]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, options):
        """Docs"""
        if not options:
            print("** class name missing **")
            return

        options = options.split(" ")
        if options[0] in self.classes:
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
        """Doc"""
        if not options:
            print("** class name missing **")
            return

        options = options.split(" ")
        if options[0] in self.classes:
            if len(options) < 2:
                print("** instance id missing **")
                return
            dic = models.storage.all()
            name = options[0] + "." + options[1]
            if name in dic:
                del dic[name]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, options):
        """Doc"""
        dic = models.storage.all()
        lis = []
        cpy = options
        options = options.split(" ")
        if cpy:
            if options[0] in self.classes:
                for key in dic:
                    if options[0] == key.split(".")[0]:
                        lis.append(str(dic[key]))
            else:
                print("** class doesn't exist **")
        else:
            for key in dic:
                lis.append(str(dic[key]))
        print(lis)

    def do_update(self, options):
        """Doc"""
        dic = models.storage.all()
        cpy = options
        options = options.split(" ")

        if not cpy:
            print("** class name missing **")
            return

        if not options[0] in self.classes:
            print("** class doesn't exist **")
            return

        if len(options) < 2:
            print("** instance id missing **")
            return

        name = options[0] + "." + options[1]
        if not name in dic:
            print("** no instance found **")
            return

        if len(options) < 3:
            print("** attribute name missing **")
            return

        if len(options) < 4:
            print("** value missing **")
            return

        options[3] = options[3].replace("\"", "")
        dic[name].__dict__[options[2]] = type(dic[name].__dict__[options[2]])(options[3])
        models.storage.save()

    def emptyline(self):
        """Nothing happends"""
        pass

    def do_EOF(self, line):
        """Exit command"""
        return True

    def do_quit(self, line):
        """Exit command"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
