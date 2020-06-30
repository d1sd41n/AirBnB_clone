#!/usr/bin/python3
"""Module's Doc"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "Place",
               "City", "Amenity", "Review", "State"]
    attr_list = ["id", "created_at", "updated_at"]

    def do_create(self, objeto):
        """creates new class ex: $ create obj_name"""
        if not objeto:
            print("** class name missing **")
            return
        if objeto in self.classes:
            obj = models.dic_classes[objeto]()
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
                return
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
        if name not in dic:
            print("** no instance found **")
            return

        if len(options) < 3:
            print("** attribute name missing **")
            return

        if len(options) < 4:
            print("** value missing **")
            return

        options[3] = options[3].replace("\"", "")
        f = False
        if options[2] in models.dic_classes[options[0]].__dict__:
            value = models.dic_classes[options[0]].__dict__[options[2]]
            f = True
        if f:
            dic[name].__dict__[options[2]] = type(value)(options[3])
        else:
            dic[name].__dict__[options[2]] = options[3]
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

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and
        returns.
        """
        line = line.split(".")
        if line[0] in self.classes:
            if line[1] == "all()":
                self.do_all(line[0])
            elif line[1] == "count()":
                dic = models.storage.all()
                lis = []
                for key in dic:
                    if line[0] == key.split(".")[0]:
                        lis.append(str(dic[key]))
                print(len(lis))
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
