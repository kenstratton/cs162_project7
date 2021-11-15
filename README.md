# cs162_project7
Description of Inheritance, Exceptions, and Polymorphism

## Build A Design

### ▼ Pick a generic object where something could cause exception in its state
A generic object represents Vegetable so that various species are created passed with its features.</br>
And the features could be subject to exceptions.

### ▼ Describe a generic exception that could happen in your object
My generic exception works at unspecific errors shares common features with sub exceptions.

### ▼ Describe two subclasses of the object
Vegetable subclasses can take over a method from a generic class.</br>
Also, they have a diferent quality to each common attribute.(polymorphism)</br>
In case of Tomato and Papper, for example, they have different values in water percentage and suitable temperature.

### ▼ Describe two subclasses of the exception
Each sub exception would work at an error from one attribute of a vegetable subclass.</br>
・WaterError - water percents of an input and expectation are different</br>
・TempError - temperature of an input and expectation are different

### ▼ Draw an inheritance diagram (relationships between the classes and the exceptions)
<img width="450" alt="Screen Shot 2021-11-16 at 1 55 02" src="https://user-images.githubusercontent.com/77530003/141822142-4b4f8141-3822-4eba-bcc3-1b5b66e22f98.png">

### ▼ Design a program of the planned classes and inheritance diagram showing how inheritance can work
A planned program would be quiz-formed.</br>
Different vegetable species have a different value in the same attribute (e.g. suitable temperature).</br>
A user answers to choice questions about this.
Inheritance could work when sub vegetables use a common method derived from Vegetable.
For example, a method printing their own information would be implemented.

## Implementation of a simple program
[-> Application URL](https://github.com/kenstratton/cs162_project7/tree/main/vege_learning)

## What kinds of tests would be useful?
**For inheritance and polymorphism :**</br>
・Check inheritance relationship between a subclass and a generic class</br>
・-> issubclass(subclass, generic class)</br>
・Check if instances of different subclasses return a different value in the same attribute</br>

**For exceptions :**</br>
・Check if a custom exception is raised when unexpected input is detected.</br>
・-> pytest.raises(Exception)</br>
・Check if an error handler outputs expcetedly when a custom exception is raised
