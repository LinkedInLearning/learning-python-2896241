# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pass

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        pass

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)    

if __name__ == "__main__":
    main()
  