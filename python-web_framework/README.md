# Python - Web framework

### Resources
- <a href="https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb">What is a Web Framework?</a>
- <a href="https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application">A Minimal Application</a>
- <a href="https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates">Rendering Templates</a>
- <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/#variables">Synopsis</a>
- <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/">jinja</a>
- <href="https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures">list-control-structures</a>
<a href="https://youtu.be/MwZwr5Tvyxo?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH">Flask tutorial </a>


### Install Flask
pip3 install Flask

## Tasks
### 0. Hello Flask!
mandatory
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition

- guillaume@ubuntu:~/AirBnB_v2$ python3 0-hello_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....


In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 

### 1. HBNB

Copy the previous task to a new script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition



guillaume@ubuntu:~/AirBnB_v2$ python3 1-hbnb_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 


### 2. C is fun!
mandatory
Copy the previous task to a new script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
- You must use the option strict_slashes=False in your route definition


guillaume@ubuntu:~/AirBnB_v2$ python3 2-c_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 


### 2. C is fun!
mandatory
Copy the previous task to a new script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
- You must use the option strict_slashes=False in your route definition


guillaume@ubuntu:~/AirBnB_v2$ python3 2-c_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 




### 4. Is it a number?
mandatory
Copy the previous task to a new script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
- You must use the option strict_slashes=False in your route definition


guillaume@ubuntu:~/AirBnB_v2$ python3 4-number_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$




### 5. Number template
mandatory
Copy the previous task to a new script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
        - H1 tag: “Number: n” inside the tag BODY
- You must use the option strict_slashes=False in your route definition


guillaume@ubuntu:~/AirBnB_v2$ python3 5-number_template.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$



### 6. Odd or even?
mandatory
Copy the previous task to a new script that starts a Flask web application:
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
        - H1 tag: “Number: n” inside the tag BODY
    - /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        - H1 tag: “Number: n is even|odd” inside the tag BODY
- You must use the option strict_slashes=False in your route definition


guillaume@ubuntu:~/AirBnB_v2$ python3 6-number_odd_or_even.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:

guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 