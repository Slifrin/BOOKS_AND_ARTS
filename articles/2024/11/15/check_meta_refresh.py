from pprint import pprint
from w3lib.html import get_meta_refresh


def simple_example():
    text_data = """
 <html xmlns="http://www.w3.org/1999/xhtml">    
  <head>      
    <title>The Tudors</title>      
    <meta http-equiv="refresh" content="45;URL='http://thetudors.example.com/'" />    
  </head>    
  <body> 
    <p>This page has moved to a <a href="http://thetudors.example.com/">
      theTudors.example.com</a>.</p> 
  </body>  
</html>     
    """
    # returns timer and url to which it should be redirected
    pprint(get_meta_refresh(text_data))


def main() -> None:
    print(f"Hello main from : {__file__}")
    simple_example()


if __name__ == "__main__":
    main()
