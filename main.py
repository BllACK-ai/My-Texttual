from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, HorizontalScroll, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Footer, Placeholder, Static, Button, Header, Label, Input
import asyncio


    
ASCII_CAT = r"""
 ⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿ ⣿ ⣿
 ⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿ ⣿ ⣿
 ⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉ ⣿ ⣿
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇ ⣿ ⣿
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴ ⣿ ⣿
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿ ⣿
 ⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿ ⣿ ⣿
 ⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾ ⣿ ⣿
 ⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃ ⣿ ⣿
 ⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄ ⣿ ⣿
 ⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄ ⣿ ⣿
 ⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀ ⣿ ⣿
 ⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⣠⣴ ⣿ ⣿
"""
site ="""
⣿⣿⣷⡁⢆⠈⠕⢕⢂⢕⢂⢕⢂⢔⢂⢕⢄⠂⣂⠂⠆⢂⢕⢂⢕⢂⢕⢂⢕⢂
⣿⣿⣿⡷⠊⡢⡹⣦⡑⢂⢕⢂⢕⢂⢕⢂⠕⠔⠌⠝⠛⠶⠶⢶⣦⣄⢂⢕⢂⢕
⣿⣿⠏⣠⣾⣦⡐⢌⢿⣷⣦⣅⡑⠕⠡⠐⢿⠿⣛⠟⠛⠛⠛⠛⠡⢷⡈⢂⢕⢂
⠟⣡⣾⣿⣿⣿⣿⣦⣑⠝⢿⣿⣿⣿⣿⣿⡵⢁⣤⣶⣶⣿⢿⢿⢿⡟⢻⣤⢑⢂
⣾⣿⣿⡿⢟⣛⣻⣿⣿⣿⣦⣬⣙⣻⣿⣿⣷⣿⣿⢟⢝⢕⢕⢕⢕⢽⣿⣿⣷⣔
⣿⣿⠵⠚⠉⢀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⢕⢕⣽⣿⣿⣿⣿
⢷⣂⣠⣴⣾⡿⡿⡻⡻⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣵⣵⣵⣷⣿⣿⣿⣿⣿⣿⡿
⢌⠻⣿⡿⡫⡪⡪⡪⡪⣺⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠣⡁⠹⡪⡪⡪⡪⣪⣾⣿⣿⣿⣿⠋⠐⢉⢍⢄⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈
⡣⡘⢄⠙⣾⣾⣾⣿⣿⣿⣿⣿⣿⡀⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⣿⠏⠠⠈
⠌⢊⢂⢣⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⢅⣿⣿⣿⣿⡿⢋⢜⠠⠈
⠄⠁⠕⢝⡢⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣕⣑⣑⣑⣵⣿⣿⣿⡿⢋⢔⢕⣿⠠⠈
⠨⡂⡀⢑⢕⡅⠂⠄⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⢔⢕⢕⣿⣿⠠⠈
⠄⠪⣂⠁⢕⠆⠄⠂⠄⠁⡀⠂⡀⠄⢈⠉⢍⢛⢛⢛⢋⢔⢕⢕⢕⣽⣿⣿⠠⠈
"""

