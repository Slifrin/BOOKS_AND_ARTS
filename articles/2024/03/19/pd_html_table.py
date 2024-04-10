import pandas as pd
from pprint import pprint


html_text = """
<table border="0" cellpadding="2" cellspacing="0" class="xh-highlight">
        <tbody><tr class="">
            <td rowspan="1" class="">Case Title:  &nbsp;</td>
            <td colspan="4" class=""><strong>DEFENDANT BRADLEY DEFOREST SMITH</strong></td>
        </tr>
        <tr class="">
            <td class="">Case Number:   &nbsp;&nbsp;</td>
            <td class=""><strong>CN445028&nbsp;&nbsp;</strong></td>
            <td class="">Case Location:  &nbsp;&nbsp;</td>
            <td class=""><strong>North County &nbsp;&nbsp;</strong></td> 
            <td rowspan="1" colspan="2" align="center" class=""> 
                <font color="#000000">
                <input type="button" value=" File Location " name="locationButton" onclick="return displayLocation()">
                </font>
            </td>
        </tr>
        <tr class="">
            <td class="">Case Type:   &nbsp;&nbsp;</td>
            <td class=""><strong>Criminal&nbsp;&nbsp;</strong></td>
            <td class="">Date Filed:   &nbsp;&nbsp;</td>
            <td class=""><strong>08/04/2023</strong>&nbsp;&nbsp;</td>
        </tr>
    </tbody></table>
"""

html_text_v2 = """
<table class="data" border="1" cellpadding="2" cellspacing="0">
        <tbody><tr bgcolor="#E6E6FA">
            <td rowspan="1" colspan="5" align="center">
                Defendant &nbsp;
            </td> 
        </tr> 
        <tr bgcolor="#E6E6FA">
            <td rowspan="1">Last Name &nbsp;</td>                       
            <td rowspan="1">First Name &nbsp;</td>                       
            <td rowspan="1">Birth Year &nbsp;</td> 
            <td rowspan="1">AKA &nbsp;</td> 
            <td rowspan="1">DA Number  &nbsp;</td> 
        </tr> 
        
            <tr> 
                <td> 
                    <strong>AARON &nbsp;&nbsp;</strong>
                </td>
                <td> 
                    <strong>MICHELLE CHRISTINA &nbsp;&nbsp;</strong>
                </td>
                <td> 
                    <strong>1966 &nbsp;&nbsp;</strong>
                </td>
                <td>
                    <strong>Y &nbsp;</strong>
                </td> 
                <td>
                    <strong>OCX04501 &nbsp;</strong>
                </td> 
            </tr> 
            
            <tr> 
                <td> 
                    <strong>AARON &nbsp;&nbsp;</strong>
                </td>
                <td> 
                    <strong>MICHELLE CHRISTINE &nbsp;&nbsp;</strong>
                </td>
                <td> 
                    <strong>1966 &nbsp;&nbsp;</strong>
                </td>
                <td>
                    <strong>  &nbsp;</strong>
                </td> 
                <td>
                    <strong>OCX04501 &nbsp;</strong>
                </td> 
            </tr> 

    </tbody></table>"""

def parse_html_text(html_to_parse):
    table = pd.read_html(html_to_parse)
    pprint(table)
    print(type(table), type(table[-1]))

def main() -> None:
    print(f"Hello main from : {__file__}")
    parse_html_text(html_text)
    parse_html_text(html_text_v2)



if __name__ == "__main__":
    main()
