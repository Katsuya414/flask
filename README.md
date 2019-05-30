## Creation
scraping server application

## Choice language
Python

## About the environment
OS macOS ver 10.13.6

python version Python 3.7.2

Additional library requests, bs4,json,flask

## Environment construction method
Homebrew install

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

pip install
```
brew install python3
```

Additional library install
```
pip3 install requests
pip3 install bs4
pip3 install json
pip3 install numpy
```

## How to run a server application
```
python3 run2.py
```
URL accsess
```
http://localhost:5000/form
```
demo Video
- https://github.com/Katsuya414/flask/blob/master/example.mov

<img width="234" alt="example" src="https://user-images.githubusercontent.com/23134366/58650882-ceb07480-834a-11e9-90f3-59254892ef6b.png">


<img width="1186" alt="example2" src="https://user-images.githubusercontent.com/23134366/58650829-b2acd300-834a-11e9-8b16-d904007dc470.png">



## Future implementation plan (if you have time)
- Create Docker image
- Add processing when there is no query and processing when there is no value for it
- Add a design (for appearance)