DECK ="""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⢻⣿⣿⣿⣿⣿⣿⣿⡿⢿⣫⣿⣿⣿
⣿⣿⣿⣿⣿⣻⢿⣿⣇⣿⡏⣿⣿⡿⣩⣷⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠟⣻⡣⠝⠛⠘⠃⣿⢟⣼⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⣫⣵⣿⣿⡏⠄⠄⠄⠄⠄⣛⣭⣭⣽⣟⣻⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡀⠄⠄⠄⢀⣶⣍⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⣀⣠⣶⡿⣾⣿⡞⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""    
sight ="""
⠄⠄⠄⠄⠄⠄⢀⣀⣀⣄⣄⣤⣠⣀⣀
⠄⠄⠄⡀⣔⣶⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀
⠄⢀⢆⡯⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀
⠄⡎⣎⣟⣿⣿⣿⣿⣿⣿⢿⢻⣙⢍⢭⢩⢋⠿⢿⣿⣿⣦
⠅⡎⣞⡾⣿⣿⣿⣿⢯⢏⢞⠸⠢⡹⣮⣷⣕⣗⣕⠹⣿⣿⣇
⢁⠪⡪⣟⣽⣻⢿⣽⢣⡃⡇⣏⢧⠕⠘⠻⢯⢱⡲⢝⠹⣿⣿
⠠⢑⠹⡸⣺⢞⣟⣗⢕⢕⢵⠬⡻⡀⠄⠄⢐⣕⢾⢜⠌⣿⣿
⠐⠠⠑⡍⡮⢯⣳⡻⡜⡌⢎⢢⠫⡲⣒⢔⢳⢺⡱⡱⣱⣿⣿
⠄⢁⠁⡂⠕⢕⢕⢽⠵⣕⢱⢱⠱⡱⡱⡱⢰⢑⠕⣕⣿⣿⠇
⠈⡀⠐⠠⠈⡂⠕⢕⠝⡎⡗⡎⣎⢆⡣⣣⣱⣼⡾⣿⣿⠋
⠄⠄⠌⡀⢂⠠⠁⡂⡑⠅⠇⡇⢗⢝⢽⢕⣟⢾⢽⠛
⠄⠄⠄⠈⠠⠂⢄⠄⡐⢈⠐⠨⠨⢈⢊⠪⠘⠈
"""  

cloud ="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⠤⢀⠀⠀⠀⠀⠀⠀⠐⠒⠒⠒⠶⠮⣅⣿⠛⠶⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⢀⢰⢈⣹⠓⣾⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⠀⢠⠐⣪⣭⣅⢤⣿⠞⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣶⢃⡃⠟⠓⡁⣫⡄⡀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡰⢫⣟⠿⠧⣿⣿⣥⠴⣴⣮⣏⡣⣄⣲⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣽⡵⢡⠤⠀⠈⢿⣷⠆⢚⡋⡁⢤⣿⡿⠁⠀⠀⠀⠀⢀⡤⠊⠉⠉⠙⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣤⠖⠶⡟⡧⢿⠀⠀⠀⠀⠀⠛⠶⣾⣷⡶⠟⠛⠉⢣⠀⣀⣀⣀⡜⠁⠀⠀⣠⠏⠁⠀⠀⢹⡠⠤⣄⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡜⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣇⡀⢅⠀⠀⠀⠀
⠀⠀⠁⠩⠵⠴⠲⠔⠶⠶⠶⠦⠴⠶⠶⠶⠖⠦⠤⢴⠏⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⡧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⣀⣀⣀⢀⣀⠀⠀⠀⠀⠀⠀⣀⣀⠤⠞⠁⠀⡜⢸⡏⠀⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠽⠕⠋⠘⠓⠒⠲⠤⠤⠤⡖⣛⠴⠶⡲⠮⠭⢶⣭⠦⠤⠎⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⡀
⠀⠀⠀⢀⣀⣔⡽⣧⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⠢⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠁⠀⠀⠉⢆
⠀⠀⠉⠉⠉⠻⡏⡗⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⣝⢏⠁⠀⠀⠀⢀⣉⣀⣀⡀⡄⠀⠀⢠⠴⠗⠗⠒⠒⠺⠋⠛⠉⠀
⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⢉⡩⠟⣓⡿⠁⠀⠀⡖⠁⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣒⢯⢕⣫⡯⠗⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡗⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡜⢛⣿⡇⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠉⠛⠛⠉⠉⠉⠉⠁⠉⠁⠁⠁⠉⠉⠉⠒⠉⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
counter = 0       
class PagesApp(App):
    CSS_PATH = "main.tcss"
    def compose(self) -> ComposeResult:
        with Horizontal():
            with Container(id = "container1"):
                yield Label("NUMBER TO BINARY INVERTER")
                with Vertical():
                    yield Input(placeholder= "input desired number", id = "input")
                    yield Static("",id = "result")
                    yield Static(site)
                    yield Static(id = "quotes")
                    yield Button("EXIT APP", id ="exit")
                    
            with Container(id = "container2"):
                yield Label("WEATHER APP")
                with VerticalScroll():
                    yield Static(cloud)
                    yield Input(placeholder="INPUT PREFERRED LOCATION", id = "input2")
                    yield Static("", id = "result2")
                    
            with Container(id ="container3"):
                yield Label("PALINDROME CHECKER")
                
                with Vertical():
                    # yield Static("A Palindrome checker checks your inputed words if its spelt the same backwords\n such a word is a palindrome")
                    
                    yield Static(sight, id = "eyes")
                    yield Static( id = "read_me")
                    yield Input(placeholder= "show your word to the Great eye", id = "input3")
                    yield Static(id = "result3")
                    yield Static(id = "quotes")
                    yield Button("read me", id = "red")

        
    async def on_input_submitted(self, event: Input.Submitted)->None:
        
        if event.input.id == "input":
            numb = event.value
        
            
            def myapp(numb):
                for chara in numb:
                    if chara.isalpha():
                        return("please input a valid number")
        
                numb = str(numb)
            
                def split(numb):
                    print(":warning:")
                    list1 = (numb.split("."))
                    if "." not in numb:
                        number = list1[0]
                        fraction = "0"
                    else:   
                        number = list1[0]
                        fraction = list1[1]
                    
                    if fraction ==[]:
                        fraction = "0"
                    return number, fraction
                
                number, fraction = split(numb)

                def binary_checker(number):
                    number = int(number)
                    binary = ""
                    while number > 0:
                        if number % 2 == 0:
                            binary = binary + "0" 
                        else:
                            binary = binary + "1"
                        number = number//2
                    binary = binary[::-1]
                    if binary =="":
                        binary ="0"
                    return binary

                binarys = binary_checker(number)
                
                def floater(fraction):
                    fraction = "0." + str(fraction)
                    fraction = float(fraction)
                    return fraction
                floated = floater(fraction)
                
                def fraction_binary(floated):
                    
                    floated = float(floated)
                    power = 0
                    while ((2**power) * floated)%1 != 0:
                        power += 1
                    fractions =int((2**power)*floated)
    
                    fract_binary = (binary_checker(fractions))
                    diff = power - len(fract_binary)
                    
                    if power > len(fract_binary):
                        fraction = (("0"*diff)+fract_binary)
                        fraction = fraction[0:9]
                        return fraction 
                    else:
                        fraction = fract_binary
                        fraction = fraction[0:9]
                        return fraction
                    
                floats = fraction_binary(floated)
                
                def joyner(binarys, floats):
            # print(binarys, floats)
                    new_string  = (binarys +"."+ floats)
                    new_float = float(new_string)
                    return new_string, new_float

                new_string, new_float = joyner(binarys, floats)
                put = str(f"Input: {numb} binary: {new_float} \n Main: {new_string}")
                return put
            
            put = myapp(numb)
            output = self.query_one("#result", Static)
            output.update(f"{put}")
            space_box = self.query_one("#quotes", Static)   
            word = "chaos is a ladder or so he said"
            my_space = ""
            for char in word:
                my_space += char
                space_box.update(my_space)
                await asyncio.sleep(0.04)
        if event.input.id =="input2":
            
            location = event.value
            import requests
            def weatherApp(location):
        
                keys = "8a7c53f2a92e452680271856251007"
                base_url = f"http://api.weatherapi.com/v1/current.json?key={keys}&q={location}"
                response = requests.get(base_url)
                data = response.json()
                myData = self.query_one("#result2")
                result = ""
                for char in location:
                    if char.isdigit():
                        myData.update(f"{location} is an invalid location")
                        return
                
                try:
                    for key, value in data["location"].items():
                        result += f"{key}: {value}\n"
                        myData.update(result)
                    myData.update("FULL WEATHER REPORT")
                    for i in data["current"]:
            
                        val = data["current"][i]
                        result += f"{i}: {val}\n"
                        myData.update(result)
                        # return result
                except:
                    myData.update(f"sorry. couldn't find information on location: {location}")
                    return

            weatherApp(location)
            
        if event.input.id == "input3":
            case = event.value
            name = case.lower()
            def pal(name, opp):
                for char in name:
                    if char.isdigit():
                        output = (f"your input is not a word\n do better thinking ")
                        return output
                
                if len(opp) == len(name):
                    if name == opp:
                        output = (f"{case} is a Palindrome")
                        return output
                    else:
                        output =(f"{case} is not a palindrome")
                        return output
                else:
                    opp += name[-(len(opp)+1)]
                    return pal(name, opp)
            

    
            out_put = pal(name, opp = "")
            Myout_put = self.query_one("#result3", Static)
            Myout_put.update("")
            
            for char in out_put:
                Myout_put.update(Myout_put.renderable + char)
                await asyncio.sleep(0.02)
                
        
    async def on_button_pressed(self, event:Button.Pressed)->None:
        
        if event.button.id == "exit":
            self.exit()
        elif event.button.id =="red":
        
            reader = self.query_one("#read_me", Static)
            game_info = "A Palindrome checker checks your inputed words if its spelt \nthe same backwards and such a word is a palindrome"
            text = ""
            

            for char in game_info:
                text += char
                reader.update(text)
                await asyncio.sleep(0.03)
                    
            
if __name__ == "__main__":
    app = PagesApp()
    app.run()