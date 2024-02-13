# A Memory Game in Pyscript

See the game online at **https://sdbenezra.github.io/Memory-Pyscript/**

As part of my investigation of various languages and frameworks I've build a memory game with [Pyscript](https://pyscript.net/).


I used this [resource](https://marina-ferreira.github.io/tutorials/js/memory-game/) from Marina Ferreira as a starting point
for the code. I chose it because it was built simply in HTML, CSS, and vanilla Javascript.
Pyscript basically allows Python to replace Javascript for web apps, while also allowing use of certain Javascript functions to 
manipulate the DOM. 

Another good reference was this [blog post](https://blog.logrocket.com/pyscript-run-python-browser/) with basic information on 
working with Pyscript.

Why use Python in place of Javascript? If you are familiar with Python and not so much with Javascript,
it is more convenient to have the option to use Python for front end coding. In addition, there are various libraries for data
science and machine learning applications that are only available in Python, so having access to those resources in the front
end is a benefit.



## Running the game locally
All files (index.html, main.py, styles.css, image folder etc) should be located in the same directory.
Use python to start a server by entering this command in your terminal ```python -m http.server```.
You should then be able to access the game on your browser at ```http://0.0.0.0:8000/``` or ```localhost:8000```.



*note: Docs folder contains files for Github pages site.*