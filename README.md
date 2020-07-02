# AirBnB clone

<a href="https://ibb.co/qyd6YzT"><img src="https://i.ibb.co/SsPSw2F/sdsds.png" alt="sdsds" border="0"></a>

## Project Overview

This project is the first part of replica of AirBnB aplication that we are gonig to build from scratch. This part of the project consist on a terminal which would serve to us the developers as a maintenance tool to manage data.

### Installing

1. Clone this repo:

```sh
$ git clone <https://github.com/d1sd41n/AirBnB_clone.git>
```

2. Run the console:

```sh
$ ./console.py
```

or

```sh
$ python3 console.py
```

3. Promt will be displayed, run a command:

```sh
(hbnb) <command>
```

### Usage

There are two ways, interactive and non-interactive to use the terminal

#### interactive:

```sh
$ ./console.py
(hbnb)
```

#### non-interactive:

```sh
$ echo "create User" | console.py
(hbnb) 97e83507-844e-4d4e-b084-21c390a627e0
$
```

### Structure
<a href="https://ibb.co/gS6vpdN"><img src="https://i.ibb.co/Byw4xGb/pld-1.png" alt="pld-1" border="0"></a><br /><a target='_blank' href='https://es.imgbb.com/'>formatos de fotos</a><br />

#### Comands:

- help: displays all commands available
- EOF, quit: close the terminal
- all: show all data stored
- all \<class\>: show all data of an specific class
- show \<class\> \<id\>: displays an objec of an specific class and id
- create \<class\>: creates a new object of an specific class
- destroy \<class\> \<id\>: deletes an objec of an specific class and id
- update \<class\> \<id\> \<attribute\> \<value\>: edit an attribute of an specific class and id
  
- \<class\>.all() : same of all \<class\>
- \<class\>.count(): displays amount of objects of an specific class

##### example:

``` sh
$ ./console.py
(hbnb) all
[]
(hbnb) create User
d1b60276-382e-40a9-a8ed-2f5c19030e6a
(hbnb) all
["[User] (d1b60276-382e-40a9-a8ed-2f5c19030e6a) {'updated_at': datetime.datetime(2020, 7, 1, 23, 23, 9, 902437), 'id': 'd1b60276-382e-40a9-a8ed-2f5c19030e6a', 'created_at': datetime.datetime(2020, 7, 1, 23, 23, 9, 902437)}"]
(hbnb) all User
["[User] (d1b60276-382e-40a9-a8ed-2f5c19030e6a) {'updated_at': datetime.datetime(2020, 7, 1, 23, 23, 9, 902437), 'id': 'd1b60276-382e-40a9-a8ed-2f5c19030e6a', 'created_at': datetime.datetime(2020, 7, 1, 23, 23, 9, 902437)}"]
(hbnb) destroy User d1b60276-382e-40a9-a8ed-2f5c19030e6a
(hbnb) all User
[]
(hbnb) create Place
f7bfb839-d345-46b2-812f-e2f93d3ef75f
(hbnb) Place.all()
["[Place] (f7bfb839-d345-46b2-812f-e2f93d3ef75f) {'updated_at': datetime.datetime(2020, 7, 1, 23, 23, 22, 60728), 'id': '5947d703-104b-4f72-b9c0-9f06568b5444', 'created_at': datetime.datetime(2020, 7, 1, 23, 23, 22, 60728)}"]
(hbnb) Place.count()
1
(hbnb) quit
$
```
  
## Authors

* Daniel Perez [https://github.com/d1sd41n](https://github.com/d1sd41n)
* Juan Olivares [https://github.com/JuanOlivares1](https://github.com/JuanOlivares1)
